# 楼宇大数据服务

该服务提供全面的楼宇和企业办公地址信息查询功能，包括企业办公地址详情、办公地址统计分析、楼宇信息查询等，帮助用户进行市场地理分布分析和企业地址布局了解。

## 主要功能

- 🔍 企业关键词模糊搜索
- 🏢 企业办公地址详情查询
- 📊 企业办公地址统计分析
- 🏙️ 楼宇信息查询

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

### 2. office_address_details
**功能**: 企业办公地址详情查询

根据特定的企业标识信息，查询和返回企业的办公地址相关数据，包括办公地址总数、每个城市的办公地址详细信息等。

**参数**:
- `matchKeyword` (必需): 企业名称/注册号/统一社会信用代码/企业id
- `address` (可选): 地区 - 支持筛选省/市，省市之间用英文逗号分隔，如："广东省,广州市"
- `pageIndex` (可选): 分页开始位置
- `keywordType` (可选): 主体类型枚举（name：企业名称，nameId：企业id等）
- `pageSize` (可选): 分页结束位置 - 一页最多获取10条数据

**返回值**:
- `officeAddress`: 地址信息
- `total`: 总数
- `officeSourceType`: 地址来源
- `officeSettleType`: 入驻方式（工商注册入驻，办公地址入驻）
- `resultList`: 列表结果
  - `estateName`: 所在楼宇
  - `estateId`: 楼宇id

### 3. office_address_stats
**功能**: 企业办公地址统计分析

根据特定的企业标识信息，查询和返回企业的办公地址相关数据，包括办公地址城市、每个城市的办公地址数量等。

**参数**:
- `matchKeyword` (必需): 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举

**返回值**:
- `officeCityStats`: 办公地址分布统计
  - `city`: 办公城市
  - `count`: 办公地址数量

### 4. building_query
**功能**: 楼宇信息查询

支持通过楼宇名称、楼宇类型等查询指定地区的全部楼盘信息，包括楼宇名称、楼宇别名、楼宇地址、楼宇类型、楼宇入驻企业数量等。

**参数**:
- `matchKeyword` (可选): 查询关键词 - 查询楼宇名称/楼宇别名包含关键词的楼盘
- `pageIndex` (可选): 分页开始位置
- `address` (可选): 地区 - 支持筛选省/市，省市之间用英文逗号分隔
- `pageSize` (可选): 分页结束位置 - 一页最多获取10条数据
- `estatePropertyType` (可选): 楼宇类型（写字楼，产业园，综合体，公寓酒店，展会中心）

**返回值**:
- `total`: 总数
- `resultList`: 结果列表
  - `estateName`: 楼宇名称
  - `estateId`: 楼宇id
  - `estateAliasName`: 楼宇别名
  - `estateAddress`: 楼宇地址
  - `estatePropertyType`: 楼宇类型
  - `estateEnterpriseCount`: 楼宇入驻企业数量

## 使用场景

1. **企业内部管理**: 了解企业办公地址布局，进行地址资源管理
2. **商业分析**: 市场地理分布分析，了解企业在各地的分布情况
3. **投资决策**: 分析特定区域的企业集中度，辅助投资选址
4. **房地产分析**: 了解楼宇入驻企业情况，评估商业地产价值
5. **政府规划**: 企业信息核实和决策辅助，了解区域企业分布
6. **竞争分析**: 了解竞争对手的地理布局和办公地址分布

## 使用注意事项

1. **企业全称要求**: 在调用需要企业全称的接口时，如果没有企业全称则先调取fuzzy_search接口获取企业全称
2. **分页限制**: 办公地址详情和楼宇查询一页最多获取10条数据
3. **地区筛选**: 支持按省市筛选，格式为"省份,城市"
4. **楼宇类型**: 支持按写字楼、产业园、综合体、公寓酒店、展会中心等类型筛选
5. **入驻方式**: 包括工商注册入驻和办公地址入驻两种类型 