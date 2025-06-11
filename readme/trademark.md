# 商标大数据服务

该服务提供全面的商标信息查询功能，包括商标搜索、商标概况统计等，帮助用户进行商标查询、情况分析和状态跟踪。

## 主要功能

- 🔍 企业关键词模糊搜索
- 📄 商标信息搜索
- 📊 企业商标概况统计
- 📈 商标统计分析

## 可用工具

### 1. trademark_bigdata_fuzzy_search
**功能**: 企业关键词模糊查询

根据提供的企业名称、人名、品牌、产品、岗位等关键词模糊查询相关企业列表。

**参数**:
- `matchKeyword` (必需): 匹配关键词 - 查询各类信息包含匹配关键词的企业
- `pageIndex` (可选): 分页开始位置
- `pageSize` (可选): 分页结束位置 - 一页最多获取50条数据

**返回值**:
- `total`: 总数
- `resultList`: 结果列表
- 其他企业相关信息

### 2. trademark_bigdata_trademark_search
**功能**: 商标信息搜索

根据商标名称、申请号、申请人名称或代理机构名称等条件进行查询，并通过商标状态进一步过滤结果。

**参数**:
- `matchKeyword` (必需): 匹配关键词 - 商标名称/申请号/申请人名称/代理机构名称
- `keywordType` (可选): 搜索方式 - 商标名称，申请号，申请人，代理机构，默认匹配全部
- `pageIndex` (可选): 页码 - 从1开始
- `pageSize` (可选): 分页大小 - 一页最多获取50条数据
- `tmStatus` (可选): 商标状态 - 驳回复审中，撤销/无效宣告申请审查中，初审公告等

**返回值**:
- `resultList`: 商标列表
  - `_id`: 商标id
  - `tmAgentName`: 代理机构名称
  - `tmAgentNameId`: 代理机构id
  - `tmCompanyNameId`: 申请人id
  - `tmName`: 商标名称
  - `tmImage`: 商标图片链接
  - `tmApplicationTime`: 申请日期
  - `tmCompanyName`: 申请人名称
  - `tmRegNum`: 申请号
  - `tmRegTime`: 注册日期
  - `tmServiceContents`: 商品服务项
  - `tmStatus`: 商标状态
  - `tmTrialTime`: 初审公告日期
- `total`: 商标数量

### 3. trademark_bigdata_trademark_profile
**功能**: 企业商标概况统计

根据输入的企业标识信息，返回与该企业相关的商标概况信息，包括商标总数、商标类别、商标状态列表等。

**参数**:
- `matchKeyword` (必需): 匹配关键词 - 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型 - name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码

**返回值**:
- `tmTypeList`: 涵盖商标类别
- `tmCount`: 商标数量
- `tmNumberThisYear`: 最近一年申请商标数
- `tmInvalidNumber`: 无效商标数
- `tmStatusList`: 商标状态列表
- `tmValidNumber`: 有效商标数
- `tmStatusStat`: 商标状态统计

### 4. trademark_bigdata_trademark_stats
**功能**: 企业商标统计分析

根据输入的企业相关信息，返回该企业的商标申请趋势、商标注册趋势、商标状态统计及商标类别统计等信息。

**参数**:
- `matchKeyword` (必需): 匹配关键词 - 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型 - name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码

**返回值**:
- `tmRegTimeStat`: 商标注册趋势
  - `year`: 年份
  - `count`: 商标数量
- `tmAppTimeStat`: 商标申请趋势
  - `year`: 年份
  - `count`: 商标数量
- `tmStatusStat`: 商标状态统计
  - `tmStatus`: 商标状态
  - `count`: 商标数量
- `tmTypeStats`: 商标类别统计
  - `tmName`: 商标类别
  - `count`: 商标数量

## 使用场景

1. **商标代理机构**: 查询竞争对手的商标布局情况
2. **企业品牌保护**: 监控自己的商标资产，评估品牌保护情况
3. **竞争对手分析**: 了解竞争对手的商标布局判断其市场策略
4. **法律咨询**: 进行商标查询、情况分析和状态跟踪
5. **市场研究**: 进行市场竞争分析和品牌研究

## 使用注意事项

1. **企业全称要求**: 在调用需要企业全称的接口时，如果没有企业全称则先调取trademark_bigdata_fuzzy_search接口获取企业全称
2. **分页限制**: 一页最多获取50条数据
3. **商标状态**: 支持按多种商标状态进行筛选查询
4. **搜索方式**: 支持精确匹配和模糊匹配多种搜索方式

## 使用提问示例

### trademark_bigdata_fuzzy_search (企业关键词模糊搜索)
1. 帮我查找包含"华为"关键词的企业信息
2. 搜索与"小米"相关的企业列表
3. 查询名称中包含"苹果"的公司

### trademark_bigdata_trademark_search (商标信息搜索)
1. 查询"华为"商标的详细信息
2. 搜索苹果公司申请的所有商标
3. 查找申请号为"80206640"的商标信息

### trademark_bigdata_trademark_profile (企业商标概况统计)
1. 华为技术有限公司的商标概况如何？
2. 查询腾讯科技的商标总数和分类情况
3. 阿里巴巴集团有多少个注册商标？

### trademark_bigdata_trademark_stats (企业商标统计分析)
1. 分析华为近几年的商标申请趋势
2. 查询苹果公司的商标注册趋势分析
3. 腾讯的商标类别分布统计情况 