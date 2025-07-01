# 全局导入
import json
import os
from hashlib import md5
import requests
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import sys

load_dotenv()

mcp = FastMCP("上云大数据", instructions="上云大数据",dependencies=["python-dotenv", "requests"])

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
def cloudmigration_cloud_assets(matchKeyword: str, keywordType: str = None) -> dict:
    """
    该接口用于查询企业的云上资产信息，通过输入企业相关标识，输出企业在云上的各种资产状况及特征信息，如有效域名、云服务厂商及云用量等。此接口的使用场景包括政府或商业机构监测企业上云情况，评估企业云服务及基础架构的使用规模与安全性，通过全面了解和评估企业的上云资产，为制定云服务采购策略、进行风险分析、提升企业信息化服务水平等提供数据支持和决策依据。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业，regNumber：注册号，socialCreditCode：统一社会信用代码)

    返回参数:
    - effectiveSubDomainList: 有效域名列表 类型：list of string
    - cloudServerList: 云服务厂商列表 类型：list of string
    - effectiveSubDomainNum: 有效域名数量 类型：int
    - subDomainNum: 子域名数量 类型：int
    - hasOverseasCloudService: 有无海外服务器 类型：int - 0:无 1：有
    - cloudServiceProviderRatio: 云服务厂商比例 类型：list of dict
    - ratio: 云服务厂商比例 类型：float
    - cloudService: 云服务商名称 类型：string
    - cloudServerNumInterval: 云用量范围 类型：string
    - hasCdn: 有无使用CDN 类型：int - 0:无 1：有
    - cdnServerNum: CDN使用规模 类型：int
    - cloudConsumptionScale: 上云资产等级 类型：string
    - cdnServerList: CDN服务商列表 类型：list of string
    - hasIDC: 有无使用IDC 类型：int - 0:无 1：有
    - hasCloudStorage: 有无使用云存储 类型：int - 0:无 1：有
    - subDomainList: 子域名列表 类型：list of string
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'keywordType': keywordType,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('6704f43fa9a1ec205f429e05', params)


@mcp.tool()
def cloudmigration_fuzzy_search(matchKeyword: str, pageIndex: int = 1, pageSize: int = None) -> dict:
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
def cloudmigration_domain_info(matchKeyword: str, pageIndex: int = 1, keywordType: str = None, pageSize: int = None) -> dict:
    """
    该接口的功能是根据输入的企业标识信息查询与该企业相关的所有已注册的域名信息，包括域名名称、对应网址、审核时间等详情。该接口可能适用于企业想要管理自己的互联网资产时，通过将其名下的域名和网站信息整理为报告，或者企业或第三方需要进行域名合规性检查、对网站进行备案审查时，快速获取相关数据信息，以此确认网站是否为企业的官方域名，确保其品牌安全。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - pageIndex: 页码 类型：int 
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码)
    - pageSize: 分页大小 类型：int - 一页最多获取50条数据

    返回参数:
    - domainName: 域名名称 类型：string
    - domainUrl: 网址 类型：string
    - total: 总数 类型：int
    - filingAuditTime: 审核时间 类型：string
    - resultList: 列表结果 类型：list of dict
    - isHomePage: 是否官网 类型：int
    - websiteRecord: 网站备案号 类型：string
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'pageIndex': pageIndex,
        'keywordType': keywordType,
        'pageSize': pageSize,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('66a0f258ce3408eb23b56706', params)


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
    