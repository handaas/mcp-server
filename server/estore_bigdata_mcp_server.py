"""
自动生成的HandaaS API MCP工具方法
生成时间: 2025-05-30 15:53:56
此文件由generate_mcp_tools.py自动生成，请勿手动修改
"""

# 全局导入
import json
from typing import Dict, List, Optional, Any, Union
import os
from hashlib import md5
import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("网店大数据", instructions="网店大数据",dependencies=["python-dotenv", "requests"])

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
def global_online_store_profile(matchKeyword: str, keywordType: str = None) -> dict:
    """
    该接口的功能是提供企业在国内外的网店概况信息，通过输入企业的相关标识信息查询，输出企业网店的数量、商品总量、销售平台、主营品牌和产品、以及店铺来源等详细信息。此接口可用于市场调研公司、投资机构、竞争分析团队或电商平台运营者，用于分析企业在电子商务领域的市场影响力、市场覆盖率和商品销售布局，帮助制定市场策略或进行投资决策。
    
    
    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码）
    
    返回参数:
    - domesticEshopCount: 国内网店数量 类型：int
    - domesticEshopProductCount: 国内网店商品总量 类型：int
    - domesticEshopBrandList: 国内网店主营品牌 类型：list of string
    - domesticEshopPlatformList: 国内网店上架平台 类型：list of string
    - domesticEshopProductList: 国内网店主营产品 类型：list of string
    - domesticEshopSourceList: 国内网店来源 类型：list of string
    - foreignEshopPlatformList: 国外网店上架平台 类型：list of string
    - foreignEshopProductList: 国外网店主营产品 类型：list of string
    - foreignEshopBrandList: 国外网店主营品牌 类型：list of string
    - foreignEshopCount: 国外网店数量 类型：int
    - foreignEshopSourceList: 国外网店来源 类型：list of string
    - foreignEshopProductCount: 国外网店商品总量 类型：int
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'keywordType': keywordType,
    }
    
    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}
    
    # 调用API
    return call_api('66d5b7df537c3f61d646c327', params)

@mcp.tool()
def ecommerce_product_profile(matchKeyword: str, keywordType: str = None) -> dict:
    """
    该接口的功能是根据企业的关键识别信息（如企业名称、注册号等）查询其在电商平台上的店铺及商品概况，包括品牌信息、评分、创建时间等详细信息。此接口可用于市场调研、竞争分析或投资评估等场景，帮助企业或投资者了解特定企业的电商运营状况及市场表现，例如在选择合作品牌或评估市场机会时，获取目标企业的电商表现数据等。
    
    
    请求参数:
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码）
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    
    返回参数:
    - ecShopAvgRates: 店铺平均评分 类型：float - 单位：分
    - ecShopEarliestFoundTime: 店铺创建时间 类型：string
    - ecShopItemCategories: 产品分类 类型：list of string
    - ecShopBrands: 主营品牌 类型：list of string
    - ecShopNumber: 店铺个数 类型：int - 单位：个
    - ecShopItemCount: 店铺商品总数 类型：int - 单位：个
    - ecShopProducts: 主营产品 类型：list of string
    - ecSources: 上架平台 类型：list of string
    """
    # 构建请求参数
    params = {
        'keywordType': keywordType,
        'matchKeyword': matchKeyword,
    }
    
    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}
    
    # 调用API
    return call_api('66c33eff3c0917a9a02feba8', params)

@mcp.tool()
def fuzzy_search(matchKeyword: str, pageIndex: int = None, pageSize: int = None) -> dict:
    """
    该接口的功能是根据提供的企业名称、人名、品牌、产品、岗位等关键词模糊查询相关企业列表。返回匹配的企业列表及其详细信息，用于查找和识别特定的企业信息。
    
    
    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 查询各类信息包含匹配关键词的企业
    - pageIndex: 分页开始位置 类型：int
    - pageSize: 分页结束位置 类型：int - 一页最多获取50条数据
    
    返回参数:
    - total: 总数 类型：int
    - resultList: 结果列表 类型：list of dict
    - annualTurnover: 年营业额 类型：string
    - formerNames: 曾用名 类型：list of string
    - catchReason: 命中原因 类型：dict
    - address: 注册地址 类型：string
    - holderList: 股东 类型：list of string
    - address: 地址 类型：list of string
    - name: 企业名称 类型：list of string
    - goodsNameList: 产品名称 类型：list of string
    - operBrandList: 品牌 类型：list of string
    - mobileList: 手机 类型：list of string
    - phoneList: 固话 类型：list of string
    - recruitingName: 招聘岗位 类型：list of string
    - emailList: 邮箱 类型：list of string
    - patentNameList: 专利 类型：list of string
    - certNameList: 资质证书 类型：list of string
    - socialCreditCode: 统一社会信用代码 类型：list of string
    - foundTime: 成立时间 类型：string
    - enterpriseType: 企业主体类型 类型：string
    - legalRepresentative: 法定代表人 类型：string
    - homepage: 企业官网 类型：string
    - legalRepresentativeId: 法定代表人id 类型：string
    - prmtKeys: 推广关键词 类型：list of string
    - operStatus: 企业状态 类型：string
    - logo: 企业logo 类型：string
    - nameId: 企业id 类型：string
    - regCapitalCoinType: 注册资本币种 类型：string
    - regCapitalValue: 注册资本金额 类型：int
    - name: 企业名称 类型：string
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
def ecommerce_store_info(matchKeyword: str, keywordType: str = None) -> dict:
    """
    该接口的功能是通过输入特定的企业标识信息（如企业名称、注册号等）来查询与该企业相关联的网店信息，并返回网店的详细信息和业务数据概览。这个接口可以用于电商平台的运营管理、数据分析和竞争对手研究等场景。例如，市场调研人员可以使用该接口获取竞争对手的网店运营状况和产品信息，从而帮助企业进行市场定位和战略调整；或者，通过该接口，监管部门可以监控企业的电商经营活动，确保合规运营。
    
    
    请求参数:
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码)
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    
    返回参数:
    - eshopList: 关联网店列表 类型：list of dict
    - address: 网店位置 类型：dict
    - businessStatistics: 经营状况 类型：dict
    - enterpriseName: 所属企业 类型：string
    - eshopIconLink: 网店logo 类型：string
    - eshopName: 网店名称 类型：string
    - eshopProducts: 主营类目 类型：list of string
    - eshopFoundTime: 开店时间 类型：string
    - eshopKeeper: 掌柜名称 类型：string
    - eshopListCount: 关联网店总数 类型：int
    - overview: 网店数据概览 类型：dict
    - enterpriseEshopBrands: 主营品牌 类型：list of string
    - eshopUrl: 网店url 类型：string
    - isExpired: 网店是否过期 类型：int
    - enterpriseEshopCount: 网店数量 类型：int
    - enterpriseName: 所属企业 类型：string
    - enterpriseEshopProducts: 主营产品 类型：list of string
    - enterpriseEshopPlatforms: 网店上架平台 类型：list of string
    - enterpriseEshopProductsCount: 网店商品总量 类型：int
    """
    # 构建请求参数
    params = {
        'keywordType': keywordType,
        'matchKeyword': matchKeyword,
    }
    
    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}
    
    # 调用API
    return call_api('66a34ccedbee527b7a831c98', params)


if __name__ == "__main__":
    print("正在启动estore_bigdata MCP服务器...")
    # streamable-http方式运行服务器
    # mcp.run(transport="streamable-http")

    # stdio方式运行服务器
    mcp.run(transport="stdio")