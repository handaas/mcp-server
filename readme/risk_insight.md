# 企业风险分析洞察服务

该服务提供全面的企业风险分析功能，包括严重违法记录查询、动产抵押信息、失信被执行人、经营异常、行政处罚等风险信息查询，帮助用户进行企业合规风险评估。

## 主要功能

- 🔍 企业关键词模糊搜索
- ⚠️ 严重违法记录查询
- 🏦 动产抵押信息查询
- 📋 失信被执行人查询
- 🚫 经营异常名录查询
- 💰 行政处罚信息查询
- ⚖️ 司法案件信息查询

## 可用工具

### 1. risk_insight_fuzzy_search
**功能**: 企业关键词模糊查询

根据提供的企业名称、人名、品牌、产品、岗位等关键词模糊查询相关企业列表。

**参数**:
- `matchKeyword` (必需): 匹配关键词
- `pageIndex` (可选): 分页开始位置
- `pageSize` (可选): 分页结束位置

**返回值**:
- `total`: 总数
- `resultList`: 结果列表

### 2. risk_insight_serious_violations
**功能**: 严重违法记录查询

查询某一家企业在政府监管下的严重违法记录，包括严重违法的详细信息和处理状态。

**参数**:
- `matchKeyword` (必需): 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举

**返回值**:
- `illegalCount`: 严重违法数量
- `illegalInfoList`: 严重违法列表
  - `createAuthority`: 做出决定机关（列入）
  - `createDate`: 列入日期
  - `createReason`: 列入原因
  - `removeAuthority`: 做出决定机关（移除）
  - `removeDate`: 移除日期
  - `type`: 类别
  - `removeReason`: 移除原因

### 3. risk_insight_chattel_mortgage
**功能**: 动产抵押信息查询

查询企业的动产抵押信息，提供有关动产抵押的详细数据，包括抵押的数量、列表信息以及相关主体和债权信息。

**参数**:
- `matchKeyword` (必需): 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举

**返回值**:
- `mortgageCount`: 动产抵押数量
- `mortgageInfoList`: 动产抵押列表
  - `authority`: 登记机关
  - `mortgageId`: 登记编号
  - `date`: 登记日期
  - `amount`: 被担保债权数额
  - `publicationDate`: 公示日期
  - `term`: 债务人履行债务的期限
  - `type`: 种类
  - `guaranteedCreditorInfo`: 被担保主债券信息
  - `mortgageeList`: 抵押权人信息
  - `pawnList`: 抵押物信息
  - `revokeInfo`: 注销信息

### 4. risk_insight_court_hearings
**功能**: 法院开庭公告查询

查询与给定企业相关的开庭公告信息，提供详细的庭审和公告细节。

**参数**:
- `matchKeyword` (必需): 企业名称/注册号/统一社会信用代码/企业id
- `pageIndex` (可选): 页码
- `pageSize` (可选): 分页大小
- `keywordType` (可选): 主体类型枚举

**返回值**:
- `total`: 总数
- `resultList`: 列表结果
  - `address`: 庭审地点
  - `caseReason`: 案由
  - `date`: 开庭日期
  - `publishPage`: 公告版面
  - `publishDate`: 公告日期
  - `publishUnit`: 开庭法院
  - `caseType`: 公告类型
  - `relatedCaseNumber`: 案号
  - `caseId`: 开庭公告id
  - `caseRelatedPerson`: 当事人

### 5. risk_insight_litigation_risk_profile
**功能**: 诉讼风险画像查询

查询企业的法律诉讼风险情况，输出包括法院公告、立案公告、开庭公告、裁判文书、被执行人、失信被执行人和限制高消费等信息。

**参数**:
- `matchKeyword` (必需): 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举

**返回值**:
- `caList`: 法院公告列表
- `caTotal`: 法院公告总数
- `caLianTotal`: 立案公告总数
- `caLianList`: 立案公告列表
- `caKaitingTotal`: 开庭公告总数
- `caKaitingList`: 开庭公告列表
- `jdTotal`: 裁判文书总数
- `jdList`: 裁判文书列表
- `enforcementList`: 被执行人列表
- `edTotal`: 失信被执行人总数
- `edList`: 失信被执行人列表
- `enforcementTotal`: 被执行人总数
- `limitedTotal`: 限制高消费总数
- `limitedList`: 限制高消费列表

### 6. risk_insight_court_announcements
**功能**: 法院公告查询

查询特定企业在法院公告中的相关信息，包括庭审地点、当事人、案由等细节。

**参数**:
- `matchKeyword` (必需): 企业名称/注册号/统一社会信用代码/企业id
- `pageIndex` (可选): 页码
- `pageSize` (可选): 分页大小
- `keywordType` (可选): 主体类型枚举

**返回值**:
- `total`: 总数
- `resultList`: 列表结果
  - `caseType`: 公告类型
  - `date`: 开庭日期
  - `caseRelatedPerson`: 当事人
  - `address`: 庭审地点
  - `publishDate`: 公告日期
  - `publishUnit`: 开庭法院
  - `caseReason`: 案由
  - `relatedCaseNumber`: 案号
  - `publishPage`: 公告版面
  - `caseId`: 法院公告id

### 7. risk_insight_intellectual_property_pledge
**功能**: 知识产权出质查询

检索并返回某企业的知识产权出质信息，包括出质数量、相关列表及详细信息。

**参数**:
- `matchKeyword` (必需): 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举

**返回值**:
- `iprPledgeCount`: 知识产权出质数量
- `iprPledgeList`: 知识产权出质列表
  - `iprName`: 知识产权名称
  - `iprPledgePeriod`: 质权登记期限
  - `iprPledgePublicDate`: 知识产权公示日期
  - `iprPledgeeName`: 知识产权质权人
  - `iprRegisterNum`: 知识产权登记编号
  - `iprPledgorName`: 知识产权出质人
  - `iprType`: 知识产权种类
  - `iprPledgeRevokeDate`: 知识产权注销日期
  - `iprPledgeRevokeReason`: 知识产权注销原因
  - `iprStatus`: 知识产权状态

### 8. risk_insight_tax_penalties
**功能**: 税务行政处罚查询

查询某一企业在税务局的行政处罚记录，包括处罚的详细信息。

**参数**:
- `matchKeyword` (必需): 企业名称/注册号/统一社会信用代码/企业id
- `pageIndex` (可选): 分页开始位置
- `keywordType` (可选): 主体类型枚举
- `pageSize` (可选): 分页结束位置

**返回值**:
- `total`: 总数
- `resultList`: 结果列表
  - `reason`: 处罚原因
  - `publishDate`: 公示日期
  - `result`: 处罚结果
  - `punishmentFileLink`: 行政处罚文件链接
  - `authority`: 决定机关
  - `content`: 行政处罚内容
  - `decisionDate`: 决定日期
  - `sources`: 数据来源
  - `type`: 违法行为类型
  - `id`: 决定书文号

### 9. risk_insight_business_anomalies
**功能**: 经营异常查询

查询企业的经营异常信息，包括异常数量及详细列表信息。

**参数**:
- `matchKeyword` (必需): 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举

**返回值**:
- `anomalyCount`: 经营异常数量
- `anomalyList`: 经营异常列表
  - `removeAuthority`: 移出决定机关
  - `createDate`: 列入日期
  - `removeDate`: 移出日期
  - `createReason`: 列入经营异常名录原因
  - `removeReason`: 移出经营异常名录原因
  - `createAuthority`: 列入决定机关

### 10. risk_insight_consumption_restrictions
**功能**: 限制高消费查询

查询特定企业或其负责人是否存在限制高消费的司法记录。

**参数**:
- `matchKeyword` (必需): 企业名称/注册号/统一社会信用代码/企业id
- `pageIndex` (可选): 页码
- `keywordType` (可选): 主体类型枚举
- `pageSize` (可选): 分页大小

**返回值**:
- `total`: 总数
- `resultList`: 列表结果
  - `efCaseCreateTime`: 立案时间
  - `efCaseNumber`: 案号
  - `efLimitedApplicant`: 申请人
  - `efExecutiveCourt`: 执行法院
  - `efLimitedPersonCasePublishTime`: 发布日期
  - `efLimitedPersonName`: 限制消费人员
  - `efLimitedPersonProvince`: 省份

## 使用场景

1. **金融贷款审批**: 银行或金融机构评估借款企业的合规风险
2. **企业尽职调查**: 投资者或合作伙伴获取目标企业的合规历史
3. **招聘背景调查**: 人力资源部门考察候选公司的背景和合法性
4. **监管合规**: 政府监管机构进行企业合规监督和处罚决策
5. **商业风险管理**: 企业在商业合作前进行风险评估
6. **法律尽职调查**: 律师事务所进行企业法律风险评估

## 使用注意事项

1. **企业全称要求**: 在调用需要企业全称的接口时，如果没有企业全称则先调取risk_insight_fuzzy_search接口获取企业全称
2. **数据时效性**: 风险信息会随时更新，建议定期查询获取最新状态
3. **综合评估**: 建议结合多个维度的风险信息进行综合评估
4. **法律合规**: 使用风险信息时需遵守相关法律法规和隐私保护要求

## 使用提问示例

### risk_insight_fuzzy_search (企业关键词模糊搜索)
1. 帮我查找包含"腾讯"关键词的企业信息
2. 搜索与"阿里"相关的企业列表
3. 查询名称中包含"字节跳动"的公司

### risk_insight_serious_violations (严重违法记录查询)
1. 查询腾讯科技有限公司的严重违法记录
2. 检查字节跳动是否有严重违法情况
3. 阿里巴巴集团的违法记录有哪些？

### risk_insight_chattel_mortgage (动产抵押信息查询)
1. 查询腾讯的动产抵押信息
2. 阿里巴巴是否有动产抵押记录？
3. 检查字节跳动的抵押担保情况

### risk_insight_court_hearings (法院开庭公告查询)
1. 查询腾讯相关的开庭公告信息
2. 阿里巴巴最近有哪些法院开庭公告？
3. 检查字节跳动的庭审信息

### risk_insight_litigation_risk_profile (诉讼风险画像查询)
1. 分析腾讯的整体诉讼风险情况
2. 阿里巴巴的法律风险画像如何？
3. 字节跳动的司法风险评估

### risk_insight_court_announcements (法院公告查询)
1. 查询腾讯在法院公告中的信息
2. 阿里巴巴有哪些法院公告记录？
3. 检查字节跳动的法院公告情况

### risk_insight_intellectual_property_pledge (知识产权出质查询)
1. 查询腾讯的知识产权出质情况
2. 阿里巴巴是否有知识产权质押？
3. 字节跳动的知识产权抵押信息

### risk_insight_tax_penalties (税务行政处罚查询)
1. 查询腾讯的税务处罚记录
2. 阿里巴巴是否有税务违法处罚？
3. 检查字节跳动的税务合规情况

### risk_insight_business_anomalies (经营异常查询)
1. 查询腾讯是否被列入经营异常名录
2. 阿里巴巴的经营异常情况如何？
3. 字节跳动有经营异常记录吗？

### risk_insight_consumption_restrictions (限制高消费查询)
1. 查询腾讯及其高管是否有限制消费令
2. 阿里巴巴的高管有限制高消费记录吗？
3. 检查字节跳动的限制消费情况 