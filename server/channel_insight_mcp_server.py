# 全局导入
import json
import os
from hashlib import md5
import requests
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import sys

load_dotenv()
mcp = FastMCP("渠道信息分析洞察", instructions="渠道信息分析洞察",dependencies=["python-dotenv", "requests"])

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
        return response.json().get("data", None) or response.json().get("msgCN", None)
    except Exception as e:
        return "查询失败"
    
@mcp.tool()
def channel_insight_channel_analysis(matchKeyword: str, keywordType: str = None) -> dict:
    """
    该接口的功能是对指定企业进行渠道统计分析，输出企业在同行业中的资金实力、品牌影响力、注册资本和销售实力等多方面的数据。这些数据包括同行企业总数、同行年营业额数据、注册资本排名以及与同行的比较等，帮助用户了解企业在市场中的地位、实力及其与同行的差距。可能的使用场景包括：企业市场分析人员开展行业对比研究、投资者在评估投资风险和潜力时使用、企业管理层在制定发展战略时参考，以及政府或金融机构在进行宏观经济分析时使用。这一接口还为企业的市场研究、竞争分析以及对外展示其市场定位和优势提供了翔实的数据支持。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码）

    返回参数:
    - categoryCount: 同行总数 类型：int
    - data: 同行年营业额数据 类型：list of dict
    - financialStat: 资金实力分析 类型：dict
    - name: 数据范围 类型：string
    - ratio: 同行比例 类型：float
    - power: 同行数量 类型：int
    - regCapitalRank: 注册资本排名 类型：int - 显示注册资本超过同行的数量
    - name: 数据范围 类型：string
    - productBrandList: 品牌占比 类型：list of dict
    - number: 数量 类型：int
    - regCapitalScope: 所在注册资本范围 类型：string
    - name: 数据范围 类型：string
    - number: 数量 类型：int
    - ratio: 同行比例 类型：float
    - ratio: 同行比例 类型：float
    - salesStat: 销量实力分析 类型：dict
    - annualTurnoverRank: 年营业排名 类型：int - 显示营业额超过同行的数量
    - productCategoryList: 品类占比 类型：list of dict
    - annualTurnoverScope: 所在年营业额范围 类型：string
    - data: 同行年营业额数据 类型：list of dict
    - name: 数据范围 类型：string
    - categoryCount: 同行总数 类型：int
    - power: 同行数量 类型：int
    - ratio: 同行比例 类型：float
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'keywordType': keywordType,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('66f3d8bf64bd2be52d68a0fe', params)


@mcp.tool()
def channel_insight_fuzzy_search(matchKeyword: str, pageIndex: int = 1, pageSize: int = None) -> dict:
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
def channel_insight_channel_search(matchKeyword: str, address: str = None, keywordType: str = None, pageIndex: int = 1,
                   channelTradeType: str = None, pageSize: int = None) -> dict:
    """
    该接口的功能是根据输入的工厂名称或产品名称以及指定的搜索条件，提供匹配的企业信息列表，包括企业基本信息及主营产品等。此接口可能用于在供应链管理平台或B2B采购平台中，帮助采购商快速定位符合特定条件的供应商，进行商业合作洽谈或市场调查。


    请求参数:
    - address: 地区 类型：list of list - 参考格式：[["广东省","中山市"],["广东省","潮州市"]]
    - keywordType: 搜索类型 类型：select - 搜索类型枚举（综合搜索，主营产品）
    - matchKeyword: 匹配关键词 类型：string - 工厂名称或产品名称（搜索多个词，使用顿号隔开，如"北京、上海"）
    - pageIndex: 页码 类型：int - 从1开始
    - channelTradeType: 销售模式 类型：select - 销售模式枚举（全部，外贸，内贸）
    - pageSize: 分页大小 类型：int - 一页最多获取50条数据

    返回参数:
    - total: 总数 类型：int - 最多返回10W家
    - mainProducts: 主营产品 类型：list of string
    - foundTime: 成立日期 类型：string
    - name: 企业名称 类型：string
    - regCapital: 注册资本 类型：dict
    - nameId: 企业id 类型：string
    - tagNames: 产品类目 类型：list of string
    - resultList: 结果列表 类型：list of dict
    """
    # 构建请求参数
    params = {
        'address': address,
        'keywordType': keywordType,
        'matchKeyword': matchKeyword,
        'pageIndex': pageIndex,
        'channelTradeType': channelTradeType,
        'pageSize': pageSize,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('66b71b498dd25dbfbe8b0acd', params)


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
    