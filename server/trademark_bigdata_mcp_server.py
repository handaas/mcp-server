# 全局导入
import json
import os
from hashlib import md5
import requests
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import sys

load_dotenv()

mcp = FastMCP("商标大数据", instructions="商标大数据",dependencies=["python-dotenv", "requests"])

INTEGRATOR_ID = os.environ.get("INTEGRATOR_ID")
SECRET_ID = os.environ.get("SECRET_ID")
SECRET_KEY = os.environ.get("SECRET_KEY")

def call_api(product_id: str, params: dict) -> dict:
    """
    调用API接口
    
    参数:
      - product_id: 数据产品ID
      - params: 接口参数
    
    返回:
      - 接口返回的JSON数据
    """
    if not params:
        params = {}
    
    if not INTEGRATOR_ID:
        return {"error": "对接器ID不能为空"}
    
    if not SECRET_ID:
        return {"error": "密钥ID不能为空"}
    
    if not SECRET_KEY:
        return {"error": "密钥不能为空"}
    
    if not product_id:
        return {"error": "产品ID不能为空"}
    
    call_params = {
        "product_id": product_id,
        "secret_id": SECRET_ID,
        "params": json.dumps(params, ensure_ascii=False)
    }
    
    # 生成签名
    keys = sorted(list(call_params.keys()))
    params_str = ""
    for key in keys:
        params_str += str(call_params[key])
    params_str += SECRET_KEY
    sign = md5(params_str.encode("utf-8")).hexdigest()
    call_params["signature"] = sign
    
    # 调用API
    url = f'https://console.handaas.com/api/v1/integrator/call_api/{INTEGRATOR_ID}'
    try:
        response = requests.post(url, data=call_params)
        return response.json().get("data", "查询为空")
    except Exception as e:
        return "查询失败"
    
@mcp.tool()
def trademark_bigdata_fuzzy_search(matchKeyword: str, pageIndex: int = None, pageSize: int = None) -> dict:
    """
    该接口的功能是根据提供的企业名称、人名、品牌、产品、岗位等关键词模糊查询相关企业列表。返回匹配的企业列表及其详细信息，用于查找和识别特定的企业信息。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 查询各类信息包含匹配关键词的企业
    - pageIndex: 分页开始位置 类型：int
    - pageSize: 分页结束位置 类型：int - 一页最多获取50条数据

    返回参数:
    - total: 总数 类型：int
    - resultList: 结果列表 类型：list of dict
    - annualTurnover: 年营业额 类型：string
    - formerNames: 曾用名 类型：list of string
    - address: 注册地址 类型：string
    - foundTime: 成立时间 类型：string
    - enterpriseType: 企业主体类型 类型：string
    - legalRepresentative: 法定代表人 类型：string
    - homepage: 企业官网 类型：string
    - legalRepresentativeId: 法定代表人id 类型：string
    - prmtKeys: 推广关键词 类型：list of string
    - operStatus: 企业状态 类型：string
    - logo: 企业logo 类型：string
    - nameId: 企业id 类型：string
    - regCapitalCoinType: 注册资本币种 类型：string
    - regCapitalValue: 注册资本金额 类型：int
    - name: 企业名称 类型：string
    - catchReason: 命中原因 类型：dict
    - catchReason.name: 企业名称 类型：list of string
    - catchReason.formerNames: 曾用名 类型：list of string
    - catchReason.holderList: 股东 类型：list of string
    - catchReason.recruitingName: 招聘岗位 类型：list of string
    - catchReason.address: 地址 类型：list of string
    - catchReason.operBrandList: 品牌 类型：list of string
    - catchReason.goodsNameList: 产品名称 类型：list of string
    - catchReason.phoneList: 固话 类型：list of string
    - catchReason.emailList: 邮箱 类型：list of string
    - catchReason.mobileList: 手机 类型：list of string
    - catchReason.patentNameList: 专利 类型：list of string
    - catchReason.certNameList: 资质证书 类型：list of string
    - catchReason.prmtKeys: 推广关键词 类型：list of string
    - catchReason.socialCreditCode: 统一社会信用代码 类型：list of string
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'pageIndex': pageIndex,
        'pageSize': pageSize,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('675cea1f0e009a9ea37edaa1', params)


@mcp.tool()
def trademark_bigdata_trademark_search(matchKeyword: str, keywordType: str = None,
                     tmStatus: str = None, pageIndex: int = 1, pageSize: int = 10) -> dict:
    """
    该接口为用户提供商标信息的搜索功能，用户可以根据商标名称、申请号、申请人名称或代理机构名称等条件进行查询，并通过商标状态进一步过滤结果。该接口特别适合于商标代理机构、企业或法律咨询公司在进行商标查询、情况分析和状态跟踪时使用，它帮助用户快速定位所需的商标信息，并了解商标的当前状态、申请和注册信息，从而便于后续的商标管理和法律事务处理。特别是在商标申请、品牌保护及市场竞争分析等场景下，这一接口能够显著提高工作效率和信息利用的准确度。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 商标名称/申请号/申请人名称/代理机构名称
    - keywordType: 搜索方式 类型：select - 搜索方式枚举（商标名称，申请号，申请人，代理机构，默认匹配全部)
    - pageIndex: 页码 类型：int - 从1开始
    - pageSize: 分页大小 类型：int - 一页最多获取50条数据
    - tmStatus: 商标状态 类型：select - 商标状态枚举（驳回复审中，撤销/无效宣告申请审查中，初审公告，等待驳回复审，等待实质审查，商标申请中，商标无效，商标已注册，商标异议中）

    返回参数:
    - resultList: 结果列表 类型：list of dict - 商标列表
    - _id: 商标id 类型：string
    - tmAgentName: 代理机构名称 类型：string
    - tmAgentNameId: 代理机构id 类型：string
    - tmCompanyNameId: 申请人id 类型：string
    - tmName: 商标名称 类型：string
    - tmImage: 商标图片链接 类型：string
    - tmApplicationTime: 申请日期 类型：string
    - tmCompanyName: 申请人名称 类型：string
    - tmRegNum: 申请号 类型：string
    - tmRegTime: 注册日期 类型：string
    - tmServiceContents: 商品服务项 类型：list of dict
    - similarGroup: 相似群组 类型：string
    - tmSingleInternationalClass: 国际分类 类型：string
    - detail: 明细 类型：string
    - tmSpecialBeginDate: 专用权开始日期 类型：string
    - tmSpecialEndDate: 专用权截止日期 类型：string
    - internationalClass: 国际分类 类型：string
    - code: 编码 类型：string
    - tmStatus: 商标状态 类型：string
    - tmTrialTime: 初审公告日期 类型：string
    - total: 总数 类型：int - 商标数量
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'keywordType': keywordType,
        'pageIndex': pageIndex,
        'pageSize': pageSize,
        'tmStatus': tmStatus,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('66b485eadaf8c77fb249a3cc', params)


@mcp.tool()
def trademark_bigdata_trademark_profile(matchKeyword: str, keywordType: str = None) -> dict:
    """
    该接口的功能是根据输入的企业标识信息（如企业名称、注册号等），返回与该企业相关的商标概况信息，包括商标总数、商标类别、商标状态列表等。这一接口的主要用途在于帮助企业、法律顾问、知识产权代理机构、竞争对手和市场研究人员快速获取某企业的商标注册情况，以便进行市场分析、竞争对手跟踪、企业决策、风险评估及品牌保护等场景。这可用于企业在商标管理过程中，监控自己的商标资产，或用于竞争对手分析，通过了解竞争对手的商标布局判断其市场策略。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码)

    返回参数:
    - tmTypeList: 涵盖商标类别 类型：list of string
    - tmCount: 商标数量 类型：int
    - tmNumberThisYear: 最近一年申请商标数 类型：int
    - tmInvalidNumber: 无效商标数 类型：int
    - tmStatusList: 商标状态列表 类型：list of srting
    - tmValidNumber: 有效商标数 类型：int
    - tmStatusStat: 商标状态统计 类型：dict
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'keywordType': keywordType,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('671357d127ab3417e1f3f21b', params)


@mcp.tool()
def trademark_bigdata_trademark_stats(matchKeyword: str, keywordType: str = None) -> dict:
    """
    该接口的功能是根据输入的企业相关信息（如企业名称、注册号、统一社会信用代码或企业ID）和主体类型，返回该企业的商标申请趋势、商标注册趋势、商标状态统计及商标类别统计等信息。该接口的用途在于帮助企业了解自身或竞争对手在商标申请和注册方面的动态，为市场分析、竞争战略制定提供数据支持。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码）

    返回参数:
    - year: 年份 类型：string
    - tmRegTimeStat: 商标注册趋势 类型：list of dict
    - tmAppTimeStat: 商标申请趋势 类型：list of dict
    - count: 商标数量 类型：int
    - count: 商标数量 类型：int
    - year: 年份 类型：string
    - tmStatusStat: 商标状态统计 类型：list of dict
    - tmStatus: 商标状态 类型：string
    - count: 商标数量 类型：int
    - count: 商标数量 类型：int
    - tmTypeStats: 商标类别统计 类型：list of dict
    - tmName: 商标类别 类型：string
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'keywordType': keywordType,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('66d5b7df537c3f61d646c2dc', params)


if __name__ == "__main__":
    print("正在启动MCP服务...")
    # 解析第一个参数
    if len(sys.argv) > 1:
        start_type = sys.argv[1]
    else:
        start_type = "stdio"

    print(f"启动方式: {start_type}")
    if start_type == "stdio":
        print("正在使用stdio方式启动MCP服务器...")
        mcp.run(transport="stdio")
    if start_type == "sse":
        print("正在使用sse方式启动MCP服务器...")
        mcp.run(transport="sse")
    elif start_type == "streamable-http":
        print("正在使用streamable-http方式启动MCP服务器...")
        mcp.run(transport="streamable-http")
    else:
        print("请输入正确的启动方式: stdio 或 sse 或 streamable-http")
        exit(1)
    