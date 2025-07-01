# 全局导入
import json
import os
from hashlib import md5
import requests
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import sys

load_dotenv()

mcp = FastMCP("政策大数据", instructions="政策大数据",dependencies=["python-dotenv", "requests"])

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
def policy_bigdata_approved_project_stats(matchKeyword: str, keywordType: str = None) -> dict:
    """
    该接口用于查询企业所获批项目的统计信息，通过输入企业的基本标识信息和主体类型枚举，返回该企业在不同级别（国家、省、市、区）的申报项目数量、项目级别分布、归口主管机构信息，以及近年项目获批趋势和补贴金额变化趋势。这一接口在企业评估项目申报成果、进行项目管理决策、以及政府部门对企业扶持情况的监控分析中可能被广泛使用。特别对于需要进行企业竞标分析、关键项目投资效益评估以及政府项目资助成效考核的场景，该接口提供了可靠的数据支持。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码）

    返回参数:
    - count: 项目数量 类型：int
    - agency: 主管机构 类型：string
    - ppeLevelStat: 项目级别分布 类型：dict
    - nationalProjectCount: 国家级项目数量 类型：int
    - provincialProjectCount: 省级项目数量 类型：int
    - municipalProjectCount: 市级项目数量 类型：int
    - ppeAgencyStat: 项目归口分布 类型：list of dict
    - ppeYearAmountStat: 补贴金额趋势 类型：list of dict
    - year: 年份 类型：int
    - districtProjectCount: 区级项目数量 类型：int
    - ppeYearProjectStat: 获批项目趋势 类型：list of dict
    - amount: 补贴金额 类型：float
    - count: 项目数量 类型：int
    - year: 年份 类型：int
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'keywordType': keywordType,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('66c702b725f04ab44cd24c9c', params)


@mcp.tool()
def policy_bigdata_fuzzy_search(matchKeyword: str, pageIndex: int = 1, pageSize: int = None) -> dict:
    """
    该接口的功能是根据提供的产品名称关键词，查询并返回与之相关的企业详细信息，包括企业基本资料及相关营业数据。可以进行综合检索。


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
def policy_bigdata_policy_info(matchKeyword: str) -> dict:
    """
    该接口的功能是根据政策id查询并返回特定政策的详细信息，包括其发布机构、内容、相关项目、资助金额、及申报时间等。这一接口可以用于政策管理系统、企业或学术研究者的政策检索功能，帮助用户快速获取特定政策的详细信息以进行分析或决策。


    请求参数:
    - matchKeyword: 政策id 类型：string - 政策id

    返回参数:
    - pnFileList: 附件 类型：list of dict
    - pnAgency: 发布机构 类型：string
    - filename: 文件名称 类型：string
    - url: 文件链接 类型：string
    - pnOriginUrl: 政策原文链接 类型：string
    - pnPublishDate: 发布时间 类型：string
    - pnTitle: 政策标题 类型：string
    - pnType: 政策类型 类型：string
    - relatedProjects: 可能关联项目 类型：list of dict
    - agency: 主管机构 类型：string
    - maxGrantMount: 资助金额 类型：int - 单位：元
    - declaredLevel: 项目级别 类型：int - 1：国家级，2：省级，3：市级，4：区级
    - pnRegion: 发布地区 类型：dict
    - pnText: 政策正文 类型：string
    - name: 项目名称 类型：string
    - projectProgress: 项目进展 类型：int - 1：未开始，2：申报中，3：申报结束，4：已公示，5：已公开
    - declaredStartTime: 申报开始时间 类型：string
    - region: 地区 类型：dict
    - declaredEndTime: 申报结束时间 类型：string
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('66c702b725f04ab44cd24cd6', params)


@mcp.tool()
def policy_bigdata_policy_search(matchKeyword: str, pnType: str = None, agency: str = None, address: str = None,
                  policyPubStartTime: str = None, policyPubEndTime: str = None, pageSize: int = 10,
                  pageIndex: int = None) -> dict:
    """
    该接口旨在根据用户提供的关键词、政策类型和地区信息，检索出符合条件的政策法规、申报指南或公示公告，输出包括相关政策的详细信息。此接口在企业或个人需要查找和获取与自身相关的政府政策信息时尤为有用，常见应用场景包括企业申请科技项目或补助资金时，快速定位相关政策指南；公众查询公示公告以获取最新的政府动态；以及咨询公司为客户制作政策合规报告时，提供当前适用的法规政策背景支持。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 政策法规/申报指南/公示公告关键词
    - pnType: 政策类型 类型：select - 政策类型枚举（全部，申报指南，公示公开，其他政策）
    - agency: 发布机构 类型：string
    - address: 地区 类型：string - 多选，支持省份/城市/区县，输入格式举例：[["福建省"],["贵州省","安顺市","平坝县"]]，查询国家发布政策则输入：[["国家部委"]]
    - policyPubStartTime: 发布开始日期 类型：string
    - policyPubEndTime: 发布结束日期 类型：string
    - pageSize: 分页大小 类型：int - 一页最多获取50条数据
    - pageIndex: 页码 类型：int - 从1开始

    返回参数:
    - total: 总数 类型：int
    - resultList: 结果列表 类型：list of dict
    - pnId: 政策id 类型：string
    - pnRegion: 发布地区 类型：dict
    - pnText: 政策内容 类型：string
    - pnTitle: 政策标题 类型：string
    - pnPublishDate: 发布时间 类型：string
    - pnType: 政策类型 类型：string
    - pnAgency: 发布机构 类型：string
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'pnType': pnType,
        'agency': agency,
        'address': address,
        'policyPubStartTime': policyPubStartTime,
        'policyPubEndTime': policyPubEndTime,
        'pageSize': pageSize,
        'pageIndex': pageIndex,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('66c702b725f04ab44cd24ceb', params)


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
    