# 全局导入
import json
import os
from hashlib import md5
import requests
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import sys

load_dotenv()

mcp = FastMCP("展会大数据", instructions="展会大数据",dependencies=["python-dotenv", "requests"])

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
def exhibition_bigdata_exhibition_participation(matchKeyword: str, pageIndex: int = 1, pageSize: int = 10,
                             keywordType: str = None) -> dict:
    """
    该接口用于查询企业在展会中的参展信息，通过输入企业的标识信息（如企业名称或统一社会信用代码），返回该企业参加展会的详细信息，包括展会的时间、描述、名称及展馆等。此接口在以下场景可能被广泛使用：展会管理平台用于管理和查询企业参与的历史和即将举办的展会信息，以帮助企业跟踪参展活动和计划未来的参展策略；展会数据分析公司用于收集企业参展数据进行大数据分析，以给予客户战略决策支持；商业情报公司利用该信息了解企业动态和市场趋势。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - pageIndex: 页码 类型：int 从1开始
    - pageSize: 分页大小 类型：int - 一页最多获取50条数据
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码)

    返回参数:
    - total: 总数 类型：int
    - resultList: 列表结果 类型：list of dict
    - fairEndTime: 闭展时间 类型：string
    - fairLogo: 展会logo 类型：string
    - fairDesc: 展会描述 类型：string
    - fairPavilion: 展馆名称 类型：string
    - fairName: 展会名称 类型：string
    - isOpen: 是否开展 类型：int
    - fairBeginTime: 开展时间 类型：string
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
    return call_api('66a26918ff3066996ecc6471', params)


@mcp.tool()
def exhibition_bigdata_fuzzy_search(matchKeyword: str, pageIndex: int = 1) -> dict:
    """
    该接口的功能是根据提供的企业名称、人名、品牌、产品、岗位等关键词模糊查询相关企业列表。返回匹配的企业列表及其详细信息，用于查找和识别特定的企业信息。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 查询各类信息包含匹配关键词的企业
    - pageIndex: 分页开始位置 类型：int 从1开始

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
        'pageIndex': pageIndex
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('675cea1f0e009a9ea37edaa1', params)


@mcp.tool()
def exhibition_bigdata_exhibition_venue_search(pavilionRegion: str, matchKeyword: str = None, pageIndex: int = 1) -> dict:
    """
    该接口的功能是提供展会会馆的搜索服务，根据用户输入的关键词以及会馆所在地区，返回符合条件的会馆列表及相关详细信息，如会馆简介、展会数量和联系方式等。接口的常见使用场景包括会展组织者寻找合适的展会场所、展会参与者获取会场信息以及商务人士计划展会行程时查询场地等，这可以帮助用户便捷地筛选合适的会馆，提升信息获取的效率。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 会馆名称/会馆简介包含关键词的会馆
    - pavilionRegion: 会馆所在地区 类型：string - 会馆所在省份城市，不可多选，如果是直辖市则只输入直辖市名称比如北京市则传入北京，示例：福建省,厦门市
    - pageIndex: 页码 类型：int - 从1开始

    返回参数:
    - total: 总数 类型：int
    - resultList: 结果列表 类型：list of dict
    - pavilionContact: 联系方式 类型：list of dict - contactType联系方式类型枚举（1：固定电话，2：邮箱，5：传真）
    - pavilionDesc: 会馆简介 类型：string
    - fairCount: 展会数 类型：int
    - pavilionAddress: 会展地址 类型：string
    - _id: 会馆id 类型：string
    - pavilionHomepage: 会馆官网链接 类型：string
    - pavilionLogo: 会馆logo 类型：string
    - pavilionName: 会馆名称 类型：string
    - pavilionScale: 展览面积 类型：string
    """
    # 构建请求参数
    if pavilionRegion == "北京市" or pavilionRegion == "上海市" or pavilionRegion == "天津市" or pavilionRegion == "重庆市":
        pavilionRegion = pavilionRegion.replace("市", "")
        
    params = {
        'matchKeyword': matchKeyword,
        'pavilionRegion': pavilionRegion,
        'pageIndex': pageIndex
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('66e2d2ca428a1f4cd69c1083', params)


@mcp.tool()
def exhibition_bigdata_exhibition_search(matchKeyword: str = None, pageIndex: int = 1) -> dict:
    """
    该接口提供了根据用户输入的查询关键词搜索展会信息的功能，返回与关键词匹配的展会列表，包括展会的详细信息，如名称、时间、地点和描述等。此接口的使用场景广泛，可以应用于展会信息聚合平台、第三方搜索引擎、企业或个人寻找特定展会的信息，或用于推荐与用户兴趣相关的展会，为用户提供便捷的展会搜索服务。


    请求参数:
    - matchKeyword: 搜索关键词 类型：string - 搜索展会名称/展品范围包含关键词的展会
    - pageIndex: 页码 类型：int 从1开始

    返回参数:
    - resultList: 列表结果 类型：list of dict
    - _id: 展会id 类型：string
    - fairName: 展会名称 类型：string
    - fairLogo: 展会Logo 类型：string
    - fairEndTime: 闭展时间 类型：string
    - fairBeginTime: 开展时间 类型：string
    - total: 总数 类型：int
    - fairDesc: 展会描述 类型：string
    - fairPavilion: 展馆地址 类型：string
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'pageIndex': pageIndex
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('66a0f6ca477cbe5f7605973f', params)


@mcp.tool()
def exhibition_bigdata_exhibitor_search(fairRegion: str = None, matchKeyword: str = None, fairIndustries: str = None,
                     fairBeginTimes: str = None, fairEndTimes: str = None, pageIndex: int = 1, fairCount: str = None) -> dict:
    """
    该接口的功能是支持根据输入条件搜索特定参展商的信息，包括企业名关键词、所在地区、展会专题及参展记录范围，返回符合条件的参展商的详细信息，如企业状态、规模、地址、行业等。此接口的使用场景包括展会组织者筛选潜在参展商、市场分析人员进行行业研究、销售人员寻找特定地区或行业的合作企业等，通过细化的搜索条件，可以快速获得目标企业的信息，从而更好地进行商业决策和合作规划。


    请求参数:
    - fairRegion: 省市地区 类型：string - 展商所在省份/城市，不可多选，示例："福建省,厦门市"
    - matchKeyword: 搜索关键词 类型：string - 搜索企业名关键词
    - fairIndustries: 展会行业 类型：string - 展会专题枚举具体见下表，不可多选，示例："教育/职业培训/商业"
    - fairBeginTimes: 参展开始时间 类型：string - 格式："yyyy-mm-dd"
    - fairEndTimes: 参展结束时间 类型：string - 格式："yyyy-mm-dd"
    - pageIndex: 分页开始位置 类型：int
    - fairCount: 参展记录 类型：select - 参展记录枚举（5场以下、5-10场、10-20场、20-50场、50-100场、100场以上）

    返回参数:
    - total: 总数 类型：int
    - resultList: 结果列表 类型：list of dict
    - enterpriseInfo: 企业信息 类型：list of dict
    - operStatus: 企业状态 类型：string
    - enterpriseScale: 公司规模 类型：string
    - foundTime: 成立时间 类型：string
    - address: 企业地址 类型：dict
    - regCapital: 企业注册资本 类型：dict
    - name: 企业名称 类型：string
    - legalRepresentative: 法人代表 类型：string
    - entityType: 主体类型 类型：string
    - industry: 行业 类型：dict
    - fairCount: 参展记录 类型：int
    - latestFair: 最新参展信息 类型：list of dict
    - fairBeginTime: 展会开始时间 类型：string
    - fairExhibitsRange: 展会类型 类型：string
    - fairName: 展会名称 类型：string
    - latestFairBeginTime: 最新参展时间 类型：string
    - fairId: 展会id 类型：string
    - nameId: 企业id 类型：string
    - fairIndustries: 展会专题 类型：list of string
    """
    # 构建请求参数
    params = {
        'fairRegion': fairRegion,
        'matchKeyword': matchKeyword,
        'fairIndustries': fairIndustries,
        'fairBeginTimes': fairBeginTimes,
        'fairEndTimes': fairEndTimes,
        'pageIndex': pageIndex,
        'fairCount': fairCount
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('66d5b7e0537c3f61d646c473', params)


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
    