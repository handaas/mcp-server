# 全局导入
import json
import os
from hashlib import md5
import requests
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import sys

load_dotenv()

mcp = FastMCP("工厂信息分析洞察", instructions="工厂信息分析洞察",dependencies=["python-dotenv", "requests"])

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
def factory_insight_fuzzy_search(matchKeyword: str, pageIndex: int = 1, pageSize: int = None) -> dict:
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
def factory_insight_factory_product_stats(matchKeyword: str, keywordType: str = None) -> dict:
    """
    该接口可以根据工厂主体名称，获取工厂的产品统计信息，包括服务品牌数量、主营产品数量、产品标签、产品类目统计信息（类目及对应数量）等，可以应用于市场分析、供应商评估、采购决策支持等领域，帮助企业全面了解工厂的产品结构与市场定位，优化合作伙伴选择，提升采购与合作的精准性。



    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码）

    返回参数:
    - serviceBrandCount: 服务品牌数量 类型：int
    - mainProductCount: 主营产品数量 类型：int
    - tagNames: 产品标签 类型：list of string
    - productCategoriesStatInfo: 产品类目统计信息 类型：list of dict
    - name: 类目 类型：string
    - value: 数量 类型：int
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'keywordType': keywordType,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('6725e5b9ba65854594baebd2', params)


@mcp.tool()
def factory_insight_factory_capabilities(matchKeyword: str, keywordType: str = None) -> dict:
    """
    该接口用于查询和获取指定企业的工厂生产实力和资质信息，包括生产线配置、人员配置、设备详情、质量管理及相关资质等详细数据。可能应用于供应链管理中，加强采购方对供应商生产能力的评估与筛选。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码）

    返回参数:
    - assemblyLine: 生产流水线 类型：int
    - boarderStaffNumber: 打版人数 类型：string
    - isSupportProofing: 是否支持打样 类型：int
    - inspectionStaffNumber: 检验人数 类型：string
    - mainDeviceList: 设备列表 类型：list of dict
    - inspectionGroup: 检验小组 类型：string
    - brand: 设备品牌 类型：string
    - equipName: 设备名称 类型：string
    - equipNum: 设备数量 类型：float
    - equipVersion: 设备型号 类型：int
    - managementSystemCertification: 管理体系认证 类型：list of string
    - monthlyProductionAmountValue: 月产值 类型：string
    - companyTechnicList: 工厂工艺 类型：list of string
    - patentCertificateImageList: 相关资质列表 类型：list of dict
    - image: 图片 类型：string
    - imageLink: 图片链接 类型：string
    - patentName: 资质名称 类型：string
    - enterpriseCertification: 生产质量认证 类型：list of string
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'keywordType': keywordType,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('66aa4eac4bb1f40b86c46ee6', params)


@mcp.tool()
def factory_insight_factory_search(matchKeyword: str, keywordType: str, pageIndex: int = 1, pageSize: int = 10,
                   address: list = []) -> dict:
    """
    该接口的功能是根据用户输入的条件（如工厂名称、主营产品、产品名称以及地理位置关键词）搜索符合条件的工厂信息(注意：该接口地区是必填项)，并返回包括企业基本信息和统计总数的结果列表。该接口可能用于企业采购部门筛选供应商、市场调研机构搜集数据、或者政府相关部门进行经济数据分析等场景，帮助用户快速找到并评估潜在的合作工厂或市场竞争者。


    请求参数:
    - pageIndex: 页码 类型：int - 从1开始
    - pageSize: 分页大小 类型：int - 一页最多获取10条
    - matchKeyword: 工厂名称、主营产品、产品名称以及地理位置关键词 类型：string - 必填项
    - address: 地区 类型：list of list - 参考如下格式：[["广东省","中山市"],["广东省","潮州市"]] - 必填项
    - keywordType: 主体类型 类型：select - 主体类型枚举值（综合搜索，工厂名称，主营产品，产品名称

    返回参数:
    - resultList: 列表结果 类型：list of dict
    - foundTime: 成立日期 类型：string
    - name: 企业名称 类型：string
    - mainProducts: 主营产品 类型：list of string
    - regCapital: 注册资本 类型：dict
    - total: 总数 类型：int - 最大显示100001
    - nameId: 企业id 类型：string
    """
    # 构建请求参数
    params = {
        'pageIndex': pageIndex,
        'pageSize': pageSize,
        'matchKeyword': matchKeyword,
        'address': json.dumps(address, ensure_ascii=False) if isinstance(address, list) else address,
        'keywordType': keywordType,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('66aa4eac4bb1f40b86c46efe', params)


@mcp.tool()
def factory_insight_factory_profile(matchKeyword: str, keywordType: str = None) -> dict:
    """
    该接口的功能是根据输入的企业标识信息（如企业名称、注册号或社会信用代码）提供该企业的工厂概况，包括风险评估和详细的工厂信息。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码)

    返回参数:
    - accountPeriodRisk: 账期风险 类型：string
    - factoryAddress: 工厂地址 类型：dict
    - city: 城市 类型：string
    - district: 地区 类型：string
    - province: 省份 类型：string
    - value: 地址 类型：float
    - monthlyProductionAmountValue: 月产值 类型：string
    - factoryScale: 工厂规模 类型：string
    - foundTime: 成立时间 类型：string
    - name: 企业名称 类型：string
    - factoryTypeList: 工厂类型 类型：list of string
    - nameId: 企业ID 类型：string
    - regCapital: 注册资本 类型：dict
    - coinType: 币种 类型：string - e.g.人民币
    - value: 金额 类型：float
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'keywordType': keywordType,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('66aa4eac4bb1f40b86c46f0b', params)


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
    