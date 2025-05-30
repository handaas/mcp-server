# 门店大数据服务

该服务提供全面的线下门店信息查询功能，包括企业旗下门店分布、门店详细信息搜索、餐饮品牌门店统计等，帮助用户了解企业的线下业务布局。

## 主要功能

- 🔍 企业关键词模糊搜索
- 🏪 企业门店分布查询
- 🔍 线下门店信息搜索
- 📊 门店统计分析

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

### 2. company_restaurant_branches
**功能**: 企业餐饮门店分布查询

根据输入的企业信息查询该企业旗下餐饮品牌门店的详细信息，包括总数、品牌类别、城市和省份的门店分布等。

**参数**:
- `matchKeyword` (必需): 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举

**返回值**:
- `storeTotal`: 门店总数
- `storeList`: 门店数据列表
  - `brandClassification`: 品牌类别
  - `brandId`: 品牌id
  - `firstClassify`: 一级类别
  - `secondClassify`: 二级类别
  - `brandCradle`: 起源地
  - `brandImage`: 品牌图片
  - `brandName`: 品牌名称
  - `mallStoreNum`: 商场店数
  - `brandStoreCityStats`: 城市分布（前十条）
  - `brandStoreProvinceStats`: 省份分布（前十条）
  - `brandStoreNum`: 门店数

### 3. offline_store_search
**功能**: 线下门店信息搜索

通过输入店铺名称、类目、消费区间、店铺状态、地理位置等条件，返回符合条件的店铺信息列表。

**参数**:
- `ooStoreName` (可选): 店铺名称
- `ooStoreBrandList` (可选): 经营品牌 - 支持多选，英文分号分割
- `ooStoreCalClassification` (可选): 店铺分类 - 一级类目和二级类目采用英文逗号分隔
- `address` (可选): 地区 - 不可多选，英文逗号分割，格式："省份,城市,区域"
- `ooStoreStatus` (可选): 店铺状态 - 营业，尚未营业，暂停营业，歇业/关闭，关闭/下架
- `ooStoreAddressValue` (可选): 店铺地址
- `hasMobile` (可选): 有无手机号 - 1：有，0：无
- `hasPhone` (可选): 有无固话 - 1：有，0：无
- `pageSize` (可选): 分页大小 - 一页最多获取50条数据
- `ooMinStorePerCapitaConsumption` (可选): 人均消费最小值
- `ooMaxStorePerCapitaConsumption` (可选): 人均消费最大值
- `pageIndex` (可选): 页码 - 从1开始

**返回值**:
- `resultList`: 门店结果列表
  - `ooStoreId`: 店铺id
  - `hasContact`: 有无联系方式
  - `contactNumber`: 联系方式数量
  - `hasMobile`: 有无手机号
  - `hasPhone`: 有无固话
  - `ooStoreCalClassification`: 店铺分类
  - `ooStoreName`: 店铺名称
  - `ooStorePerCapitaConsumption`: 人均价格
  - `ooStoreRank`: 店铺排名
  - `ooStoreStatus`: 店铺状态
  - `ooStoreTradingArea`: 店铺所在商圈
- `total`: 总数

## 使用场景

1. **企业内部管理**: 了解企业旗下门店分布和经营状况
2. **商业分析**: 分析企业在线下市场的布局和品牌影响力
3. **竞争对手研究**: 了解竞争对手的门店分布和市场覆盖
4. **投资决策**: 评估企业的线下业务规模和发展潜力
5. **合作伙伴筛选**: 寻找符合条件的线下门店进行合作
6. **市场调研**: 分析特定区域的门店分布和竞争状况

## 使用注意事项

1. **企业全称要求**: 在调用需要企业全称的接口时，如果没有企业全称则先调取fuzzy_search接口获取企业全称
2. **分页限制**: 一页最多获取50条数据
3. **地区筛选**: 支持按省市区进行精确筛选
4. **消费筛选**: 支持按人均消费区间进行筛选
5. **联系方式**: 可以筛选有联系方式的门店，便于商务合作 