# 全局导入
import json
import os
from hashlib import md5
import requests
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import sys

load_dotenv()

mcp = FastMCP("资质大数据", instructions="资质大数据",dependencies=["python-dotenv", "requests"])

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
def qualification_bigdata_honor_qualifications(matchKeyword: str, keywordType: str = None) -> dict:
    """
    该接口的功能是根据输入的企业相关信息（如企业名称、注册号、统一社会信用代码等），查询并返回企业获得的荣誉资质详细信息，包括认定机关、资质级别、有效期等。它的用途在于帮助企业、投资者、合作伙伴或监管机构等快速获取某家企业的资质背景，用于资质验证、市场调研、企业评估或合规审核等场景，为合同签署或商业决策提供关键的背景验证信息。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码)

    返回参数:
    - total: 总数 类型：int
    - resultList: 结果列表 类型：list of dict
    - eaqBeginDate: 有效期开始日期 类型：string
    - eaqPublishDate: 发布日期 类型：string
    - eaqRecognitionLevel: 资质级别 类型：string
    - eaqTitle: 公告标题 类型：string
    - eaqEndDate: 有效期截止日期 类型：string
    - eaqType: 资质类型 类型：string
    - eaqAuthority: 认定机关 类型：string
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'keywordType': keywordType,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('66b71b498dd25dbfbe8b0a9f', params)


@mcp.tool()
def qualification_bigdata_enterprise_qualifications(matchKeyword: str, keywordType: str = None, pageIndex: int = 1,
                              pageSize: int = None) -> dict:
    """
    该接口的功能是查询和返回企业的资质信息，通过输入企业名称、注册号、统一社会信用代码或企业ID等信息，能够获取企业的资质总数、资质信息列表、企业资质分类、资质类型、发布年份、发布日期、资质级别、发布单位、高新行业分类以及绿色设计等多维度数据。此接口可广泛应用于企业合作评估、项目招投标、行业监管、市场调研等场景，帮助用户全面了解企业的资质水平和专业能力。例如，企业在参与项目投标时，可利用该接口查询自身资质是否符合要求；合作伙伴可通过此接口核实企业的资质真实性，以评估合作风险；政府部门也可借此进行行业资质监管，规范市场秩序。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码)
    - pageIndex: 页码 类型：int - 从1开始
    - pageSize: 分页大小 类型：int - 一页最多获取10条数据

    返回参数:
    - total: 资质总数 类型：int
    - resultList: 资质信息列表 类型：list of dict
    - qualificationClasses: 企业资质分类 类型：string - 1：企业创新与成长类，2：科技研发与创新类，3：科技服务与孵化类，4：知识产权类，5：产业升级与转型类
    - qualificationType: 资质类型 类型：string
    - publishYear: 发布年份 类型：int
    - publishDate: 发布日期 类型：string
    - qualificationLevel: 资质级别 类型：string
    - agency: 发布单位 类型：string
    - highTechIndustryList: 高新行业分类 类型：list of string
    - greenProducts: 绿色设计产品 类型：string
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'keywordType': keywordType,
        'pageIndex': pageIndex,
        'pageSize': pageSize,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('67f3b410ac893a1d33dadef5', params)


@mcp.tool()
def qualification_bigdata_fuzzy_search(matchKeyword: str, pageIndex: int = 1, pageSize: int = None) -> dict:
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
def qualification_bigdata_administrative_licenses(matchKeyword: str, pageSize: int = 10, pageIndex: int = 1,
                            keywordType: str = None) -> dict:
    """
    该接口的功能是根据提供的企业标识信息（如企业名称、注册号、统一社会信用代码等）查询并返回企业的相关行政许可信息，包括许可详情和有效期限。该接口可能用于政府部门、金融机构以及相关监督机构在对企业进行合规性检查、贷款审批、背景调查或其他需要了解企业合法资质的情形中，以有效确保企业的经营活动符合规定，并帮助相关机构做出更为准确的判断和决策。


    请求参数:
    - pageSize: 分页大小 类型：int - 一页最多获取50条数据
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - pageIndex: 页码 类型：int - 从1开始
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码)

    返回参数:
    - total: 总数 类型：int
    - resultList: 列表结果 类型：list of dict
    - authority: 许可机关 类型：string
    - auditType: 审核类型 类型：string
    - beginDate: 许可有效期自 类型：string
    - content: 许可内容 类型：string
    - status: 当前状态 类型：string
    - endDate: 许可有效期至 类型：string
    - creditPubLicenseId: 行政许可决定文书号 类型：string
    - fileName: 行政许可决定文书名称 类型：string
    """
    # 构建请求参数
    params = {
        'pageSize': pageSize,
        'matchKeyword': matchKeyword,
        'pageIndex': pageIndex,
        'keywordType': keywordType,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('669fb610a32fff27615b0c03', params)


@mcp.tool()
def qualification_bigdata_qualification_certificate_profile(matchKeyword: str, keywordType: str = None) -> dict:
    """
    该接口的功能是根据企业的基本信息（如企业名称、注册号、统一社会信用代码或企业ID）查询该企业的资质证书相关概况，包括总证书数量、最近一年内获得的证书数量、首次获得证书的日期、最近获得证书的日期以及涵盖的证书类别。可能的使用场景包括：政府部门或第三方审计机构对企业资质进行审核，企业内部用于管理和跟踪自身或竞争对手的资质变化，投资者或合作伙伴评估企业的资质可信度，以及行业报告和市场分析以了解企业资质的分布和趋势。此接口有助于提高信息透明度和决策的准确性。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码)

    返回参数:
    - certificateCount: 证书数量 类型：int
    - certNumberThisYear: 最近一年获证数量 类型：int
    - certFirstPublishTime: 初次获证日期 类型：string
    - certTypeList: 涵盖证书类别 类型：list of string
    - certLastPublishTime: 最近获证日期 类型：string
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'keywordType': keywordType,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('66a24df68912d491d34ab0a1', params)


@mcp.tool()
def qualification_bigdata_hitech_enterprise_cert(matchKeyword: str, pageIndex: int = 1, pageSize: int = 10,
                           keywordType: str = None) -> dict:
    """
    该接口的功能是查询特定企业的高新技术企业资质信息，包括证书状态、编号、发证机构等详细信息。具体用途在于帮助企业或者相关机构快速验证企业是否具备高新技术资质，以及资质的有效期限和类别。该接口可能的使用场景包括政府部门对企业资质的审查，投资公司在投资前对企业的资质核验，以及其他企业在进行商业合作前对合作方资质的审核。此查验过程能够提高业务决策的准确性和可靠性。


    请求参数:
    - pageIndex: 页码 类型：int - 从1开始
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - pageSize: 分页大小 类型：int - 一页最多获取50条数据
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码)

    返回参数:
    - total: 总数 类型：int
    - resultList: 列表结果 类型：list of dict
    - certId: 证书编号 类型：string
    - certStatus: 证书状态 类型：string
    - certPublishTime: 颁证日期 类型：string
    - certAuthority: 发证机构 类型：string
    - certType: 资质类别 类型：string
    - certExpireTime: 截止日期 类型：string
    """
    # 构建请求参数
    params = {
        'pageIndex': pageIndex,
        'matchKeyword': matchKeyword,
        'pageSize': pageSize,
        'keywordType': keywordType,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('669f8ec259dda752d9799950', params)


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
    