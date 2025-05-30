# 电商大数据服务

该服务提供全面的电商平台企业信息查询功能，包括电商店铺信息、销售数据分析、产品类别统计等，帮助用户了解企业的电商业务布局。

## 主要功能

- 🔍 企业关键词模糊搜索
- 🛒 全球网店概况查询
- 📊 电商产品概况分析
- 🏬 电商店铺信息查询
- 📦 产品类别统计
- 🌐 平台分布分析

## 可用工具

### 1. fuzzy_search
**功能**: 企业关键词模糊查询

根据提供的企业名称、人名、品牌、产品、岗位等关键词模糊查询相关企业列表。

**参数**:
- `matchKeyword` (必需): 匹配关键词 - 查询各类信息包含匹配关键词的企业
- `pageIndex` (可选): 分页开始位置
- `pageSize` (可选): 分页结束位置 - 一页最多获取50条数据

**返回值**:
- `total`: 总数
- `resultList`: 结果列表
  - `nameId`: 企业id
  - `name`: 企业名称
  - `socialCreditCode`: 统一社会信用代码
  - `legalRepresentative`: 法定代表人
  - `enterpriseType`: 企业主体类型
  - `operStatus`: 企业状态
  - `address`: 注册地址
  - `foundTime`: 成立时间
  - `regCapitalValue`: 注册资本金额
  - `catchReason`: 命中原因

### 2. global_online_store_profile
**功能**: 全球网店概况查询

提供企业在国内外的网店概况信息，包括网店数量、商品总量、销售平台、主营品牌和产品等详细信息。

**参数**:
- `matchKeyword` (必需): 匹配关键词 - 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举 - name/nameId/regNumber/socialCreditCode

**返回值**:
- `domesticEshopCount`: 国内网店数量
- `domesticEshopProductCount`: 国内网店商品总量
- `domesticEshopBrandList`: 国内网店主营品牌
- `domesticEshopPlatformList`: 国内网店上架平台
- `domesticEshopProductList`: 国内网店主营产品
- `domesticEshopSourceList`: 国内网店来源
- `foreignEshopCount`: 国外网店数量
- `foreignEshopProductCount`: 国外网店商品总量
- `foreignEshopBrandList`: 国外网店主营品牌
- `foreignEshopPlatformList`: 国外网店上架平台
- `foreignEshopProductList`: 国外网店主营产品
- `foreignEshopSourceList`: 国外网店来源

### 3. ecommerce_product_profile
**功能**: 电商产品概况分析

查询企业在电商平台上的店铺及商品概况，包括品牌信息、评分、创建时间等详细信息。

**参数**:
- `matchKeyword` (必需): 匹配关键词 - 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举 - name/nameId/regNumber/socialCreditCode

**返回值**:
- `ecShopNumber`: 店铺个数
- `ecShopItemCount`: 店铺商品总数
- `ecShopAvgRates`: 店铺平均评分（分）
- `ecShopEarliestFoundTime`: 店铺创建时间
- `ecShopItemCategories`: 产品分类
- `ecShopBrands`: 主营品牌
- `ecShopProducts`: 主营产品
- `ecSources`: 上架平台

### 4. ecommerce_store_info
**功能**: 电商店铺信息查询

查询与企业相关联的网店信息，返回网店的详细信息和业务数据概览。

**参数**:
- `matchKeyword` (必需): 匹配关键词 - 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举 - name/nameId/regNumber/socialCreditCode

**返回值**:
- `eshopListCount`: 关联网店总数
- `enterpriseEshopCount`: 网店数量
- `enterpriseEshopProductsCount`: 网店商品总量
- `enterpriseEshopBrands`: 主营品牌
- `enterpriseEshopProducts`: 主营产品
- `enterpriseEshopPlatforms`: 网店上架平台
- `eshopList`: 关联网店列表
  - `eshopName`: 网店名称
  - `eshopKeeper`: 掌柜名称
  - `eshopFoundTime`: 开店时间
  - `eshopUrl`: 网店url
  - `eshopIconLink`: 网店logo
  - `eshopProducts`: 主营类目
  - `enterpriseName`: 所属企业
  - `address`: 网店位置
  - `businessStatistics`: 经营状况
  - `isExpired`: 网店是否过期
- `overview`: 网店数据概览

## 使用场景

1. **电商运营分析**: 了解企业在各电商平台的运营情况和市场表现
2. **竞争对手研究**: 分析竞争对手的电商布局和销售策略
3. **市场调研**: 研究特定行业的电商发展趋势和市场机会
4. **投资决策**: 评估企业的电商业务发展潜力和商业价值
5. **合作伙伴选择**: 寻找优质的电商合作伙伴和供应商
6. **品牌监控**: 监控企业品牌在电商平台的表现和声誉
7. **供应链分析**: 了解企业的电商供应链和产品分布

## 使用注意事项

1. **企业全称要求**: 在调用需要企业全称的接口时，如果没有企业全称则先调取fuzzy_search接口获取企业全称
2. **平台差异**: 不同电商平台的数据结构和统计方式可能有所差异
3. **数据时效性**: 电商数据更新频率较高，建议关注数据时间戳
4. **销售数据**: 部分销售数据可能为估算值，仅供参考
5. **国际数据**: 国外网店数据的完整性和准确性可能受限于数据来源
6. **店铺状态**: 注意区分活跃店铺和已关闭店铺的状态 