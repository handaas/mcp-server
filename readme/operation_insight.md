# 企业经营分析洞察服务

该服务提供企业运营相关的深度分析，包括经营状况、业务发展、市场表现等多维度运营数据洞察。

## 主要功能

- 🔍 企业关键词模糊搜索
- 📈 企业动向趋势分析
- 💼 品牌概况查询
- 🎯 企业榜单排名分析
- 💰 经营规模评估
- 📰 舆情情感分析
- 🚀 相似项目查询
- 📋 税务资质查询
- 💸 融资信息分析
- 🏷️ 产品标签识别

## 可用工具

### 1. operation_insight_fuzzy_search
**功能**: 企业关键词模糊查询

根据提供的企业名称、人名、品牌、产品、岗位等关键词模糊查询相关企业列表。

**参数**:
- `matchKeyword` (必需): 匹配关键词 - 查询各类信息包含匹配关键词的企业
- `pageIndex` (可选): 分页开始位置
- `pageSize` (可选): 分页结束位置 - 一页最多获取50条数据

**返回值**:
- `total`: 总数
- `resultList`: 结果列表，包含企业基本信息

### 2. operation_insight_company_trends
**功能**: 企业动向趋势分析

查询企业近3至12个月的动向标签数据，包括人员扩张、开设/注销分子公司、新增城市、新增融资、异地中标、入选榜单、法人变更、租约临期等动向。

**参数**:
- `matchKeyword` (必需): 匹配关键词 - 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举 - name/nameId/regNumber/socialCreditCode

**返回值**:
- `isStaffExpandIn3Month/6Month/12Month`: 是否3/6/12个月内人员扩张
- `isFoundSubsidiaryIn3Month`: 是否3个月内开设子公司
- `isCancelSubsidiaryIn3Month`: 是否3个月内注销子公司
- `isFoundBranchIn3Month`: 是否3个月内开设分公司
- `isCancelBranchIn3Month`: 是否3个月内注销分公司
- `isExpandNewCityIn3Month/6Month/12Month`: 是否3/6/12个月内新增城市
- `isNewFinancingIn3Month/6Month/12Month`: 是否3/6/12个月内新增融资
- `isDiffAreaWinBidIn3Month/6Month/12Month`: 是否3/6/12个月内异地中标
- `isAuthorityListIn6Month/12Month`: 是否近6/12个月入选榜单
- `isLegalRpAlterIn3Month/6Month/12Month`: 是否近3/6/12个月法人变更
- `nYearLeaseAboutToExpire`: 剩余租约年限

### 3. operation_insight_brand_profile
**功能**: 品牌概况查询

提供企业品牌的基本信息，包括品牌发源地、创立年份、所属行业和主营产品。

**参数**:
- `matchKeyword` (必需): 匹配关键词 - 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举 - name/nameId/regNumber/socialCreditCode

**返回值**:
- `brandCradleList`: 品牌发源地
- `brandCreateTime`: 品牌创立年份
- `brandIndustryList`: 品牌所属行业
- `brandProductList`: 主营产品

### 4. operation_insight_enterprise_rankings
**功能**: 企业榜单排名分析

查询企业的上榜信息，包括榜单类型、排名、发布年份、榜单级别以及发布单位等信息。

**参数**:
- `matchKeyword` (必需): 匹配关键词 - 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举 - name/nameId/regNumber/socialCreditCode
- `pageIndex` (可选): 页码
- `pageSize` (可选): 分页大小 - 一页最多获取10条数据

**返回值**:
- `total`: 榜单总数
- `resultList`: 榜单信息列表
  - `rankingListType`: 榜单类型（世界500强、中国500强、民营500强等）
  - `rankingListCompanyName`: 上榜公司名
  - `rankingListName`: 榜单名称
  - `rank`: 排名
  - `rankingListYear`: 发布年份
  - `rankingListLevel`: 榜单级别
  - `rankingListInstitution`: 发布单位

### 5. operation_insight_business_scale
**功能**: 经营规模评估

获取企业的经营规模相关信息，包括算法评估的企业人员规模及年营业额区间信息。

**参数**:
- `matchKeyword` (必需): 匹配关键词 - 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举 - name/nameId/regNumber/socialCreditCode

**返回值**:
- `enterpriseScale`: 人员规模
- `annualTurnover`: 年营业额

### 6. operation_insight_news_sentiment_stats
**功能**: 舆情情感分析

查询并统计企业的舆情情感类型，包括消极、中立、积极、未知四类情感的分布及其趋势变化。

**参数**:
- `matchKeyword` (必需): 匹配关键词 - 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举 - name/nameId/regNumber/socialCreditCode

**返回值**:
- `newsSentimentStats`: 舆情情感类型统计（neutral/negative/positive/unknown）
- `sentimentLabelList`: 所有舆情类别列表
- `newsSentimentTrend`: 舆情趋势
  - `month`: 月份（yyyy-mm格式）
  - `stats`: 情感类型分布

### 7. operation_insight_similar_projects
**功能**: 相似项目查询

查询与企业相关的相似项目信息，包括项目所属企业、最新融资轮次、项目概述等。

**参数**:
- `matchKeyword` (必需): 匹配关键词 - 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举 - name/nameId/regNumber/socialCreditCode
- `pageIndex` (可选): 页码 - 从1开始
- `pageSize` (可选): 分页大小 - 一页最多获取10条数据

**返回值**:
- `total`: 总数
- `resultList`: 结果列表
  - `projectName`: 项目名称
  - `enterpriseName`: 所属企业
  - `nameId`: 所属企业id
  - `financingSeries`: 最新轮次
  - `fpIntroduction`: 项目概述
  - `logo`: 项目图片

### 8. operation_insight_tax_qualifications
**功能**: 税务资质查询

查询企业的税务资质信息，包括纳税人识别号、纳税人名称、资质全称等。

**参数**:
- `matchKeyword` (必需): 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举 - name/nameId/regNumber/socialCreditCode

**返回值**:
- `tpQualificationList`: 企业税务资质信息
  - `tpId`: 纳税人识别号
  - `tpName`: 纳税人名称
  - `qualification`: 资质全称
  - `begin`: 有效期起
  - `end`: 有效期止

### 9. operation_insight_financing_info
**功能**: 融资信息分析

查询企业的融资信息，包括融资次数、详细的融资记录、融资金额、融资轮次、融资时间和投资方等。

**参数**:
- `matchKeyword` (必需): 匹配关键词 - 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举 - name/nameId/regNumber/socialCreditCode

**返回值**:
- `fpFinancingCount`: 融资次数
- `fpFinancingList`: 融资信息
  - `financingAmount`: 融资金额
  - `financingSeries`: 融资轮次
  - `financingTime`: 融资时间
  - `investorList`: 投资方

### 10. operation_insight_product_tags
**功能**: 产品标签识别

根据企业基本信息返回该企业的产品标签，用于识别企业产品的特性和类别。

**参数**:
- `matchKeyword` (必需): 匹配关键词 - 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举 - name/nameId/regNumber/socialCreditCode

**返回值**:
- `tagNames`: 产品标签

## 使用场景

1. **企业运营分析**: 深度了解企业运营状况和发展趋势，制定运营策略
2. **投资决策支持**: 为投资决策提供全面的运营数据支撑和风险评估
3. **竞争对手研究**: 分析竞争对手的运营表现、品牌实力和市场地位
4. **市场研究**: 了解行业整体运营水平和发展趋势，把握市场机会
5. **业务合作评估**: 评估潜在合作伙伴的运营能力和财务状况
6. **舆情监控**: 监控企业舆情变化，进行声誉管理和危机预警
7. **融资分析**: 分析企业融资历史和投资方背景，评估融资能力
8. **税务合规**: 查询税务资质信息，确保合规经营

## 使用注意事项

1. **企业全称要求**: 在调用需要企业全称的接口时，如果没有企业全称则先调取operation_insight_fuzzy_search接口获取企业全称
2. **数据时效性**: 运营数据会定期更新，建议关注数据时间和趋势变化
3. **综合分析**: 建议结合多个维度进行综合分析，避免单一指标误判
4. **行业对比**: 可以进行同行业企业运营对比分析，提高分析准确性
5. **舆情敏感**: 舆情数据具有时效性和敏感性，需谨慎使用和解读
6. **融资保密**: 部分融资信息可能涉及商业机密，数据可能不完整

## 使用提问示例

### operation_insight_fuzzy_search (企业关键词模糊搜索)
1. 帮我查找包含"字节跳动"关键词的企业信息
2. 搜索与"美团"相关的企业列表
3. 查询名称中包含"滴滴"的公司

### operation_insight_company_trends (企业动向趋势分析)
1. 分析字节跳动最近的企业动向趋势
2. 美团近期有哪些重要的企业动态？
3. 滴滴出行的人员扩张和业务拓展情况

### operation_insight_brand_profile (品牌概况查询)
1. 字节跳动的品牌画像信息
2. 美团品牌的发源地和创立年份
3. 滴滴出行的品牌行业分类和主营产品

### operation_insight_enterprise_rankings (企业榜单排名分析)
1. 字节跳动入选了哪些权威榜单？
2. 美团在各类企业排行榜中的表现
3. 查询滴滴出行的榜单排名情况

### operation_insight_business_scale (经营规模评估)
1. 字节跳动的企业经营规模如何？
2. 美团的人员规模和年营业额
3. 滴滴出行的企业规模分析

### operation_insight_news_sentiment_stats (舆情情感分析)
1. 分析字节跳动的舆情情感分布
2. 美团最近的舆情趋势如何？
3. 滴滴出行的舆情分析报告

### operation_insight_similar_projects (相似项目查询)
1. 与字节跳动相似的项目有哪些？
2. 查询美团的相似项目信息
3. 滴滴出行的同类项目分析

### operation_insight_tax_qualifications (税务资质查询)
1. 查询字节跳动的税务资质信息
2. 美团的纳税人资质详情
3. 滴滴出行的税务资质证书

### operation_insight_financing_info (融资信息分析)
1. 字节跳动的融资历史记录
2. 美团各轮融资的详细信息
3. 滴滴出行的投资方和融资轮次

### operation_insight_product_tags (产品标签识别)
1. 字节跳动科技有限公司的产品标签有哪些？
2. 美团的产品特性标签分析
3. 查询滴滴出行的产品标签信息 