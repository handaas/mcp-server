# 全局导入
import json
import os
from hashlib import md5
import requests
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import sys

load_dotenv()

mcp = FastMCP("店铺大数据", instructions="店铺大数据",dependencies=["python-dotenv", "requests"])

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
def store_bigdata_company_restaurant_branches(matchKeyword: str, keywordType: str = None) -> dict:
    """
    该接口的功能是根据输入的企业信息（如企业名称、注册号、统一社会信用代码或企业id）查询并返回该企业旗下餐饮品牌门店的详细信息，包括总数、品牌类别、城市和省份的门店分布等。此接口可能用于企业内部管理、商业合作对接、市场调研及分析等场景，帮助相关人员获取某一企业在餐饮行业的市场布局和品牌影响力。通过分析返回的数据，企业可以优化资源配置、制定市场策略，并评估品牌覆盖的地域广度和门店分布情况。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码）

    返回参数:
    - storeTotal: 总数 类型：int
    - storeList: 数据列表 类型：list of dict
    - brandClassification: 品牌类别 类型：dict
    - brandId: 品牌id 类型：string
    - firstClassify: 一级类别 类型：string
    - secondClassify: 二级类别 类型：string
    - brandCradle: 起源地 类型：string
    - brandImage: 品牌图片 类型：string
    - brandName: 品牌名称 类型：string
    - mallStoreNum: 商场店数 类型：int
    - brandStoreCityStats: 城市分布 类型：list of dict - 只返回前十条数据
    - count: 门店数量 类型：int
    - brandStoreProvinceStats: 省份分布 类型：list of dict - 只返回前十条数据
    - brandStoreNum: 门店数 类型：int
    - count: 门店数量 类型：int
    - province: 省份 类型：string
    - city: 城市 类型：string
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'keywordType': keywordType,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('66f3d8bf64bd2be52d68a0e9', params)


@mcp.tool()
def store_bigdata_fuzzy_search(matchKeyword: str, pageIndex: int = 1, pageSize: int = None) -> dict:
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
def store_bigdata_offline_store_search(ooStoreName: str = None, ooStoreBrandList: str = None, ooStoreCalClassification: str = None,
                         address: str = None, ooStoreStatus: str = None, ooStoreAddressValue: str = None,
                         hasMobile: str = None, hasPhone: int = None, pageSize: int = 10,
                         ooMinStorePerCapitaConsumption: float = None, ooMaxStorePerCapitaConsumption: float = None,
                         pageIndex: int = None) -> dict:
    """
    该接口的功能是提供线下店铺的搜索功能，通过输入店铺名称、类目、消费区间、店铺状态、地理位置等条件，返回符合条件的店铺信息列表，包括店铺的详细信息和联系方式。此接口可以用于帮助用户便捷地找到符合其需求的线下店铺，例如在本地服务类应用中帮助消费者搜索到达便利的店铺，或可供商家进行市场分析和潜在客户定位。通过结合人均消费、店铺状态、地理区域等多种条件进行筛选，有助于精确匹配用户需求。


    请求参数:
    - ooStoreName: 店铺名称 类型：string - 店铺名称
    - ooStoreBrandList: 经营品牌 类型：string - 支持多选，英文分号分割。
    - ooStoreCalClassification: 店铺分类 类型：string - 支持多选，一级类目和二级类目采用英文逗号分隔，多选采用英文分号分隔，格式示例："汽车服务,汽车俱乐部;汽车服务,汽车维修"
    - address: 地区 类型：string - 不可多选，英文逗号分割，参考点评划分区域，举例："广东省,广州市,天河公园"
    - ooStoreStatus: 店铺状态 类型：select - 店铺状态枚举（营业，尚未营业，暂停营业，歇业/关闭，关闭/下架），默认全部
    - ooStoreAddressValue: 店铺地址 类型：string - 店铺地址
    - hasMobile: 有无手机号 类型：string - 1：有，0：无
    - hasPhone: 有无手机号 类型：int - 1：有，0：无
    - pageSize: 分页大小 类型：int - 一页最多获取50条数据
    - ooMinStorePerCapitaConsumption: 人均消费最小值 类型：float - 人均消费最小值
    - ooMaxStorePerCapitaConsumption: 人均消费最大值 类型：float - 人均消费最大值
    - pageIndex: 页码 类型：int - 从1开始

    返回参数:
    - resultList: 结果列表 类型：list of dict
    - total: 总数 类型：int
    - ooStoreId: 店铺id 类型：string
    - hasContact: 有无联系方式 类型：int - 1：有，0：无
    - contactNumber: 联系方式数量 类型：int
    - hasMobile: 有无手机号 类型：int - 1：有，0：无
    - hasPhone: 有无固话 类型：int - 1：有，0：无
    - ooStoreCalClassification: 店铺分类 类型：dict
    - ooStoreName: 店铺名称 类型：string
    - ooStorePerCapitaConsumption: 人均价格 类型：float
    - ooStoreRank: 店铺排名 类型：int
    - ooStoreStatus: 店铺状态 类型：string
    - ooStoreTradingArea: 店铺所在商圈 类型：string
    """
    # 构建请求参数
    params = {
        'ooStoreName': ooStoreName,
        'ooStoreBrandList': ooStoreBrandList,
        'ooStoreCalClassification': ooStoreCalClassification,
        'address': address,
        'ooStoreStatus': ooStoreStatus,
        'ooStoreAddressValue': ooStoreAddressValue,
        'hasMobile': hasMobile,
        'hasPhone': hasPhone,
        'pageSize': pageSize,
        'ooMinStorePerCapitaConsumption': ooMinStorePerCapitaConsumption,
        'ooMaxStorePerCapitaConsumption': ooMaxStorePerCapitaConsumption,
        'pageIndex': pageIndex,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('66ed53be15858a879f40242f', params)


@mcp.tool()
def store_bigdata_restaurant_branch_stats(matchKeyword: str, pageIndex: int = 1, pageSize: int = None) -> dict:
    """
    该接口的功能是根据品牌ID获取特定餐饮品牌在各城市及省份的门店分布情况，包括各城市和省份的门店数量统计。此接口可以用于企业内部业务分析，帮助企业了解其门店在不同地域的分布，从而优化资源分配和市场策略。


    请求参数:
    - matchKeyword: 品牌id 类型：string - 品牌id，字段来源企业旗下餐饮品牌门店
    - pageIndex: 页码 类型：int - 从1开始
    - pageSize: 分页大小 类型：int - 一页最多获取50条数据

    返回参数:
    - count: 门店数量 类型：int
    - city: 城市 类型：string
    - provinceStatsList: 省份分布列表 类型：list of dict - 返回全部数据
    - cityStatsTotal: 城市分布数量 类型：int
    - cityStatsList: 城市分布列表 类型：list of dict
    - province: 省份 类型：string
    - count: 门店数量 类型：int
    - provinceStatsTotal: 省份分布数量 类型：int
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
    return call_api('66f3d8c064bd2be52d68a159', params)

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
    