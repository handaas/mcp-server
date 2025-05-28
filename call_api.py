import json
import functools
import contextvars
from hashlib import md5
from typing import Callable, Any, Optional, Dict

import requests


def auth_required(product_id: str = None, use_authorization: bool = True):
    """
    鉴权装饰器 - 统一处理API调用的鉴权操作
    
    Args:
        product_id: 数据产品ID，如果不提供则从被装饰函数的参数中获取
        use_authorization: 是否使用Authorization头进行鉴权
    
    Usage:
        @auth_required(product_id='your_product_id')
        def your_api_function(param1, param2):
            # 函数体
            pass
            
        @auth_required()  # 从函数参数中获取product_id
        def your_api_function(product_id, param1, param2):
            # 函数体
            pass
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 获取Authorization信息
            authorization = get_authorization() if use_authorization else None
            
            if not authorization and use_authorization:
                return {
                    "error": "未提供Authorization信息",
                    "code": "AUTHORIZATION_MISSING"
                }
            
            # 解析鉴权参数
            real_customs_params = None
            if authorization and use_authorization:
                real_customs_params = get_real_customs_params(authorization)
                if not real_customs_params:
                    return {
                        "error": "Authorization信息解析失败",
                        "code": "AUTHORIZATION_INVALID"
                    }
            
            # 确定product_id
            current_product_id = product_id
            if not current_product_id:
                # 尝试从函数参数中获取product_id
                if 'product_id' in kwargs:
                    current_product_id = kwargs['product_id']
                elif len(args) > 0 and hasattr(func, '__code__'):
                    # 检查第一个参数是否是product_id
                    param_names = func.__code__.co_varnames[:func.__code__.co_argcount]
                    if param_names and param_names[0] == 'product_id':
                        current_product_id = args[0]
            
            if not current_product_id:
                return {
                    "error": "未提供product_id",
                    "code": "PRODUCT_ID_MISSING"
                }
            
            # 将鉴权信息注入到kwargs中
            kwargs['_auth_product_id'] = current_product_id
            kwargs['_auth_real_customs_params'] = real_customs_params
            kwargs['_auth_authorization'] = authorization
            
            # 调用原函数
            return func(*args, **kwargs)
        
        return wrapper
    return decorator


def get_authorization() -> Optional[str]:
    """
    获取当前请求的Authorization头信息
    这个函数需要根据您的具体实现来调整
    """
    # 这里需要根据您的实际上下文变量实现来获取
    # 假设您有一个全局的上下文变量
    try:
        # 如果您使用了contextvars，类似这样：
        # return authorization_context.get()
        
        # 临时实现，您需要根据实际情况调整
        import contextvars
        authorization_context = contextvars.ContextVar('authorization_context', default=None)
        return authorization_context.get()
    except:
        return None


def get_real_customs_params(authorization: str) -> Optional[Dict[str, str]]:
    """
    解析Authorization信息获取真实的自定义参数
    这个函数需要根据您的具体实现来调整
    """
    if not authorization or not authorization.startswith('Token '):
        return None
    
    try:
        # 这里需要根据您的实际解密逻辑来实现
        # 假设您有symmetric_encrypt_decrypt函数
        from apps.mcp_server.utils.permission import symmetric_encrypt_decrypt
        
        authorization_part = symmetric_encrypt_decrypt(authorization[6:]).split(',')
        if len(authorization_part) == 3:
            return {
                'secret_id': authorization_part[0],
                'secret_key': authorization_part[1],
                'integrator_id': authorization_part[2],
            }
    except Exception as e:
        print(f"解析Authorization失败: {e}")
    
    return None


def call_api_with_auth(
    product_id: str,
    params: dict,
    real_customs_params: Optional[Dict[str, str]] = None,
    use_default_auth: bool = True
) -> dict:
    """
    带鉴权的API调用函数
    
    Args:
        product_id: 数据产品ID
        params: 查询参数
        real_customs_params: 鉴权参数，如果不提供则使用默认值
        use_default_auth: 是否使用默认鉴权参数
    """
    # 如果没有提供鉴权参数且需要使用默认鉴权，则使用默认值
    if not real_customs_params and use_default_auth:
        real_customs_params = {
            'secret_id': 'xxxxx',
            'secret_key': 'xxxx',
            'integrator_id': 'xxxxx'
        }
    
    if not real_customs_params:
        return {
            "error": "未提供鉴权参数",
            "code": "AUTH_PARAMS_MISSING"
        }
    
    call_params = {
        'product_id': product_id,
        'secret_id': real_customs_params.get('secret_id', ''),
        'params': json.dumps(params, ensure_ascii=False)
    }
    
    # 生成签名
    sign = signature(real_customs_params.get('secret_key', ''), call_params)
    call_params["signature"] = sign
    
    print("API调用参数:", call_params)
    
    integrator_id = real_customs_params.get('integrator_id', '')
    url = f'https://console.handaas.com/api/v1/integrator/call_api/{integrator_id}'
    
    try:
        response = requests.post(url, data=call_params)
        response.raise_for_status()
        resp_data = response.json()
        print("API响应:", json.dumps(resp_data, ensure_ascii=False))
        return resp_data
    except requests.RequestException as e:
        return {
            "error": f"API请求失败: {str(e)}",
            "code": "API_REQUEST_FAILED"
        }
    except json.JSONDecodeError as e:
        return {
            "error": f"响应解析失败: {str(e)}",
            "code": "RESPONSE_PARSE_FAILED"
        }


def signature(secret_key, params):
    print("params", params)
    keys = sorted(list(params.keys()))
    print("keys", keys)
    params_str = ''
    for key in keys:
        params_str += str(params[key])
    params_str += secret_key
    return md5(params_str.encode('utf-8')).hexdigest()


# 使用装饰器的示例函数
@auth_required(product_id='xxxx')
def query_enterprise_info(keyword: str, page_index: int = 1, page_size: int = 5, **kwargs):
    """
    查询企业信息的示例函数
    """
    params = {
        'keyword': keyword,
        'pageIndex': page_index,
        'pageSize': page_size
    }
    
    # 从装饰器注入的参数中获取鉴权信息
    product_id = kwargs.get('_auth_product_id')
    real_customs_params = kwargs.get('_auth_real_customs_params')
    
    return call_api_with_auth(product_id, params, real_customs_params, use_default_auth=False)


@auth_required()  # 从函数参数中获取product_id
def query_with_dynamic_product_id(product_id: str, keyword: str, **kwargs):
    """
    动态product_id的查询示例
    """
    params = {'keyword': keyword}
    
    # 从装饰器注入的参数中获取鉴权信息
    auth_product_id = kwargs.get('_auth_product_id')
    real_customs_params = kwargs.get('_auth_real_customs_params')
    
    return call_api_with_auth(auth_product_id, params, real_customs_params, use_default_auth=False)


def call_api_demo():
    # 原有的演示函数保持不变
    # 数据产品id
    product_id = 'xxxx'
    # accessToken 每个对接器唯一
    secret_id = 'xxxxx'
    # 秘钥 每个对接器唯一
    secret_key = 'xxxx'
    # 请求对接器ID
    integrator_id = 'xxxxx'
    # 查询数据产品的入参,json字符串格式
    params = {}

    call_params = {
        'product_id': product_id,
        'secret_id': secret_id,
        'params': json.dumps(params, ensure_ascii=False)
    }
    sign = signature(secret_key, call_params)
    call_params["signature"] = sign
    print(call_params)
    url = f'https://console.handaas.com/api/v1/integrator/call_api/{integrator_id}'
    rsp = requests.post(url, data=call_params)
    resp_data = json.dumps(rsp.json(), ensure_ascii=False)
    print(resp_data)


if __name__ == '__main__':
    print("=" * 60)
    print("鉴权装饰器使用示例")
    print("=" * 60)
    
    # 测试简化装饰器
    print("\n1. 测试简化装饰器 @simple_auth_required")
    try:
        result = search_enterprise_by_keyword("测试企业", 1, 5)
        print("查询结果:", json.dumps(result, ensure_ascii=False, indent=2))
    except Exception as e:
        print(f"查询失败: {e}")
    
    # 测试预配置鉴权
    print("\n2. 测试预配置鉴权装饰器")
    try:
        result = query_enterprise_with_preconfig("预配置测试")
        print("预配置查询结果:", json.dumps(result, ensure_ascii=False, indent=2))
    except Exception as e:
        print(f"预配置查询失败: {e}")
    
    # 测试批量查询
    print("\n3. 测试批量查询")
    queries = [
        {'matchKeyword': '腾讯', 'pageIndex': 1, 'pageSize': 2},
        {'matchKeyword': '阿里巴巴', 'pageIndex': 1, 'pageSize': 2},
        {'matchKeyword': '百度', 'pageIndex': 1, 'pageSize': 2}
    ]
    
    # 使用预配置的鉴权信息进行批量查询
    auth_config = AuthConfig('test_secret_id', 'test_secret_key', 'test_integrator_id')
    try:
        batch_results = batch_query_with_auth('675cea1f0e009a9ea37edaa1', queries, auth_config)
        print("批量查询结果:")
        for i, result in enumerate(batch_results):
            print(f"  查询 {i+1}: {json.dumps(result, ensure_ascii=False)}")
    except Exception as e:
        print(f"批量查询失败: {e}")
    
    print("\n4. 运行原有演示")
    call_api_demo()
    
    print("\n" + "=" * 60)
    print("使用说明:")
    print("=" * 60)
    print("""
1. 简化装饰器 @simple_auth_required(product_id)
   - 自动从Authorization头获取鉴权信息
   - 注入call_handaas_api函数到被装饰的函数中
   - 适用于大多数场景
   
   示例:
   @simple_auth_required('your_product_id')
   def your_function(param1, param2, **kwargs):
       call_handaas_api = kwargs.get('call_handaas_api')
       return call_handaas_api({'key': 'value'})

2. 预配置鉴权装饰器 create_auth_decorator(auth_config)
   - 使用预设的鉴权配置
   - 不依赖Authorization头
   - 适用于内部服务调用
   
   示例:
   config = AuthConfig('secret_id', 'secret_key', 'integrator_id')
   my_auth = create_auth_decorator(config)
   
   @my_auth('product_id')
   def your_function(**kwargs):
       call_handaas_api = kwargs.get('call_handaas_api')
       return call_handaas_api({'key': 'value'})

3. 批量查询函数 batch_query_with_auth()
   - 支持一次性执行多个查询
   - 可以使用Authorization头或预配置的鉴权信息
   
   示例:
   queries = [{'param1': 'value1'}, {'param1': 'value2'}]
   results = batch_query_with_auth('product_id', queries, auth_config)

4. 鉴权配置类 AuthConfig
   - 封装鉴权参数
   - 便于管理和传递鉴权信息
   
   示例:
   config = AuthConfig('secret_id', 'secret_key', 'integrator_id')

注意事项:
- 确保在MCP服务器环境中正确设置了authorization_context
- get_authorization()和get_real_customs_params()函数需要根据实际环境调整
- 所有装饰器都会进行错误处理，返回标准化的错误信息
    """)


class AuthConfig:
    """鉴权配置类"""
    def __init__(self, secret_id: str, secret_key: str, integrator_id: str):
        self.secret_id = secret_id
        self.secret_key = secret_key
        self.integrator_id = integrator_id
    
    def to_dict(self) -> Dict[str, str]:
        return {
            'secret_id': self.secret_id,
            'secret_key': self.secret_key,
            'integrator_id': self.integrator_id
        }


def simple_auth_required(product_id: str):
    """
    简化版鉴权装饰器 - 适用于大多数场景
    
    Args:
        product_id: 数据产品ID
    
    Usage:
        @simple_auth_required('your_product_id')
        def your_api_function(param1, param2):
            return call_handaas_api({'key': 'value'})
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 获取Authorization信息
            authorization = get_authorization()
            
            if not authorization:
                return {
                    "error": "未提供Authorization信息",
                    "code": "AUTHORIZATION_MISSING"
                }
            
            # 解析鉴权参数
            real_customs_params = get_real_customs_params(authorization)
            if not real_customs_params:
                return {
                    "error": "Authorization信息解析失败",
                    "code": "AUTHORIZATION_INVALID"
                }
            
            # 将call_handaas_api函数注入到函数的局部作用域
            def call_handaas_api(params: dict) -> dict:
                return call_api_with_auth(product_id, params, real_customs_params, use_default_auth=False)
            
            # 将辅助函数添加到kwargs中
            kwargs['call_handaas_api'] = call_handaas_api
            kwargs['auth_info'] = {
                'product_id': product_id,
                'authorization': authorization,
                'real_customs_params': real_customs_params
            }
            
            # 调用原函数
            return func(*args, **kwargs)
        
        return wrapper
    return decorator


def create_auth_decorator(auth_config: AuthConfig):
    """
    创建带有预配置鉴权信息的装饰器
    
    Args:
        auth_config: 鉴权配置对象
    
    Usage:
        auth_config = AuthConfig('secret_id', 'secret_key', 'integrator_id')
        my_auth = create_auth_decorator(auth_config)
        
        @my_auth('product_id')
        def your_function():
            pass
    """
    def auth_decorator(product_id: str):
        def decorator(func: Callable) -> Callable:
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                def call_handaas_api(params: dict) -> dict:
                    return call_api_with_auth(product_id, params, auth_config.to_dict(), use_default_auth=False)
                
                kwargs['call_handaas_api'] = call_handaas_api
                kwargs['auth_info'] = {
                    'product_id': product_id,
                    'auth_config': auth_config.to_dict()
                }
                
                return func(*args, **kwargs)
            
            return wrapper
        return decorator
    return auth_decorator


# 使用简化装饰器的示例
@simple_auth_required('675cea1f0e009a9ea37edaa1')
def search_enterprise_by_keyword(keyword: str, page_index: int = 1, page_size: int = 5, **kwargs):
    """
    根据关键词搜索企业信息
    """
    params = {
        'matchKeyword': keyword,
        'pageIndex': page_index,
        'pageSize': page_size
    }
    
    # 使用装饰器注入的API调用函数
    call_handaas_api = kwargs.get('call_handaas_api')
    if call_handaas_api:
        return call_handaas_api(params)
    else:
        return {"error": "API调用函数未注入", "code": "API_FUNCTION_MISSING"}


@simple_auth_required('another_product_id')
def get_company_details(company_name: str, **kwargs):
    """
    获取公司详细信息
    """
    params = {'companyName': company_name}
    
    call_handaas_api = kwargs.get('call_handaas_api')
    auth_info = kwargs.get('auth_info', {})
    
    print(f"正在查询公司: {company_name}")
    print(f"使用产品ID: {auth_info.get('product_id')}")
    
    if call_handaas_api:
        return call_handaas_api(params)
    else:
        return {"error": "API调用函数未注入", "code": "API_FUNCTION_MISSING"}


# 预配置鉴权的示例
def create_enterprise_auth():
    """创建企业查询专用的鉴权装饰器"""
    config = AuthConfig(
        secret_id='your_enterprise_secret_id',
        secret_key='your_enterprise_secret_key',
        integrator_id='your_enterprise_integrator_id'
    )
    return create_auth_decorator(config)


# 使用预配置鉴权
enterprise_auth = create_enterprise_auth()

@enterprise_auth('enterprise_product_id')
def query_enterprise_with_preconfig(keyword: str, **kwargs):
    """
    使用预配置鉴权查询企业
    """
    params = {'keyword': keyword}
    
    call_handaas_api = kwargs.get('call_handaas_api')
    return call_handaas_api(params) if call_handaas_api else {"error": "API调用失败"}


def batch_query_with_auth(product_id: str, queries: list, auth_config: AuthConfig = None) -> list:
    """
    批量查询函数
    
    Args:
        product_id: 产品ID
        queries: 查询参数列表
        auth_config: 鉴权配置，如果不提供则从Authorization头获取
    
    Returns:
        查询结果列表
    """
    results = []
    
    if auth_config:
        # 使用提供的鉴权配置
        real_customs_params = auth_config.to_dict()
    else:
        # 从Authorization头获取鉴权信息
        authorization = get_authorization()
        if not authorization:
            return [{"error": "未提供Authorization信息", "code": "AUTHORIZATION_MISSING"}]
        
        real_customs_params = get_real_customs_params(authorization)
        if not real_customs_params:
            return [{"error": "Authorization信息解析失败", "code": "AUTHORIZATION_INVALID"}]
    
    for query_params in queries:
        try:
            result = call_api_with_auth(product_id, query_params, real_customs_params, use_default_auth=False)
            results.append(result)
        except Exception as e:
            results.append({"error": f"查询失败: {str(e)}", "code": "QUERY_FAILED"})
    
    return results