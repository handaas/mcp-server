# 海关大数据服务

该服务提供全面的进出口贸易数据查询功能，包括出口趋势分析、商品类别统计、订单地理分布、海外认证信息等，帮助用户了解企业的国际贸易情况。

## 主要功能

- 🔍 企业关键词模糊搜索
- 📈 出口趋势分析
- 📦 出口商品分析
- 🌍 订单地理分布
- 👥 外贸招聘分析
- 📋 海外认证查询

## 可用工具

### 1. fuzzy_search
**功能**: 企业关键词模糊查询

根据提供的企业名称、人名、品牌、产品、岗位等关键词模糊查询相关企业列表。

**参数**:
- `matchKeyword` (必需): 匹配关键词
- `pageIndex` (可选): 分页开始位置
- `pageSize` (可选): 分页结束位置

**返回值**:
- `total`: 总数
- `resultList`: 结果列表

### 2. export_trends
**功能**: 出口趋势分析

根据企业的身份标识信息查询该企业的外贸出口趋势，包括每年的出口金额和订单数量等数据。

**参数**:
- `matchKeyword` (必需): 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举

**返回值**:
- `exportTrend`: 出口年份列表
  - `amount`: 金额（美元）
  - `count`: 订单数量
  - `year`: 年份
- `total`: 出口年份总数

### 3. export_product_trends
**功能**: 出口商品趋势分析

查询并分析企业外贸商品的发展趋势，提供企业在不同年份的出口商品订单量及海关HS编码分布信息。

**参数**:
- `matchKeyword` (必需): 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举

**返回值**:
- `exportGoodsOrderDistribution`: 出口商品订单量分布
  - `orderCountOfYear`: 每年的订单量
  - `count`: 数量
  - `hsCode`: 海关HS商品编码
  - `year`: 年份
- `exportGoodsOrderTrend`: 出口商品订单量趋势
  - `year`: 年份
  - `count`: 数量
  - `name`: 名称

### 4. export_recruitment_profile
**功能**: 外贸招聘分析

根据输入的企业标识信息，获取企业在过去三个月内的外贸相关岗位的招聘情况。

**参数**:
- `matchKeyword` (必需): 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举

**返回值**:
- `recruitingLatestThreeMonthCount`: 近三个月招聘岗位数
- `recruitingCityCount`: 招聘城市数量
- `recruitingCityList`: 招聘城市
- `recruitingCount`: 招聘岗位数
- `recruitingPositions`: 招聘岗位名称
- `recruitingPlatforms`: 外贸相关岗位平台
- `recruitingSourceCount`: 招聘渠道数量
- `recruitingSourceList`: 招聘渠道

### 5. export_order_regions
**功能**: 出口订单地理分布

根据提供的企业标识信息查询该企业外贸订单的地理分布情况，包括各地区的订单金额、数量等。

**参数**:
- `matchKeyword` (必需): 企业名称/注册号/统一社会信用代码/企业id
- `pageIndex` (可选): 页码 - 从1开始
- `pageSize` (可选): 分页大小 - 一页最多获取50条
- `keywordType` (可选): 主体类型枚举

**返回值**:
- `resultList`: 订单地区分布列表
  - `amount`: 金额（美元）
  - `count`: 订单数
  - `destCountry`: 国家/地区
  - `weight`: 净重（千克）
- `total`: 分布地区总数

### 6. overseas_certifications
**功能**: 海外认证信息查询

根据企业的名称、注册编号等查询企业的海外认证信息，包括认证类别、证书编号及相关产品信息。

**参数**:
- `matchKeyword` (必需): 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举

**返回值**:
- `certType`: 认证类别
- `certId`: 证书号
- `certCount`: 总数
- `certDomain`: 认证领域
- `certProductName`: 产品名称

## 使用场景

1. **企业国际贸易分析**: 了解企业的出口能力和市场份额变化趋势
2. **竞争对手研究**: 分析竞争对手在国际市场中的表现
3. **金融风险评估**: 银行或投资机构评估企业的国际贸易风险和收益
4. **市场拓展策略**: 制定更加有效的国际市场拓展策略
5. **政府统计研究**: 政府或行业协会统计企业整体外贸出口趋势
6. **招投标资质验证**: 企业在申请招投标过程中提交资质证明

## 使用注意事项

1. **企业全称要求**: 在调用需要企业全称的接口时，如果没有企业全称则先调取fuzzy_search接口获取企业全称
2. **分页限制**: 一页最多获取50条数据
3. **金额单位**: 出口金额以美元为单位
4. **重量单位**: 净重以千克为单位
5. **时间范围**: 招聘信息为过去三个月内的数据
6. **HS编码**: 商品分类基于海关HS编码标准 