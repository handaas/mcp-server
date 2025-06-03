# 旷湖企业大数据服务MCP

[该MCP服务提供旷湖企业大数据服务，是一个全面的企业信息查询和分析平台，涵盖企业工商信息、风险分析、知识产权、地理分布、经营洞察等多个维度的专业数据服务。](https://www.handaas.com/)

## 简介

旷湖企业大数据服务MCP是基于旷湖海量企业数据构建的Model Context Protocol（MCP）服务集合，为用户提供一站式企业信息查询和分析能力。通过结构化的API接口，用户可以轻松获取企业的全方位信息，包括但不限于：

- **企业基础信息**: 工商信息、企业简介、业务范围、组织架构等
- **风险评估分析**: 违法记录、失信信息、经营异常、司法风险等
- **知识产权资产**: 商标、专利、著作权等知识产权信息
- **地理分布数据**: 办公地址、分支机构、楼宇信息等
- **经营洞察分析**: 招投标、进出口、渠道分布、经营表现等
- **行业专业数据**: 资质证书、展会参展、政策扶持等

## 核心功能特性

### 🏢 企业基础信息
- **工商信息查询**: 注册资本、成立时间、经营状态、法定代表人等
- **企业画像分析**: 企业简介、主营业务、行业标签等
- **股权结构分析**: 控股股东、对外投资、分支机构等
- **关键人员信息**: 主要人员、任职信息、股权关系等

### ⚠️ 风险评估体系
- **合规风险监控**: 严重违法记录、行政处罚、经营异常等
- **信用风险评估**: 失信被执行人、动产抵押、司法案件等
- **经营风险分析**: 经营状态变更、注册信息变更等
- **综合风险评级**: 多维度风险指标综合评估

### 🔒 知识产权管理
- **商标资产分析**: 商标搜索、企业商标概况、商标状态统计
- **专利技术评估**: 专利搜索、专利统计、技术领域分布
- **知识产权趋势**: 申请授权趋势、类别分布、竞争分析

### 🌍 楼宇入驻分析
- **办公地址分析**: 企业办公地址详情、城市分布统计
- **楼宇信息查询**: 楼宇详情、入驻企业、楼宇类型分析
- **区域业务布局**: 分支机构分布、地理覆盖范围

### 📊 经营洞察分析
- **招投标信息**: 中标记录、招标参与情况、竞争分析
- **进出口贸易**: 贸易记录、贸易伙伴、商品类别分析
- **渠道分布**: 经销商网络、销售渠道、市场覆盖
- **经营表现**: 运营数据、业务发展趋势、市场表现

### 🏅 资质认证体系
- **行业资质**: 各类行业准入资质、经营许可证
- **认证证书**: 质量认证、环境认证、安全认证等
- **政策支持**: 政府补贴、优惠政策、扶持项目

### 🎯 行业专业服务
- **制造业洞察**: 生产能力、制造工艺、设备配置
- **电商平台分析**: 店铺信息、销售数据、产品分析
- **展会参展**: 参展历史、展会类型、产品展示
- **云服务分析**: 云用量统计、上云资产分析

## 服务文档

### 核心服务
- [🏢 企业基础信息服务](readme/enterprise.md) - 提供企业工商信息、简介、股权结构等基础查询
- [⚠️ 企业风险分析洞察服务](readme/risk_insight.md) - 提供全面的企业风险评估和分析
- [📄 商标大数据服务](readme/trademark.md) - 提供商标信息查询和统计分析
- [🔬 专利大数据服务](readme/patent.md) - 提供专利信息查询和技术分析
- [🏙️ 楼宇大数据服务](readme/building.md) - 提供办公地址和楼宇信息查询

### 专业服务
- [📋 招投标大数据服务](readme/bid.md) - 提供招投标信息查询和中标分析
- [📈 运营洞察服务](readme/operation_insight.md) - 提供企业运营数据分析和洞察
- [🏪 门店大数据服务](readme/store.md) - 提供线下门店信息查询和餐饮品牌分析
- [📦 海关大数据服务](readme/customs.md) - 提供进出口贸易数据和海外认证查询
- [🏆 资质证书服务](readme/qualification.md) - 提供企业资质证书和行政许可查询
- [🎪 展会大数据服务](readme/exhibition.md) - 提供展会参展记录和场馆信息查询
- [🛒 电商大数据服务](readme/estore.md) - 提供电商平台店铺信息和销售数据分析
- [📜 政策大数据服务](readme/policy.md) - 提供政府补贴和政策支持信息查询
- [🏭 工厂洞察服务](readme/factory.md) - 提供制造业生产能力和工艺分析
- [🏪 渠道洞察服务](readme/channel.md) - 提供销售渠道和经销商网络分析
- [☁️ 上云企业洞察服务](readme/cloudmigration.md) - 提供云服务使用和技术栈分析

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

### 4. 修改server/enterprise_mcp_server脚本中启动方式为streamable-http

```python
mcp.run(transport="streamable-http")
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

### 1. 修改server/enterprise_mcp_server脚本中启动方式为stdio

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
### 3. 其他全部mcpServer配置参考[all_mcp_config.json](all_mcp_config.json)

## 使用官方Remote服务(暂时只支持企业大数据MCP)

### 1. 直接设置Cursor / Cherry Studio MCP配置

```json
{
  "mcpServers": {
    "handaas-ent-mcp-server":{
      "type": "streamableHttp",
      "url": "https://mcp.handaas.com/enterprise/enterprise_profile?token={token}"  
      }
  }
}
```

### 注意：integrator_id、secret_id、secret_key及token需要登录 https://www.handaas.com/ 进行注册开通平台获取

## 多服务部署

除了企业基础信息服务外，我们还提供了多个专业服务，每个服务都可以独立部署：

```bash
# 企业基础信息服务
python server/enterprise_mcp_server.py

# 风险分析服务
python server/risk_insight_mcp_server.py

# 商标大数据服务
python server/trademark_bigdata_mcp_server.py

# 专利大数据服务
python server/patent_bigdata_mcp_server.py

# 楼宇大数据服务
python server/building_bigdata_mcp_server.py

# 招投标大数据服务
python server/bid_bigdata_mcp_server.py

# 运营洞察服务
python server/operation_insight_mcp_server.py

# 门店大数据服务
python server/store_bigdata_mcp_server.py

# 海关大数据服务
python server/customs_bigdata_mcp_server.py

# 资质证书服务
python server/qualification_bigdata_mcp_server.py

# 展会大数据服务
python server/exhibition_bigdata_mcp_server.py

# 电商大数据服务
python server/estore_bigdata_mcp_server.py

# 政策大数据服务
python server/policy_bigdata_mcp_server.py

# 工厂洞察服务
python server/factory_insight_mcp_server.py

# 渠道洞察服务
python server/channel_insight_mcp_server.py

# 云迁移服务
python server/cloudmigration_mcp_server.py
```

## 使用注意事项

1. **企业全称要求**: 在调用需要企业全称的接口时，需要先调用关键词模糊查询企业接口进行补全后，再调用该接口。

2. **API限制**: 分页查询时，不同服务有不同的分页限制，具体请参考各服务文档。

3. **环境变量**: 确保正确配置 `INTEGRATOR_ID`、`SECRET_ID` 和 `SECRET_KEY`。

4. **错误处理**: 所有接口都包含错误处理，查询失败时会返回相应的错误信息。

5. **网络要求**: 服务器需要能够访问 `https://handaas.com` API接口。

6. **数据时效性**: 各类数据会定期更新，建议关注数据的时间戳。

## 故障排除

1. **环境变量未配置**: 检查 `.env` 文件是否存在且配置正确
2. **网络连接问题**: 确保服务器可以访问 `https://handaas.com`
3. **端口占用**: 如果8000端口被占用，可以修改 `enterprise_mcp_server.py` 中的端口配置
4. **权限问题**: 确保API密钥有效且有足够的访问权限

## 项目结构

```
enterprise-mcp/
├── server/                              # MCP服务器文件
│   ├── enterprise_mcp_server.py         # 企业基础信息服务
│   ├── risk_insight_mcp_server.py       # 风险分析服务
│   ├── trademark_bigdata_mcp_server.py  # 商标大数据服务
│   ├── patent_bigdata_mcp_server.py     # 专利大数据服务
│   ├── building_bigdata_mcp_server.py   # 楼宇大数据服务
│   ├── bid_bigdata_mcp_server.py        # 招投标服务
│   ├── operation_insight_mcp_server.py  # 运营洞察服务
│   ├── store_bigdata_mcp_server.py      # 门店大数据服务
│   ├── customs_bigdata_mcp_server.py    # 海关大数据服务
│   ├── qualification_bigdata_mcp_server.py # 资质证书服务
│   ├── exhibition_bigdata_mcp_server.py # 展会大数据服务
│   ├── estore_bigdata_mcp_server.py     # 电商大数据服务
│   ├── policy_bigdata_mcp_server.py     # 政策大数据服务
│   ├── factory_insight_mcp_server.py    # 工厂洞察服务
│   ├── channel_insight_mcp_server.py    # 渠道洞察服务
│   └── cloudmigration_mcp_server.py     # 云迁移服务
├── readme/                              # 服务文档目录
│   ├── enterprise.md                    # 企业基础信息文档
│   ├── risk_insight.md                  # 风险分析文档
│   ├── trademark.md                     # 商标服务文档
│   ├── patent.md                        # 专利服务文档
│   ├── building.md                      # 楼宇服务文档
│   ├── bid.md                           # 招投标服务文档
│   ├── operation_insight.md             # 运营洞察文档
│   ├── store.md                         # 门店大数据文档
│   ├── customs.md                       # 海关大数据文档
│   ├── qualification.md                 # 资质证书文档
│   ├── exhibition.md                    # 展会大数据文档
│   ├── estore.md                        # 电商大数据文档
│   ├── policy.md                        # 政策大数据文档
│   ├── factory.md                       # 工厂洞察文档
│   ├── channel.md                       # 渠道洞察文档
│   ├── cloudmigration.md                # 上云企业服务文档
│   └── other_services.md                # 其他服务概览
├── requirements.txt                     # Python依赖
├── start_mcp.sh                        # 启动脚本
├── .env.example                        # 环境变量模板
└── README.md                           # 项目文档
```

## MCP使用示例

1. 探迹科技是做什么的?
2. 探迹科技有哪些股东？
3. 探迹科技对外投资了哪些企业？
4. 探迹科技有哪些分公司？
5. 探迹科技的业务有哪些？
6. 查询腾讯的风险信息
7. 查询阿里巴巴的商标信息
8. 查询华为的专利分布
9. 查询字节跳动的办公地址
10. 查询百度的招投标记录

## 联系方式

如有问题或建议，请联系开发团队。 