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

### 2. serious_violations
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

### 3. chattel_mortgage
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

### 4. dishonesty_executor
**功能**: 失信被执行人查询

查询企业或个人的失信被执行人记录，提供详细的执行信息和失信行为记录。

**参数**:
- `matchKeyword` (必需): 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举

**返回值**:
- `dishonestCount`: 失信被执行人数量
- `dishonestInfoList`: 失信被执行人列表
  - `caseNumber`: 案件编号
  - `courtName`: 执行法院
  - `executedPerson`: 被执行人姓名/名称
  - `province`: 省份
  - `caseCreateTime`: 立案时间
  - `publishDate`: 发布时间
  - `performance`: 履行情况
  - `regDate`: 做出执行依据单位
  - `duty`: 生效法律文书确定的义务

### 5. abnormal_operation
**功能**: 经营异常名录查询

查询企业被列入经营异常名录的记录，包括列入原因、列入日期、移除信息等。

**参数**:
- `matchKeyword` (必需): 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举

**返回值**:
- `abnormalCount`: 经营异常数量
- `abnormalInfoList`: 经营异常列表
  - `createAuthority`: 列入决定机关
  - `createDate`: 列入日期
  - `createReason`: 列入原因
  - `removeAuthority`: 移除决定机关
  - `removeDate`: 移除日期
  - `removeReason`: 移除原因

### 6. administrative_penalty
**功能**: 行政处罚信息查询

查询企业的行政处罚记录，包括处罚决定书文号、处罚事由、处罚结果等详细信息。

**参数**:
- `matchKeyword` (必需): 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举

**返回值**:
- `penaltyCount`: 行政处罚数量
- `penaltyInfoList`: 行政处罚列表
  - `penaltyAuthority`: 处罚决定机关
  - `penaltyNo`: 处罚决定书文号
  - `penaltyDate`: 处罚决定日期
  - `penaltyReason`: 行政处罚事由
  - `penaltyResult`: 行政处罚结果

## 使用场景

1. **金融贷款审批**: 银行或金融机构评估借款企业的合规风险
2. **企业尽职调查**: 投资者或合作伙伴获取目标企业的合规历史
3. **招聘背景调查**: 人力资源部门考察候选公司的背景和合法性
4. **监管合规**: 政府监管机构进行企业合规监督和处罚决策
5. **商业风险管理**: 企业在商业合作前进行风险评估
6. **法律尽职调查**: 律师事务所进行企业法律风险评估

## 使用注意事项

1. **企业全称要求**: 在调用需要企业全称的接口时，如果没有企业全称则先调取fuzzy_search接口获取企业全称
2. **数据时效性**: 风险信息会随时更新，建议定期查询获取最新状态
3. **综合评估**: 建议结合多个维度的风险信息进行综合评估
4. **法律合规**: 使用风险信息时需遵守相关法律法规和隐私保护要求 