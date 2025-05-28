# HANDAAS企业大数据服务 MCP

该MCP服务提供HANDAAS企业大数据服务，包括企业工商信息、企业简介、企业标签、企业业务、企业控股股东信息、企业对外投资信息、企业分支机构信息、企业主要人员信息等。

## 功能特性

- 🔍 企业关键词模糊搜索
- 🏢 企业基础信息查询
- 👥 企业控股股东信息
- 💰 企业对外投资信息
- 🏪 企业分支机构信息
- 👨‍💼 企业主要人员信息

## 环境要求

- Python 3.10+
- 依赖包：python-dotenv, requests, mcp

## 本地streamable-http快速启动

### 1. 克隆项目
```bash
git clone https://github.com/handaas/mcp-server
cd mcp-server
```

### 2. 创建虚拟环境&安装依赖

```bash
python -m venv mcp_env && source mcp_env/bin/activate
pip install -r requirements.txt
```

### 3. 环境配置

复制环境变量模板并配置：

```bash
cp .env.example .env
```

编辑 `.env` 文件，配置以下环境变量：

```env
INTEGRATOR_ID=your_integrator_id
SECRET_ID=your_secret_id
SECRET_KEY=your_secret_key
```

### 4. 启动服务

```bash
python server/enterprise_mcp_server.py
```

服务将在 `http://localhost:8000` 启动。

### 5. Cursor / Cherry Studio MCP配置

```json
{
  "mcpServers": {
    "handaas-mcp-server": {
      "type": "streamableHttp",
      "url": "http://127.0.0.1:8000/mcp"
    }
  }
}
```

## STDIO版安装部署

### 1. 修改enterprise_mcp_server脚本中启动方式为stdio

```python
mcp.run(transport="stdio")
```

### 2. 设置Cursor / Cherry Studio MCP配置

```json
{
    "mcpServers": {
      "handaas-mcp-server": {
        "command": "uv",
        "args": ["run", "mcp", "run", "{workdir}/server/enterprise_mcp_server.py"],
        "env": {
          "PATH": "{workdir}/mcp_env/bin:$PATH",
          "PYTHONPATH": "{workdir}/mcp_env",
          "INTEGRATOR_ID": "your_integrator_id",
          "SECRET_ID": "your_secret_id",
          "SECRET_KEY": "your_secret_key"
        }
      }
    }
  }
```


## 使用官方Remote服务

### 1. 直接设置Cursor / Cherry Studio MCP配置

```json
{
  "mcpServers": {
    "handaas-ent-mcp-server":{
        "url": "http://mcp.handaas.com/ent_mcp?token={token}"  
        }
  }
}
```


### 注意：integrator_id、secret_id、secret_key及token需要登录 https://www.handaas.com/ 进行注册开通平台获取


## 可用工具 (Tools)

### 1. get_keyword_search
**功能**: 关键词模糊查询企业

根据提供的企业名称、人名、品牌、产品、岗位等关键词模糊查询相关企业列表。

**参数**:
- `matchKeyword` (必需): 匹配关键词 - 查询各类信息包含匹配关键词的企业
- `pageIndex` (可选): 分页开始位置
- `pageSize` (可选): 分页结束位置 - 一页最多获取50条数据

**返回值**:
- `catchReason`: 命中原因
- `address`: 地址
- `enterpriseType`: 企业类型
- `foundTime`: 成立时间
- `homepage`: 官网
- `legalRepresentative`: 法人
- `name`: 企业名称
- `operStatus`: 经营状态
- `regCapitalCoinType`: 注册资本币种
- `regCapitalValue`: 注册资本
- `annualTurnover`: 年营业额

### 2. get_enterprise_base_info
**功能**: 查询企业基础信息

通过输入企业全称查询企业业务相关信息，识别该公司是做什么的。

**参数**:
- `keyword` (必需): 企业全称

**返回值**:
- `base_info`: 企业工商信息
- `desc`: 企业简介
- `business_info`: 企业业务
- `tag`: 企业标签

### 3. get_enterprise_holder_info
**功能**: 查询企业控股股东信息

通过输入企业全称查询企业控股股东信息，该信息通过工商信息及旷湖全部数据分析得出。

**参数**:
- `keyword` (必需): 企业全称

**返回值**:
- `holderList`: 股东列表（工商公示）
  - `entityType`: 主体类型
  - `holderType`: 股东类型
  - `name`: 股东名称
  - `nameId`: 企业id
  - `humanId`: 人员id
  - `payAmount`: 实缴金额
  - `ratio`: 持股比例
  - `subscriptionDetail`: 认缴信息
- `stockHolderList`: 股东列表（最新公示）来自于上市信息

### 4. get_enterprise_invest_info
**功能**: 查询企业对外投资信息

通过输入企业全称查询企业的对外投资信息，该信息通过工商信息及旷湖全部数据分析得出。

**参数**:
- `keyword` (必需): 企业全称

**返回值**:
- `resultList`: 对外投资结果列表
  - `addressValue`: 被投资公司所属地区
  - `business`: 被投资公司经营范围
  - `foundTime`: 被投资公司成立日期
  - `isListed`: 被投资公司上市状态
  - `legalRepresentative`: 被投资公司法定代表人
  - `name`: 对外投资企业名
  - `operStatus`: 对外投资企业经营状态
  - `ratio`: 占股比例
  - `regCapital`: 被投资公司注册资本
  - `scCode`: 对外投资企业统一信用编码
  - `subscriptionAmount`: 投资金额信息

### 5. get_enterprise_branch_info
**功能**: 查询企业分支机构信息

通过输入企业全称查询企业的分支机构信息，分支机构信息来源于工商公示。

**参数**:
- `keyword` (必需): 企业全称

**返回值**:
- `resultList`: 分支机构结果列表
  - `addressValue`: 地址信息
  - `foundTime`: 成立时间
  - `legalRepresentative`: 法定代表人
  - `name`: 机构名称
  - `operStatus`: 经营状态
  - `orgCode`: 组织机构代码
  - `registrationAuthority`: 登记机关
  - `socialCreditCode`: 统一社会信用代码

### 6. get_enterprise_main_person_info
**功能**: 查询企业主要人员信息

通过输入企业全称查询企业的主要人员信息，主要人员信息来源于工商公示。

**参数**:
- `keyword` (必需): 企业全称

**返回值**:
- `resultList`: 主要人员结果列表
  - `name`: 成员名称
  - `position`: 职位
  - `ratio`: 持股比例
  - `relatedEnterpriseCurrentNum`: 现任职企业数
  - `relatedEnterpriseHistoryNum`: 曾任职企业数


## 使用注意事项

1. **企业全称要求**: 在调用需要企业全称的接口时，需要先调用关键词模糊查询企业接口进行补全后，再调用该接口。

2. **API限制**: 分页查询时，一页最多获取50条数据。

3. **环境变量**: 确保正确配置 `INTEGRATOR_ID`、`SECRET_ID` 和 `SECRET_KEY`。

4. **错误处理**: 所有接口都包含错误处理，查询失败时会返回相应的错误信息。

5. **网络要求**: 服务器需要能够访问 `https://handaas.com` API接口。

## 故障排除

1. **环境变量未配置**: 检查 `.env` 文件是否存在且配置正确
2. **网络连接问题**: 确保服务器可以访问 `https://handaas.com`
3. **端口占用**: 如果8000端口被占用，可以修改 `enterprise_mcp_server.py` 中的端口配置

## 项目结构

```
enterprise-mcp/
├── server/
│   └── enterprise_mcp_server.py    # MCP服务器主文件
├── client_example.py               # 客户端使用示例
├── requirements.txt                # Python依赖
├── start_mcp.sh                   # 启动脚本
├── .env.example                   # 环境变量模板
└── README.md                      # 项目文档
```

## MCP使用示例

1. 探迹科技是做什么的?
2. 探迹科技有哪些股东？
3. 探迹科技对外投资了哪些企业？
4. 探迹科技有哪些分公司？
5. 探迹科技的业务有哪些？


## 联系方式

如有问题或建议，请联系开发团队。 