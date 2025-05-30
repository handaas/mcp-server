# 招投标大数据服务

该服务提供全面的招投标信息查询功能，包括企业招投标记录、中标统计、招标分析、采购信息、拟建项目等，帮助用户了解企业的招投标情况和发现商业机会。

## 主要功能

- 🔍 企业关键词模糊搜索
- 📋 招投标信息查询
- 🏆 中标统计分析
- 📊 招标统计分析
- 🛒 采购统计分析
- 🔍 招投标公告搜索
- 🏗️ 拟建项目查询

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

### 2. bidding_info
**功能**: 企业招投标信息查询

根据输入的企业标识符查询并返回该企业参与的招投标信息，包括招投标公告类型、项目地区、公告详情等。

**参数**:
- `matchKeyword` (必需): 企业名称/注册号/统一社会信用代码/企业id
- `pageSize` (可选): 分页大小 - 一页最多获取50条数据
- `keywordType` (可选): 主体类型枚举
- `pageIndex` (可选): 页码 - 从1开始

**返回值**:
- `total`: 总数
- `resultList`: 招投标记录列表
  - `biddingId`: 招投标Id
  - `infoType`: 招投标公告类型
  - `projectRegion`: 项目地区
  - `publishDate`: 公告发布时间
  - `subjectMatterList`: 标的物
  - `title`: 公告标题
  - `role`: 招投标角色（招标，中标）
  - `projectAmount`: 项目金额
  - `winningBidderList`: 中标企业列表
  - `purchasingBidderList`: 招标企业列表

### 3. bid_win_stats
**功能**: 中标统计分析

根据企业信息获取企业中标信息统计项，包括标的分布、金额分布、区域分布及中标趋势等。

**参数**:
- `matchKeyword` (必需): 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举

**返回值**:
- `winbidAmountStatList`: 中标金额分布
  - `range`: 金额范围
  - `percent`: 比例
  - `count`: 数量
- `winbidAreaStat`: 区域分布
  - `area`: 区域
- `winbidStatList`: 中标标的分布
  - `count`: 数量
  - `percent`: 比例
  - `subjectMatter`: 标的物
- `winbidTrend`: 中标趋势
  - `count`: 数量
  - `year`: 年份

### 4. tender_stats
**功能**: 招标统计分析

根据企业信息获取企业招标信息统计项，包括标的分布、金额分布、区域分布及招标趋势等。

**参数**:
- `matchKeyword` (必需): 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举

**返回值**:
- `tenderAmountStatList`: 招标金额分布
  - `range`: 金额范围
  - `percent`: 比例
  - `count`: 数量
- `tenderAreaStat`: 区域分布
  - `area`: 区域
  - `count`: 数量
- `tenderStatList`: 招标标的分布
  - `count`: 数量
  - `percent`: 比例
  - `subjectMatter`: 标的物
- `tenderTrend`: 招标趋势
  - `count`: 数量
  - `year`: 年份

### 5. procurement_stats
**功能**: 采购统计分析

根据企业名称或ID，获取企业采购统计信息，包括采购产品分布、采购区域分布等。

**参数**:
- `matchKeyword` (必需): 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举

**返回值**:
- `purchasingProductStatList`: 采购产品分布
  - `count`: 采购数量
  - `percent`: 占比
  - `product`: 产品名称
- `purchasingAreaStatList`: 采购区域分布
  - `times`: 客户数
  - `area`: 地区

### 6. bid_search
**功能**: 招投标公告搜索

通过提供多种过滤条件查询和筛选招投标信息，返回符合条件的招投标公告详细信息。

**参数**:
- `matchKeyword` (可选): 搜索关键词
- `biddingType` (可选): 信息类型 - 招标预告，招标公告，变更补充，中标公告，采购意向，废标终止
- `biddingRegion` (可选): 项目地区 - 多选，支持省份、城市
- `biddingAnncPubStartTime` (可选): 发布开始日期 - 格式："2024-08-01"
- `biddingAnncPubEndTime` (可选): 发布结束日期 - 格式："2024-11-01"
- `searchMode` (可选): 搜索模式 - 标题匹配，标的物匹配，全文匹配
- `biddingProjectMaxAmount` (可选): 项目金额最大值（万元）
- `biddingPurchasingType` (可选): 招标单位类型 - 政府，学校，医院，公安，部队，企业
- `biddingProjectMinAmount` (可选): 项目金额最小值（万元）
- `pageIndex` (可选): 分页索引
- `pageSize` (可选): 分页大小 - 一页最多获取50条

**返回值**:
- `total`: 总数
- `resultList`: 招投标公告列表
  - `biddingId`: 公告id
  - `biddingAnncTitle`: 公告标题
  - `biddingContent`: 正文
  - `biddingInfoType`: 公告类型
  - `biddingProjectType`: 项目类型
  - `biddingPublishTime`: 公告时间
  - `biddingEndTime`: 招标截止时间
  - `biddingProjectID`: 项目编号
  - `biddingAgentInfoList`: 招标代理机构信息
  - `biddingPurchasingInfoList`: 招标单位信息
  - `biddingWinningInfoList`: 中标单位信息
  - `biddingRegion`: 招投标所属地区
  - `hasFile`: 有无附件

### 7. planned_projects
**功能**: 拟建项目查询

查询企业拟建公告的信息，提供通过企业名称等多种方式检索拟建项目的相关详情。

**参数**:
- `matchKeyword` (必需): 企业名称/注册号/统一社会信用代码/企业id
- `pageIndex` (可选): 页码 - 从1开始
- `pageSize` (可选): 分页大小 - 一页最多获取50条数据
- `keywordType` (可选): 主体类型枚举

**返回值**:
- `total`: 总数
- `resultList`: 拟建项目列表
  - `ppId`: 项目id
  - `deviceList`: 待采设备
  - `ppRegion`: 建设地点
  - `ppTitle`: 项目名称
  - `ppContent`: 项目内容
  - `ppPublishTime`: 发布时间
  - `ppApprovalTime`: 评审时间

## 使用场景

1. **商业机会发现**: 查找相关行业的招标机会，发现新的业务机会
2. **竞争对手分析**: 了解竞争对手的中标情况和业务范围
3. **企业能力评估**: 通过中标记录评估企业实力和专业能力
4. **市场研究**: 分析特定行业的招投标趋势和市场动向
5. **合作伙伴筛选**: 根据中标记录选择优质的合作伙伴
6. **供应链分析**: 了解企业的采购习惯和供应商网络
7. **项目跟踪**: 跟踪企业的拟建项目和发展规划

## 使用注意事项

1. **企业全称要求**: 在调用需要企业全称的接口时，如果没有企业全称则先调取fuzzy_search接口获取企业全称
2. **分页限制**: 支持分页查询，一页最多获取50条数据，提高查询效率
3. **时间范围**: 支持按时间范围筛选招投标信息，注意日期格式
4. **地区筛选**: 支持按地区筛选招投标项目，可多选省份和城市
5. **金额单位**: 项目金额单位为万元，注意数值范围设置
6. **数据时效性**: 招投标信息更新及时，建议关注最新公告 