# 全局导入
import json
import os
from hashlib import md5
import requests
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import sys

load_dotenv()

mcp = FastMCP("楼宇大数据", instructions="楼宇大数据",dependencies=["python-dotenv", "requests"])

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
def building_bigdata_fuzzy_search(matchKeyword: str, pageIndex: int = 1, pageSize: int = None) -> dict:
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
def building_bigdata_office_address_details(matchKeyword: str, address: str = None, pageIndex: int = 1, keywordType: str = None,
                           pageSize: int = None) -> dict:
    """
    该接口功能及用途是根据特定的企业标识信息，查询和返回企业的办公地址相关数据，包括办公地址总数、每个城市的办公地址详细信息等。该接口的主要使用场景包括企业内部管理系统用于了解办公地址布局、商业分析工具中用于市场地理分布分析，以及政府或合作机构进行企业信息核实或者决策辅助时快速获取企业在各地的实际运营地址信息。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id，如果没有企业全称则先调取fuzzy_search接口获取企业全称。
    - address: 地区 类型：string - 支持筛选省/市，不可多选，省市之间用英文逗号分隔，输入示例："广东省,广州市"
    - pageIndex: 分页开始位置 类型：int
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码）
    - pageSize: 分页结束位置 类型：int - 一页最多获取10条数据

    返回参数:
    - officeAddress: 地址 类型：dict
    - total: 总数 类型：int
    - officeSourceType: 地址来源 类型：string
    - officeSettleType: 入驻方式 类型：string - 工商注册入驻，办公地址入驻
    - resultList: 列表结果 类型：list of dict
    - estateName: 所在楼宇 类型：string
    - estateId: 楼宇id 类型：string
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'address': address,
        'pageIndex': pageIndex,
        'keywordType': keywordType,
        'pageSize': pageSize,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('6786528b1677add9f934358f', params)


@mcp.tool()
def building_bigdata_office_address_stats(matchKeyword: str, keywordType: str = None) -> dict:
    """
    该接口功能及用途是根据特定的企业标识信息，查询和返回企业的办公地址相关数据，包括办公地址城市、每个城市的办公地址数量等。该接口的主要使用场景包括企业内部管理系统用于了解办公地址布局、商业分析工具中用于市场地理分布分析，以及政府或合作机构进行企业信息核实或者决策辅助时快速获取企业在各地的实际运营地址信息。


    请求参数:
    - matchKeyword: 匹配关键词 类型：string - 企业名称/注册号/统一社会信用代码/企业id
    - keywordType: 主体类型 类型：select - 主体类型枚举（name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码）

    返回参数:
    - officeCityStats: 办公地址分布统计 类型：list of dict
    - city: 办公城市 类型：string
    - count: 办公地址数量 类型：int
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'keywordType': keywordType,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('6786528b1677add9f934359d', params)


@mcp.tool()
def building_bigdata_building_query(matchKeyword: str = None, pageIndex: int = 1, address: str = None, pageSize: int = 10,
                   estatePropertyType: str = None) -> dict:
    """
    支持通过楼宇名称、楼宇类型等查询指定地区的全部楼盘信息，包括楼宇名称、楼宇别名、楼宇地址、楼宇类型、楼宇入驻企业数量等


    请求参数:
    - matchKeyword: 查询关键词 类型：string - 查询楼宇名称/楼宇别名包含关键词的楼盘
    - pageIndex: 分页开始位置 类型：int
    - address: 地区 类型：string - 支持筛选省/市，不可多选，省市之间用英文逗号分隔，输入示例："广东省,广州市"
    - pageSize: 分页结束位置 类型：int - 一页最多获取10条数据
    - estatePropertyType: 楼宇类型 类型：select - 楼宇类型枚举（写字楼，产业园，综合体，公寓酒店，展会中心）

    返回参数:
    - total: 总数 类型：int
    - estateName: 楼宇名称 类型：string
    - estateId: 楼宇id 类型：string
    - estateAliasName: 楼宇别名 类型：list of string
    - estateAddress: 楼宇地址 类型：dict
    - estatePropertyType: 楼宇类型 类型：string - 写字楼，产业园，综合体，公寓酒店，展会中心
    - estateEnterpriseCount: 楼宇入驻企业数量 类型：int
    - resultList: 结果列表 类型：list of dict
    """
    # 构建请求参数
    params = {
        'matchKeyword': matchKeyword,
        'pageIndex': pageIndex,
        'address': address,
        'pageSize': pageSize,
        'estatePropertyType': estatePropertyType,
    }

    # 过滤None值
    params = {k: v for k, v in params.items() if v is not None}

    # 调用API
    return call_api('6786528b1677add9f93435db', params)


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
    