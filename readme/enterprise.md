# 企业基础信息服务

该服务提供企业工商信息、企业简介、企业标签、企业业务、企业控股股东信息、企业对外投资信息、企业分支机构信息、企业主要人员信息等基础查询功能。

## 主要功能

- 🔍 企业关键词模糊搜索
- 🏢 企业基础信息查询
- 👥 企业控股股东信息
- 💰 企业对外投资信息
- 🏪 企业分支机构信息
- 👨‍💼 企业主要人员信息

## 可用工具

### 1. enterprise_get_keyword_search
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

### 2. enterprise_get_enterprise_base_info
**功能**: 查询企业基础信息

通过输入企业全称查询企业业务相关信息，识别该公司是做什么的。

**参数**:
- `keyword` (必需): 企业全称

**返回值**:
- `base_info`: 企业工商信息
- `desc`: 企业简介
- `business_info`: 企业业务
- `tag`: 企业标签

### 3. enterprise_get_enterprise_holder_info
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

### 4. enterprise_get_enterprise_invest_info
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

### 5. enterprise_get_enterprise_branch_info
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

### 6. enterprise_get_enterprise_main_person_info
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
3. **错误处理**: 所有接口都包含错误处理，查询失败时会返回相应的错误信息。

## 使用提问示例

### enterprise_get_keyword_search (企业关键词模糊搜索)
1. 帮我查找包含"探迹"关键词的企业信息
2. 搜索与"腾讯"相关的企业列表
3. 查询名称中包含"阿里巴巴"的公司

### enterprise_get_enterprise_base_info (企业基础信息查询)
1. 探迹科技是做什么的？
2. 腾讯科技有限公司的主营业务是什么？
3. 北京字节跳动科技有限公司的企业简介

### enterprise_get_enterprise_holder_info (企业控股股东信息)
1. 探迹科技有哪些股东？
2. 腾讯的控股股东都有谁？
3. 查询字节跳动的股权结构信息

### enterprise_get_enterprise_invest_info (企业对外投资信息)
1. 探迹科技对外投资了哪些企业？
2. 腾讯投资了哪些公司？
3. 阿里巴巴的投资组合有哪些？

### enterprise_get_enterprise_branch_info (企业分支机构信息)
1. 探迹科技有哪些分公司？
2. 腾讯在全国有哪些分支机构？
3. 华为的分公司分布情况

### enterprise_get_enterprise_main_person_info (企业主要人员信息)
1. 探迹科技的主要管理人员有哪些？
2. 腾讯的高管团队信息
3. 字节跳动的核心人员构成 