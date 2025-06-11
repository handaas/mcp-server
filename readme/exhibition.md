# 展会大数据服务

该服务提供全面的展会信息查询功能，包括企业参展记录、展会场馆信息、展会搜索等，帮助用户了解企业的展会参与情况和行业展会信息。

## 主要功能

- 🔍 企业关键词模糊搜索
- 🏢 企业参展记录查询
- 🏛️ 展会场馆信息查询
- 📅 展会搜索

## 可用工具

### 1. exhibition_bigdata_fuzzy_search
**功能**: 企业关键词模糊查询

根据提供的企业名称、人名、品牌、产品、岗位等关键词模糊查询相关企业列表。

**参数**:
- `matchKeyword` (必需): 匹配关键词
- `pageIndex` (可选): 分页开始位置
- `pageSize` (可选): 分页结束位置

**返回值**:
- `total`: 总数
- `resultList`: 结果列表

### 2. exhibition_bigdata_exhibition_participation
**功能**: 企业参展记录查询

查询企业在展会中的参展信息，返回该企业参加展会的详细信息，包括展会的时间、描述、名称及展馆等。

**参数**:
- `matchKeyword` (必需): 企业名称/注册号/统一社会信用代码/企业id
- `pageIndex` (可选): 页码
- `pageSize` (可选): 分页大小 - 一页最多获取50条数据
- `keywordType` (可选): 主体类型枚举

**返回值**:
- `total`: 总数
- `resultList`: 参展记录列表
  - `fairEndTime`: 闭展时间
  - `fairLogo`: 展会logo
  - `fairDesc`: 展会描述
  - `fairPavilion`: 展馆名称
  - `fairName`: 展会名称
  - `isOpen`: 是否开展
  - `fairBeginTime`: 开展时间

### 3. exhibition_bigdata_exhibition_venue_search
**功能**: 展会场馆搜索

提供展会会馆的搜索服务，根据用户输入的省份和城市信息，返回符合条件的会馆列表及相关详细信息。

**参数**:
- `pavilionRegion` (必需): 会馆所在地区 - 格式："省份,城市"，如："福建省,厦门市"
- `matchKeyword` (可选): 匹配关键词
- `pageIndex` (可选): 页码 - 从1开始
- `pageSize` (可选): 分页大小 - 一页最多获取50条数据

**返回值**:
- `total`: 总数
- `resultList`: 场馆结果列表
  - `pavilionContact`: 联系方式（1：固定电话，2：邮箱，5：传真）
  - `pavilionDesc`: 会馆简介
  - `fairCount`: 展会数
  - `pavilionAddress`: 会展地址
  - `_id`: 会馆id
  - `pavilionHomepage`: 会馆官网链接
  - `pavilionLogo`: 会馆logo
  - `pavilionName`: 会馆名称
  - `pavilionScale`: 展览面积

### 4. exhibition_bigdata_exhibition_search
**功能**: 展会信息搜索

根据用户输入的查询关键词搜索展会信息，返回与关键词匹配的展会列表。

**参数**:
- `matchKeyword` (可选): 搜索关键词 - 搜索展会名称/展品范围包含关键词的展会
- `pageIndex` (可选): 页码
- `pageSize` (可选): 分页大小 - 一页最多获取50条数据

**返回值**:
- `resultList`: 展会列表结果
  - `_id`: 展会id
  - 其他展会详细信息

## 使用场景

1. **展会管理**: 展会组织者管理和查询企业参与的历史和即将举办的展会信息
2. **参展策略**: 企业跟踪参展活动和计划未来的参展策略
3. **数据分析**: 展会数据分析公司收集企业参展数据进行大数据分析
4. **商业情报**: 了解企业动态和市场趋势
5. **场地选择**: 会展组织者寻找合适的展会场所
6. **行程规划**: 商务人士计划展会行程时查询场地信息

## 使用注意事项

1. **企业全称要求**: 在调用需要企业全称的接口时，如果没有企业全称则先调取exhibition_bigdata_fuzzy_search接口获取企业全称
2. **分页限制**: 一页最多获取50条数据
3. **地区格式**: 场馆查询时地区格式为"省份,城市"
4. **联系方式类型**: 场馆联系方式类型编码（1：固定电话，2：邮箱，5：传真）
5. **时间信息**: 关注展会的开展和闭展时间信息

## 使用提问示例


### exhibition_bigdata_exhibition_participation (企业参展记录查询)
3. 华为参加过哪些重要的科技展会？展会时间都是什么时候？
4. 比亚迪的参展记录有多少？都在哪些展馆举办的？
5. 小米最近参加的展会有哪些？展会描述是什么？

### exhibition_bigdata_exhibition_venue_search (展会场馆搜索)
6. 上海有哪些大型会展中心？展览面积多大？
7. 北京的展会场馆都有哪些？联系方式是什么？
8. 深圳的会展场地情况如何？举办了多少场展会？

### exhibition_bigdata_exhibition_search (展会信息搜索)
9. 汽车行业相关的展会有哪些？
10. 科技类展会都有什么？展会详情如何？
11. 最近有哪些电子产品相关的展览？