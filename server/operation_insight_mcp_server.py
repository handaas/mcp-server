import json
import os
from hashlib import md5
import requests
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import sys

load_dotenv()

mcp = FastMCP("企业经营分析洞察", instructions="企业经营分析洞察",dependencies=["python-dotenv", "requests"])

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
def operation_insight_product_tags(matchKeyword: str, keywordType: str = None) -> dict:
    """
    该接口的功能是根据输入的企业基本信息（如企业名称、注册号、统一社会信用代码或企业ID）以及主体类型枚举，返回该企业的产品标签，用于识别企业产品的特性和类别。此接口可能用于大数据分析系统、商业智能平台或企业内部信息管理系统中，以支持市场分析、竞争对手分析、产品分类管理以及商业决策等场景。通过将企业信息与产品标签关联，可以帮助企业更好地创新产品、优化市场策略，进而提升竞争优势。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码）

    返回参数:
    - tagNames: 产品标签 类型：list of string
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'keywordType': keywordType,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('66c33eff3c0917a9a02feb6f', params)


@mcp.tool()
def operation_insight_company_trends(matchKeyword: str, keywordType: str = None) -> dict:
    """
    根据企业名称/企业ID等企业标识，查询和返回企业近3至12个月的动向标签等数据，包括人员扩张、开设/注销分子公、新增城市、新增融资、异地中标、入选榜单、法人变更、租约临期等企业动向标签数据。此接口可用于市场监测、竞争情报分析、投资跟踪等领域，帮助用户及时掌握企业的最新发展动态，以便提前布局或调整策略。例如，竞争对手可通过该接口监测对手的扩张动向，投资机构可据此跟踪投资企业的运营情况，以评估投资价值和风险。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码)

    返回参数:
    - isStaffExpandIn3Month: 是否3个月内人员扩张 类型：int
    - isStaffExpandIn6Month: 是否6个月内人员扩张 类型：int
    - isStaffExpandIn12Month: 是否12个月内人员扩张 类型：int
    - isFoundSubsidiaryIn3Month: 是否3个月内开设子公司 类型：int
    - isCancelSubsidiaryIn3Month: 是否3个月内注销子公司 类型：int
    - isFoundBranchIn3Month: 是否3个月内开设分公司 类型：int
    - isCancelBranchIn3Month: 是否3个月内注销分公司 类型：int
    - isExpandNewCityIn3Month: 是否3个月内新增城市 类型：int
    - isExpandNewCityIn6Month: 是否6个月内新增城市 类型：int
    - isExpandNewCityIn12Month: 是否12个月内新增城市 类型：int
    - isNewFinancingIn3Month: 是否3个月内新增融资 类型：int
    - isNewFinancingIn6Month: 是否6个月内新增融资 类型：int
    - isNewFinancingIn12Month: 是否12个月内新增融资 类型：int
    - isDiffAreaWinBidIn3Month: 是否3个月内异地中标 类型：int
    - isDiffAreaWinBidIn6Month: 是否6个月内异地中标 类型：int
    - isDiffAreaWinBidIn12Month: 是否12个月内异地中标 类型：int
    - isAuthorityListIn6Month: 是否近6个月入选榜单 类型：int
    - isAuthorityListIn12Month: 是否近12个月入选榜单 类型：int
    - isLegalRpAlterIn3Month: 是否近3个月法人变更 类型：int
    - isLegalRpAlterIn6Month: 是否近6个月法人变更 类型：int
    - isLegalRpAlterIn12Month: 是否近12个月法人变更 类型：int
    - nYearLeaseAboutToExpire: 剩余租约年限 类型：int
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'keywordType': keywordType,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('67f3af2fac893a1d33dadebe', params)


@mcp.tool()
def operation_insight_brand_profile(matchKeyword: str, keywordType: str = None) -> dict:
    """
    该接口的功能是提供企业品牌的基本信息，包括品牌发源地、创立年份、所属行业和主营产品，根据输入的企业名称、注册号、统一社会信用代码或企业id进行查询。此接口可用于市场分析、竞争对手调查、企业背景调查等场景，帮助企业、投资者或研究人员快速获取目标企业的品牌概况，从而支持商业决策、品牌合作或投资评估。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码）

    返回参数:
    - brandCradleList: 品牌发源地 类型：list of string
    - brandCreateTime: 品牌创立年份 类型：list of dict
    - brandIndustryList: 品牌所属行业 类型：list of string
    - brandProductList: 主营产品 类型：list of string
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'keywordType': keywordType,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('66c33eff3c0917a9a02feb80', params)


@mcp.tool()
def operation_insight_enterprise_rankings(matchKeyword: str, keywordType: str = None, pageIndex: int = 1,
                        pageSize: int = None) -> dict:
    """
    该接口的功能是查询和返回企业的上榜信息，通过输入企业名称、注册号、统一社会信用代码或企业ID等信息，能够获取榜单总数、榜单信息列表、榜单类型、上榜公司名、榜单名称、排名、发布年份、榜单级别以及发布单位等多维度数据。此接口可用于市场分析、行业研究、投资决策、品牌评估等场景，帮助用户了解企业在行业内的地位和影响力。例如，投资机构可通过该接口筛选出行业内表现优异的企业作为潜在投资对象；企业自身可借此了解自身在行业中的排名变化，以便制定相应的发展战略；行业研究机构也可利用此数据进行市场趋势分析和行业竞争力评估。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码)
    - pageIndex: 页码 类型：int - 从1开始
    - pageSize: 分页大小 类型：int - 一页最多获取10条数据

    返回参数:
    - total: 榜单总数 类型：int
    - resultList: 榜单信息列表 类型：list of dict
    - rankingListType: 榜单类型 类型：string - 世界500强榜单，中国500强榜单，民营500强榜单，新经济500强榜单，制造业500强榜单，制造业民营500强榜单
    - rankingListCompanyName: 上榜公司名 类型：string
    - rankingListName: 榜单名称 类型：string
    - rank: 排名 类型：int
    - rankingListYear: 发布年份 类型：int
    - rankingListLevel: 榜单级别 类型：string
    - rankingListInstitution: 发布单位 类型：string
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
    return call_api('67f3be85ac893a1d33dadfbf', params)


@mcp.tool()
def operation_insight_business_scale(matchKeyword: str, keywordType: str = None) -> dict:
    """
    该接口用于根据企业标识信息（如企业名称、注册号等）获取企业的经营规模相关信息，包括根据算法识别评估的企业人员规模及企业年营业额区间信息。此接口可以快速获取企业的基本经营实力及经营活跃度。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码）

    返回参数:
    - enterpriseScale: 人员规模 类型：string
    - annualTurnover: 年营业额 类型：string
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'keywordType': keywordType,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('67189489ae286373219cdd32', params)


@mcp.tool()
def operation_insight_fuzzy_search(matchKeyword: str, pageIndex: int = 1, pageSize: int = None) -> dict:
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
def operation_insight_news_sentiment_stats(matchKeyword: str, keywordType: str = None) -> dict:
    """
    该接口的功能是根据输入的企业标识信息（如名称、注册号等），查询并统计该企业的舆情情感类型，包括消极、中立、积极、和未知四类情感的分布及其趋势变化。该接口主要用于企业的声誉管理和舆情监控，帮助企业了解社会对其的评价和情绪变化趋势，从而在公关、市场策略调整、风险预警等方面进行及时决策。适用场景包括企业需要进行危机公关时，分析特定时期内的舆情变化；或在日常进行品牌形象监控，判断市场对公司行为或决策的反应等。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码)

    返回参数:
    - newsSentimentStats: 舆情情感类型统计 类型：dict - neutral：中立，negative：消极，positive：积极，unknown：未知
    - sentimentLabelList: 所有舆情类别列表 类型：list of string - neutral：中立，negative：消极，positive：积极
    - newsSentimentTrend: 舆情趋势 类型：dict
    - month: 月份 类型：string - 格式：yyyy-mm
    - stats: 情感类型 类型：dict - negative：消极，positive：积极
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'keywordType': keywordType,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('66b338e274bf098447db7efd', params)


@mcp.tool()
def operation_insight_similar_projects(matchKeyword: str, pageIndex: int = 1, pageSize: int = 10, keywordType: str = None) -> dict:
    """
    该接口的功能是根据输入的企业识别信息（如企业名称、注册号、统一社会信用代码或企业id）和主体类型，查询与该企业相关的相似项目信息，并返回这些项目信息的详细描述，包括项目所属企业、最新融资轮次、项目概述及相关图片、企业id、项目名称和相似项目的总数。该接口的场景利用包括企业投资分析、市场竞争分析、公司内部项目管理系统中用于评估企业的项目布局情况或潜在投资机会的探查等，方便使用者掌握企业相关或竞争企业的项目动态。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - pageIndex: 页码 类型：int - 从1开始
    - pageSize: 分页大小 类型：int - 一页最多获取10条数据
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码)

    返回参数:
    - resultList: 结果列表 类型：list of dict
    - logo: 项目图片 类型：string
    - fpIntroduction: 项目概述 类型：string
    - nameId: 所属企业id 类型：string
    - projectName: 项目名称 类型：string
    - total: 总数 类型：int
    - enterpriseName: 所属企业 类型：string
    - financingSeries: 最新轮次 类型：string
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'pageIndex': pageIndex,
        'pageSize': pageSize,
        'keywordType': keywordType,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('66b0a51fce5e524754b8502d', params)


@mcp.tool()
def operation_insight_tax_qualifications(matchKeyword: str, keywordType: str = None) -> dict:
    """
    该接口用于查询企业的税务资质信息，通过输入企业名称、注册号、统一社会信用代码或企业id来获取企业的税务资质详细资料, 例如纳税人识别号、纳税人名称、资质全称等。此接口主要用于企业在进行合规审查、税务申报或者与政府机构进行必要资质验证时的场景，以确保企业提交的信息准确无误，符合相关的法律要求和税务规定。


    请求参数:
    - matchKeyword:  类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - keywordType:  类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码)

    返回参数:
    - tpQualificationList: 企业税务资质信息 类型：list of dict
    - tpId: 纳税人识别号 类型：string
    - tpName: 纳税人名称 类型：string
    - qualification: 资质全称 类型：string
    - begin: 有效期起 类型：string
    - end: 有效期止 类型：string
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'keywordType': keywordType,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('66a0f66a5646e2b0fc8ae758', params)


@mcp.tool()
def operation_insight_financing_info(matchKeyword: str, keywordType: str = None) -> dict:
    """
    该接口的功能是根据输入的企业标识信息（如企业名称、注册号、统一社会信用代码或企业ID）及主体类型，查询企业的融资信息，包括融资次数、详细的融资记录、融资金额、融资轮次、融资时间和投资方等。该接口可以用于金融机构、投资公司和企业自身的风控系统，以分析目标企业的融资历史和投资方背景，从而辅助在投资决策、企业评级、风险评估以及市场竞争分析等场景下进行精准的判断和规划。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码)

    返回参数:
    - fpFinancingCount: 融资次数 类型：int
    - fpFinancingList: 融资信息 类型：list of dict
    - financingAmount: 融资金额 类型：string
    - financingSeries: 融资轮次 类型：string
    - financingTime: 融资时间 类型：string
    - investorList: 投资方 类型：list of string
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'keywordType': keywordType,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('66a0f56efc5601eba12cc2e3', params)


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
    