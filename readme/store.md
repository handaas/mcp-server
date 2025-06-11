# 门店大数据服务

该服务提供全面的线下门店信息查询功能，包括企业餐饮品牌门店查询、线下店铺搜索、餐饮品牌门店统计等，帮助用户进行门店分析和品牌研究。

## 主要功能

- 🔍 企业关键词模糊搜索
- 🍽️ 企业餐饮品牌门店查询
- 🏪 线下店铺信息搜索
- 📊 餐饮品牌门店统计

## 可用工具

### 1. store_bigdata_fuzzy_search
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

### 2. store_bigdata_company_restaurant_branches
**功能**: 企业餐饮品牌门店查询

根据输入的企业信息查询并返回该企业旗下餐饮品牌门店的详细信息，包括总数、品牌类别、城市和省份的门店分布等。

**参数**:
- `matchKeyword` (必需): 匹配关键词 - 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型 - name：企业名称，nameId：企业id，regNumber：注册号，socialCreditCode：统一社会信用代码

**返回值**:
- `storeTotal`: 总数
- `storeList`: 数据列表
  - `brandClassification`: 品牌类别
    - `brandId`: 品牌id
    - `firstClassify`: 一级类别
    - `secondClassify`: 二级类别
  - `brandCradle`: 起源地
  - `brandImage`: 品牌图片
  - `brandName`: 品牌名称
  - `mallStoreNum`: 商场店数
  - `brandStoreCityStats`: 城市分布 - 只返回前十条数据
    - `count`: 门店数量
    - `city`: 城市
  - `brandStoreProvinceStats`: 省份分布 - 只返回前十条数据
    - `count`: 门店数量
    - `province`: 省份
  - `brandStoreNum`: 门店数

### 3. store_bigdata_offline_store_search
**功能**: 线下店铺信息搜索

提供线下店铺的搜索功能，通过输入店铺名称、类目、消费区间、店铺状态、地理位置等条件，返回符合条件的店铺信息列表。

**参数**:
- `ooStoreName` (可选): 店铺名称
- `ooStoreBrandList` (可选): 经营品牌 - 支持多选，英文分号分割
- `ooStoreCalClassification` (可选): 店铺分类 - 支持多选
- `address` (可选): 地区 - 不可多选，英文逗号分割
- `ooStoreStatus` (可选): 店铺状态 - 营业，尚未营业，暂停营业，歇业/关闭，关闭/下架
- `ooStoreAddressValue` (可选): 店铺地址
- `hasMobile` (可选): 有无手机号 - 1：有，0：无
- `hasPhone` (可选): 有无固话 - 1：有，0：无
- `pageSize` (可选): 分页大小 - 一页最多获取50条数据
- `ooMinStorePerCapitaConsumption` (可选): 人均消费最小值
- `ooMaxStorePerCapitaConsumption` (可选): 人均消费最大值
- `pageIndex` (可选): 页码 - 从1开始

**返回值**:
- `total`: 总数
- `resultList`: 结果列表
  - `ooStoreId`: 店铺id
  - `hasContact`: 有无联系方式 - 1：有，0：无
  - `contactNumber`: 联系方式数量
  - `hasMobile`: 有无手机号 - 1：有，0：无
  - `hasPhone`: 有无固话 - 1：有，0：无
  - `ooStoreCalClassification`: 店铺分类
  - `ooStoreName`: 店铺名称
  - `ooStorePerCapitaConsumption`: 人均价格
  - `ooStoreRank`: 店铺排名
  - `ooStoreStatus`: 店铺状态
  - `ooStoreTradingArea`: 店铺所在商圈

### 4. store_bigdata_restaurant_branch_stats
**功能**: 餐饮品牌门店统计

根据品牌ID获取特定餐饮品牌在各城市及省份的门店分布情况，包括各城市和省份的门店数量统计。

**参数**:
- `matchKeyword` (必需): 品牌id - 字段来源企业旗下餐饮品牌门店
- `pageIndex` (可选): 页码 - 从1开始
- `pageSize` (可选): 分页大小 - 一页最多获取50条数据

**返回值**:
- `cityStatsTotal`: 城市分布数量
- `cityStatsList`: 城市分布列表
  - `count`: 门店数量
  - `city`: 城市
- `provinceStatsList`: 省份分布列表 - 返回全部数据
  - `province`: 省份
  - `count`: 门店数量
- `provinceStatsTotal`: 省份分布数量

## 使用场景

1. **餐饮企业管理**: 了解企业旗下品牌门店分布和经营状况
2. **市场分析**: 分析特定区域的餐饮市场分布和竞争情况
3. **选址决策**: 通过门店分布数据辅助新店选址决策
4. **品牌研究**: 研究餐饮品牌的市场覆盖和发展策略
5. **竞争分析**: 了解竞争对手的门店布局和市场策略
6. **消费者研究**: 分析不同区域的消费水平和偏好

## 使用注意事项

1. **企业全称要求**: 在调用需要企业全称的接口时，如果没有企业全称则先调取store_bigdata_fuzzy_search接口获取企业全称
2. **分页限制**: 不同接口的分页限制有所不同，请注意参数说明
3. **地区筛选**: 支持按省市区域进行筛选，注意格式要求
4. **品牌分类**: 支持按餐饮品牌类别进行筛选查询
5. **数据覆盖**: 主要覆盖餐饮类品牌门店，其他行业覆盖有限

## 使用提问示例

### store_bigdata_fuzzy_search (企业关键词模糊搜索)
1. 帮我查找包含"海底捞"关键词的企业信息
2. 搜索与"星巴克"相关的企业列表
3. 查询名称中包含"麦当劳"的公司

### store_bigdata_company_restaurant_branches (企业餐饮品牌门店查询)
1. 查询海底捞国际控股有限公司的餐饮门店分布
2. 星巴克在中国有哪些门店品牌？
3. 麦当劳的门店城市分布情况

### store_bigdata_offline_store_search (线下店铺信息搜索)
1. 搜索北京地区的火锅店信息
2. 查找上海市人均消费100-200元的餐厅
3. 搜索广州天河区营业中的咖啡店

### store_bigdata_restaurant_branch_stats (餐饮品牌门店统计)
1. 统计海底捞品牌在各个城市的门店数量
2. 星巴克在各个省份的门店分布统计
3. 分析肯德基的门店地理分布情况 