# 全局导入
import json
import os
from hashlib import md5
import requests
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import sys

load_dotenv()

mcp = FastMCP("企业风险分析洞察", instructions="企业风险分析洞察",dependencies=["python-dotenv", "requests"])

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
def risk_insight_serious_violations(matchKeyword: str, keywordType: str = None) -> dict:
    """
    该接口的功能是查询某一家企业在政府监管下的严重违法记录，包括严重违法的详细信息和处理状态。可能的使用场景包括：在金融贷款审批中，银行或金融机构使用该接口来判断借款企业的合规风险；在企业尽职调查中，投资者或合作伙伴通过此接口获取目标企业的合规历史；在招聘过程中，人力资源部门考察候选公司的背景和合法性；甚至在市场及监管机构内部用于对企业做出合规监督和处罚决策。这样的查询接口是商业风险管理及合规决策中不可或缺的一环。

    请求参数:
    - matchKeyword:  类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - keywordType:  类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码)

    返回参数:
    - illegalCount: 严重违法数量 类型：int
    - illegalInfoList: 严重违法列表 类型：list of dict
    - createAuthority: 做出决定机关（列入） 类型：string
    - createDate: 列入日期 类型：string
    - createReason: 列入原因 类型：string
    - removeAuthority: 做出决定机关（移除） 类型：string
    - removeDate: 移除日期 类型：string
    - type: 类别 类型：string
    - removeReason: 移除原因 类型：string
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'keywordType': keywordType,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('669fb97b76742e172f2a5193', params)


@mcp.tool()
def risk_insight_fuzzy_search(matchKeyword: str, pageIndex: int = 1, pageSize: int = None) -> dict:
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
def risk_insight_chattel_mortgage(matchKeyword: str, keywordType: str = None) -> dict:
    """
    该接口的功能是查询企业的动产抵押信息，提供有关动产抵押的详细数据，包括抵押的数量、列表信息以及相关主体和债权信息。可能的使用场景包括金融机构在进行信贷审批时评估企业资产负债情况，法律和金融分析师在制作企业信用报告时验证抵押信息，以及企业与合作伙伴在商讨业务合作时提供的资产担保状况核实。通过输入企业的各种标识信息，可以精准获取该企业的动产抵押记录，有助于评估企业的财务稳定性和信用状况。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码)

    返回参数:
    - mortgageCount: 动产抵押数量 类型：int
    - mortgageInfoList: 动产抵押列表 类型：list of dict
        - authority: 登记机关 类型：string
        - mortgageId: 登记编号 类型：dict
        - date: 登记日期 类型：string
        - amount: 被担保债权数额 类型：string
        - publicationDate: 公示日期 类型：string
        - term: 债务人履行债务的期限 类型：string
        - type: 种类 类型：string
        - guaranteedCreditorInfo: 被担保主债券信息 类型：dict
        - mortgageeList: 抵押权人信息 类型：list of dict
        - scope: 担保的范围 类型：string
        - identifacationNo: 证件号码 类型：string
        - identificationType: 证件类型 类型：string
        - address: 抵押权人住所地 类型：string
        - amount: 数额 类型：string
        - name: 抵押权人名称 类型：string
        - owner: 所有权或使用权归属 类型：string
        - name: 抵押物名称 类型：string
        - remark: 备注 类型：string
        - detail: 抵押物详情 类型：string - 数量、质量、状况、所在地等情况
        - pawnList: 抵押物信息 类型：list of dict
        - revokeInfo: 注销信息 类型：dict
        - date: 注销日期 类型：string
        - reason: 注销原因 类型：string
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'keywordType': keywordType,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('66a0e19aa84e3d948a9fc373', params)


@mcp.tool()
def risk_insight_court_hearings(matchKeyword: str, pageIndex: int = 1, pageSize: int = 10, keywordType: str = None) -> dict:
    """
    该接口用于查询与给定企业相关的开庭公告信息，提供详细的庭审和公告细节。这一功能可以帮助法律从业者、企业管理人员或风险控制部门了解特定企业的法律诉讼情况及历史记录。场景包括企业尽职调查、市场竞争分析，以及企业内部风险管理，例如当涉及到企业收购或投资决策时，需要评估目标企业的法律状态与潜在风险。


    请求参数:
    - pageIndex: 页码 类型：int - 从1开始
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - pageSize: 分页大小 类型：int - 一页最多获取50条数据
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码)

    返回参数:
    - total: 总数 类型：int
    - resultList: 列表结果 类型：list of dict
        - address: 庭审地点 类型：string
        - caseReason: 案由 类型：string
        - date: 开庭日期 类型：string
        - publishPage: 公告版面 类型：string
        - publishDate: 公告日期 类型：string
        - publishUnit: 开庭法院 类型：string
        - caseType: 公告类型 类型：string
        - relatedCaseNumber: 案号 类型：string
        - caseId: 开庭公告id 类型：string
        - caseRelatedPerson: 当事人 类型：dict
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
    return call_api('66a0e123bc2d198e864482c4', params)


@mcp.tool()
def risk_insight_litigation_risk_profile(matchKeyword: str, keywordType: str = None) -> dict:
    """
    该接口的功能是查询企业的法律诉讼风险情况，输出包括法院公告、立案公告、开庭公告、裁判文书、被执行人、失信被执行人和限制高消费等信息，帮助用户评估企业的法律风险状况。该接口可能用于信贷风险评估、投资决策支持、企业合规审核、大数据分析中的舆情监测等场景，在这些场合中，获取企业的法律风险信息可以支持更全面的风险评估和决策过程。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码）

    返回参数:
    
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'keywordType': keywordType,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('66bb1aa834d3cd3e43928163', params)


@mcp.tool()
def risk_insight_court_announcements(matchKeyword: str, pageIndex: int = 1, pageSize: int = 10,
                        keywordType: str = None) -> dict:
    """
    该接口的功能是查询特定企业在法院公告中的相关信息，包括庭审地点、当事人、案由等细节，并以列表形式呈现。这一接口主要应用于法律、合规领域内的背景调查中，帮助律师、法务人员或企业合规团队获取目标企业涉及的历史及当前法律诉讼或公告信息，从而评估企业潜在法律风险。这个接口也可能被金融机构在企业信贷评估或风险监控中使用，以查看企业当前或过往是否曾卷入法律纠纷，以及该企业在司法体系中的信用表现。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - pageIndex: 页码 类型：int - 从1开始
    - pageSize: 分页大小 类型：int - 一页最多获取50条数据
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码)

    返回参数:
    - total: 总数 类型：int
    - resultList: 列表结果 类型：list of dict
        - caseType: 公告类型 类型：string
        - date: 开庭日期 类型：string
        - caseRelatedPerson: 当事人 类型：list of dict
        - address: 庭审地点 类型：string
        - publishDate: 公告日期 类型：string
        - publishUnit: 开庭法院 类型：string
        - caseReason: 案由 类型：string
        - relatedCaseNumber: 案号 类型：string
        - publishPage: 公告版面 类型：string
        - caseId: 法院公告id 类型：string
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
    return call_api('669f997d0839b73a327efb4f', params)


@mcp.tool()
def risk_insight_intellectual_property_pledge(matchKeyword: str, keywordType: str = None) -> dict:
    """
    该接口的功能是检索并返回某企业的知识产权出质信息，包括出质数量、相关列表及详细信息，如出质人、质权人、登记期限等。此接口可能用于评估企业的知识产权质权活动，为金融机构在进行企业信用评估和贷款审批时提供支持。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码)

    返回参数:
    - iprPledgeCount: 知识产权出质数量 类型：int
    - iprPledgeList: 知识产权出质列表 类型：list of dict
        - iprName: 知识产权名称 类型：string
        - iprPledgePeriod: 质权登记期限 类型：dict
        - iprPledgePublicDate: 知识产权公示日期 类型：string
        - iprPledgeeName: 知识产权质权人 类型：string
        - iprRegisterNum: 知识产权登记编号 类型：string
        - iprPledgorName: 知识产权出质人 类型：string
        - iprType: 知识产权种类 类型：string
        - iprPledgeRevokeDate: 知识产权注销日期 类型：string
        - iprPledgeRevokeReason: 知识产权注销原因 类型：string
        - iprStatus: 知识产权状态 类型：string
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'keywordType': keywordType,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('66a0e1ca10026dc291e21049', params)


@mcp.tool()
def risk_insight_penalties(matchKeyword: str, keywordType: str = None) -> dict:
    """
    该接口的功能是查询某一企业行政处罚记录，包括处罚的详细信息，如处罚原因、结果、决定机关等。它可以用于企业合规审查、信用评估、合作前调查等场景。例如，企业在招标或融资前对自身或合作方进行法律合规性检查，防范合作风险；金融机构在贷款审核中审查企业信用风险，确保交易安全；政府监管部门进行定期监督检查，促进市场健康发展。通过该接口获取的详细处罚信息，可以帮助判断企业在市场中的信誉和法律合规情况，辅助决策过程。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码）

    返回参数:
    - punishmentCount: 行政处罚数量 类型：int
    - punishmentList: 行政处罚列表 类型：list of dict
        - punishContent: 行政处罚内容 类型：string
        - punishAuthority: 决定机关 类型：string
        - punishDecisionDate: 决定日期 类型：string
        - punishId: 决定书文号 类型：string
        - punishType: 违法行为类型 类型：string
        - punishDate: 公示日期 类型：string
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'keywordType': keywordType
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('66a24a59515324c521d6610d', params)


@mcp.tool()
def risk_insight_business_anomalies(matchKeyword: str, keywordType: str = None) -> dict:
    """
    该接口的功能是查询企业的经营异常信息，包括异常数量及详细列表信息，如决定机关、日期及原因等。该接口可能用于企业信用评估、风险管理、尽职调查等场景，以帮助合作伙伴、投资者或监管机构了解企业的经营状况和信用风险，确保业务合作的安全性和合规性。


    请求参数:
    - matchKeyword:  类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - keywordType:  类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码)

    返回参数:
    - anomalyCount: 经营异常数量 类型：int
    - anomalyList: 经营异常列表 类型：list of dict
        - removeAuthority: 移出决定机关 类型：string
        - createDate: 列入日期 类型：string
        - removeDate: 移出日期 类型：string
        - createReason: 列入经营异常名录原因 类型：string
        - removeReason: 移出经营异常名录原因 类型：string
        - createAuthority: 列入决定机关 类型：string
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'keywordType': keywordType,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('66a248f381d41651f2689d95', params)


@mcp.tool()
def risk_insight_consumption_restrictions(matchKeyword: str, pageIndex: int = 1, keywordType: str = None,
                             pageSize: int = None) -> dict:
    """
    该接口功能是查询特定企业或其负责人是否存在限制高消费的司法记录，输出结果包括立案时间、案号、执行法院等详细信息。此接口适用于律师事务所、金融机构或商业伙伴在进行企业信用评估和风险控制时，用于核查潜在合作对象是否存在限制消费令，这可能影响其信用状况及履行商业合同的能力，从而决定是否进行合作或采取预防性措施。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - pageIndex: 页码 类型：int - 从1开始
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码)
    - pageSize: 分页大小 类型：int - 一页最多获取50条数据

    返回参数:
    - total: 总数 类型：int  
    - resultList: 列表结果 类型：list of dict
        - efCaseCreateTime: 立案时间 类型：string
        - efCaseNumber: 案号 类型：string
        - efLimitedApplicant: 申请人 类型：list of string
        - efExecutiveCourt: 执行法院 类型：string
        - efLimitedPersonCasePublishTime: 发布日期 类型：string
        - efLimitedPersonName: 限制消费人员 类型：string
        - efLimitedPersonProvince: 省份 类型：string
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
    return call_api('669e3087d6e30dd7e6d03e55', params)


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
    