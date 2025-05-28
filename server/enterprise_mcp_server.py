import json
import os
from hashlib import md5
import requests
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
# 加载环境变量
load_dotenv()

description = """
该MCP服务, 提供HANDAAS企业大数据服务, 包括企业工商信息、企业简介、企业标签、企业业务、企业控股股东信息、企业对外投资信息、企业分支机构信息、企业主要人员信息等。在调用需要企业全称的接口时，需要先调用关键词模糊查询企业接口进行补全后，再调用该接口。
"""
# 创建MCP服务器（增加依赖说明）
mcp = FastMCP("HANDAAS企业大数据服务", instructions=description,dependencies=["python-dotenv", "requests"])

INTEGRATOR_ID = os.environ.get("INTEGRATOR_ID")
SECRET_ID = os.environ.get("SECRET_ID")
SECRET_KEY = os.environ.get("SECRET_KEY")
MCP_HOST = os.environ.get("MCP_HOST", "127.0.0.1")
MCP_PORT = os.environ.get("MCP_PORT", 8000)


def call_api(product_id: str, params: dict) -> dict:
    """
    调用API接口
    
    参数:
      - product_id: 数据产品ID
      - params: 接口参数
      - integrator_id: 对接器ID(可选)
    """
    if not params:
        params = {}
    
    if not INTEGRATOR_ID:
        return {"error": "对接器ID不能为空"}
    
    call_params = {
        'product_id': product_id,
        'secret_id': SECRET_ID,
        'params': json.dumps(params, ensure_ascii=False)
    }
    
    # 签名生成
    keys = sorted(list(call_params.keys()))
    params_str = ''
    for key in keys:
        params_str += str(call_params[key])
    params_str += SECRET_KEY
    sign = md5(params_str.encode('utf-8')).hexdigest()
    
    call_params["signature"] = sign
    
    # 调用API
    url = f'https://console.handaas.com/api/v1/integrator/call_api/{INTEGRATOR_ID}'
    try:
        response = requests.post(url, data=call_params)
        return response.json().get("data", "查询为空")
    except Exception as e:
        return "查询失败"

@mcp.tool()
def get_keyword_search(matchKeyword: str, pageIndex: int = None, pageSize: int = None) -> dict:
    """
    关键词模糊查询企业
    该接口的功能是根据提供的企业名称、人名、品牌、产品、岗位等关键词模糊查询相关企业列表。返回匹配的企业列表及其详细信息，用于查找和识别特定的企业信息。
        
    参数:
        - matchKeyword: 匹配关键词 - 查询各类信息包含匹配关键词的企业
        - pageIndex: 分页开始位置
        - pageSize: 分页结束位置 - 一页最多获取50条数据
    返回值:
        - catchReason: 命中原因
        - address: 地址
        - enterpriseType: 企业类型
        - foundTime: 成立时间
        - homepage: 官网
        - legalRepresentative: 法人
        - name: 企业名称
        - operStatus: 经营状态
        - regCapitalCoinType: 注册资本币种
        - regCapitalValue: 注册资本
        - annualTurnover: 年营业额
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
def get_enterprise_base_info(keyword: str) -> dict:
    """
    该接口通过输入企业全称查询企业业务相关信息，识别该公司是做什么的。如果没有全称则需要先调用关键词模糊查询企业接口进行补全后，再调用该接口。返回企业工商信息、企业简介、企业标签、企业业务。
    
    参数:
      - keyword: 企业全称   
    返回值:
      - base_info: 企业工商信息
      - desc: 企业简介
      - business_info: 企业业务
      - tag: 企业标签
    """
    try:
        # 调用模糊搜索接口
        enterprise_base_info = call_api("66dbccbec7a7e3460f5e613f", {"matchKeyword": keyword})
        enterprise_desc = call_api("6682b0b370f56cb7d77701e0", {"matchKeyword": keyword})
        enterprise_business_info = call_api("66e55613ae988a28c6db9259", {"matchKeyword": keyword})
        enterprise_tag = call_api("669e531ce1fd7bff82321d8d", {"matchKeyword": keyword})
        
        return {
            "base_info": enterprise_base_info,
            "desc": enterprise_desc,
            "business_info": enterprise_business_info,
            "tag": enterprise_tag
        }
    except Exception as e:
        return "查询失败"



@mcp.tool()
def get_enterprise_holder_info(keyword: str) -> dict:
    """
    该接口通过输入企业全称查询企业控股股东信息。如果没有全称则需要先调用关键词模糊查询企业接口进行补全后，再调用该接口。该信息通过工商信息及旷湖全部数据分析得出。
    
    参数:
      - keyword: 企业全称
    返回值:
      - holderList: 股东列表（工商公示）
        - entityType: 主体类型
        - holderType: 股东类型
        - name: 股东名称
        - nameId: 企业id
        - humanId: 人员id
        - payAmount: 实缴金额
        - ratio: 持股比例
        - subscriptionDetail: 认缴信息
      - stockHolderList：股东列表（最新公示）来自于上市信息
    """
    try:
        # 调用模糊搜索接口
        holder_info = call_api("66b485eadaf8c77fb249a441", {"matchKeyword": keyword})        
        return holder_info
    except Exception as e:
        return "查询失败"


@mcp.tool()
def get_enterprise_invest_info(keyword: str) -> dict:
    """
    该接口通过输入企业全称查询企业的对外投资信息。如果没有全称则需要先调用关键词模糊查询企业接口进行补全后，再调用该接口。该信息通过工商信息及旷湖全部数据分析得出。
    
    参数:
      - keyword: 企业全称
      
    返回值:
      - resultList: 对外投资结果列表
        - addressValue: 被投资公司所属地区
        - business: 被投资公司经营范围
        - foundTime: 被投资公司成立日期
        - isListed: 被投资公司上市状态
        - legalRepresentative: 被投资公司法定代表人
        - name: 对外投资企业名
        - operStatus: 对外投资企业经营状态
        - ratio: 占股比例
        - regCapital: 被投资公司注册资本
        - scCode: 对外投资企业统一信用编码
        - subscriptionAmount: 投资金额信息
    """
    try:
        # 调用模糊搜索接口
        invest_info = call_api("669e5ee54efb02e6f96c7c9c", {"matchKeyword": keyword})        
        return invest_info
    except Exception as e:
        return "查询失败"


@mcp.tool()
def get_enterprise_branch_info(keyword: str) -> dict:
    """
    该接口通过输入企业全称查询企业的分支机构信息，分支机构信息来源于工商公示。如果没有全称则需要先调用关键词模糊查询企业接口进行补全后，再调用该接口。
    
    参数:
      - keyword: 企业全称

    返回值:
      - resultList: 对外投资结果列表
        - addressValue: 地址信息
        - foundTime: 成立时间
        - legalRepresentative: 法定代表人
        - name: 机构名称
        - operStatus: 经营状态
        - orgCode: 组织机构代码
        - registrationAuthority: 登记机关
        - socialCreditCode: 统一社会信用代码
    """
    try:
        # 调用模糊搜索接口
        branch_info = call_api("669fa757c629692bdb8d80b7", {"matchKeyword": keyword})        
        return branch_info
    except Exception as e:
        return "查询失败"


@mcp.tool()
def get_enterprise_main_person_info(keyword: str) -> dict:
    """
    该接口通过输入企业全称查询企业的主要人员信息，主要人员信息来源于工商公示。如果没有全称则需要先调用关键词模糊查询企业接口进行补全后，再调用该接口。
    
    参数:
      - keyword: 企业全称

    返回值:
      - resultList: 对外投资结果列表
        - name: 成员名称
        - position: 职位
        - ratio: 持股比例
        - relatedEnterpriseCurrentNum: 现任职企业数
        - relatedEnterpriseHistoryNum: 曾任职企业数
    """
    try:
        # 调用模糊搜索接口
        main_person_info = call_api("669fa60021b2cee211ad3ef2", {"matchKeyword": keyword})        
        return main_person_info
    except Exception as e:
        return "查询失败"
    
    
# 运行服务器
if __name__ == "__main__":
    print(f"正在启动HandaaS API MCP服务器...")
    mcp.settings.port = MCP_PORT
    mcp.settings.host = MCP_HOST
    # 运行服务器
    mcp.run(transport="streamable-http")
