# 旷湖大数据服务MCP平台

[该MCP服务提供旷湖企业大数据服务，是一个全面的信息查询和分析平台，涵盖企业工商信息、风险分析、知识产权、经营洞察等多个维度的专业数据服务。](https://www.handaas.com/)

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
- [🏢 企业基础信息服务](https://github.com/handaas/enterprise-mcp-server) - 提供企业工商信息、简介、股权结构等基础查询
- [⚠️ 企业风险分析洞察](https://github.com/handaas/enterprise-risk-mcp-server) - 提供全面的企业风险评估和分析
- [📄 商标大数据服务](https://github.com/handaas/trademark-mcp-server) - 提供商标信息查询和统计分析
- [🔬 专利大数据服务](https://github.com/handaas/patent-mcp-server) - 提供专利信息查询和技术分析
- [🏙️ 楼宇大数据服务](https://github.com/handaas/building-mcp-server) - 提供办公地址和楼宇信息查询

### 专业服务
- [📋 招投标大数据服务](https://github.com/handaas/bidding-mcp-server) - 提供招投标信息查询和中标分析
- [📈 运营洞察服务](https://github.com/handaas/enterprise-operation-mcp-server) - 提供企业运营数据分析和洞察
- [🏪 门店大数据服务](https://github.com/handaas/store-mcp-server) - 提供线下门店信息查询和餐饮品牌分析
- [📦 海关大数据服务](https://github.com/handaas/customs-mcp-server) - 提供进出口贸易数据和海外认证查询
- [🏆 资质证书服务](https://github.com/handaas/qualification-mcp-server) - 提供企业资质证书和行政许可查询
- [🎪 展会大数据服务](https://github.com/handaas/exhibition-mcp-server) - 提供展会参展记录和场馆信息查询
- [🛒 电商大数据服务](https://github.com/handaas/estore-mcp-server) - 提供电商平台店铺信息和销售数据分析
- [📜 政策大数据服务](https://github.com/handaas/policy-mcp-server) - 提供政府补贴和政策支持信息查询
- [🏭 工厂洞察服务](https://github.com/handaas/factory-mcp-server) - 提供制造业生产能力和工艺分析
- [🏪 渠道洞察服务](https://github.com/handaas/factory-channel-mcp-server) - 提供企业销售渠道和经销商网络分析
- [☁️ 上云大数据服务](https://github.com/handaas/cloudmigration-mcp-server) - 提供企业的云上资产信息。

## 环境要求

- Python 3.10+
- 依赖包：python-dotenv, requests, mcp

## 本地streamable-http快速启动、STDIO版安装部署参考服务文档中各核心服务项目

## 使用官方Remote服务

### 1. 直接设置Cursor / Cherry Studio MCP配置

#### 配置格式
```json
{
  "mcpServers": {
    "handaas-mcp-server":{
      "type": "streamableHttp",
      "url": "https://mcp.handaas.com/{URL路径}?token={token}"  
      }
  }
}
```

#### 全部线上MCP配置

| MCP名称 | 子类 | URL路径 |
|---------|------|-----|
| 企业大数据 | 企业基础信息分析 | enterprise/enterprise_profile |
| 企业大数据 | 企业风险分析洞察 | enterprise/risk_insight |
| 企业大数据 | 企业经营分析洞察 | enterprise/operation_insight |
| 工厂大数据 | 工厂信息分析洞察 | factory/factory_insight |
| 工厂大数据 | 渠道信息分析洞察 | factory/channel_insight |
| 店铺大数据 | 店铺大数据 | store/store_bigdata |
| 展会大数据 | 展会大数据 | exhibition/exhibition_bigdata |
| 楼宇大数据 | 楼宇大数据 | building/building_bigdata |
| 标讯大数据 | 标讯大数据 | bidding/bidding_bigdata |
| 专利大数据 | 专利大数据 | patent/patent_bigdata |
| 商标大数据 | 商标大数据 | trademark/trademark_bigdata |
| 海关大数据 | 海关大数据 | customs/customs_bigdata |
| 政策大数据 | 政策大数据 | policy/policy_bigdata |
| 资质大数据 | 资质大数据 | qualification/qualification_bigdata |
| 网店大数据 | 网店大数据 | estore/estore_bigdata |
| 上云大数据 | 上云大数据 | cloudmigration/cloudmigration |


#### 配置示例（以“企业基础信息分析”为例）

```json
{
  "mcpServers": {
    "handaas-enterprise-profile-server":{
      "type": "streamableHttp",
      "url": "https://mcp.handaas.com/enterprise/enterprise_profile?token={token}"  
      }
  }
}
```



### 注意：integrator_id、secret_id、secret_key及token需要登录 https://www.handaas.com/ 进行注册开通平台获取


## 联系方式

如有问题或建议，请联系开发团队。 