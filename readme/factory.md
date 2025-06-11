# 工厂洞察服务

该服务提供制造业企业的生产能力分析，包括产能评估、生产设备、制造工艺、工厂分布等信息，帮助用户了解企业的制造实力。

## 主要功能

- 🔍 企业关键词模糊搜索
- 🏭 工厂概况信息查询
- 📊 工厂产品统计分析
- ⚙️ 工厂生产能力评估
- 🔧 工厂搜索筛选
- 📍 工厂地理分布分析

## 可用工具

### 1. factory_insight_fuzzy_search
**功能**: 企业关键词模糊查询

根据提供的企业名称、人名、品牌、产品、岗位等关键词模糊查询相关企业列表。

**参数**:
- `matchKeyword` (必需): 匹配关键词 - 查询各类信息包含匹配关键词的企业
- `pageIndex` (可选): 分页开始位置
- `pageSize` (可选): 分页结束位置 - 一页最多获取50条数据

**返回值**:
- `total`: 总数
- `resultList`: 结果列表，包含企业基本信息

### 2. factory_insight_factory_profile
**功能**: 工厂概况信息查询

根据企业标识信息提供该企业的工厂概况，包括风险评估和详细的工厂信息。

**参数**:
- `matchKeyword` (必需): 匹配关键词 - 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举 - name/nameId/regNumber/socialCreditCode

**返回值**:
- `nameId`: 企业ID
- `name`: 企业名称
- `foundTime`: 成立时间
- `factoryScale`: 工厂规模
- `factoryTypeList`: 工厂类型
- `monthlyProductionAmountValue`: 月产值
- `accountPeriodRisk`: 账期风险
- `factoryAddress`: 工厂地址
  - `province`: 省份
  - `city`: 城市
  - `district`: 地区
  - `value`: 地址
- `regCapital`: 注册资本
  - `coinType`: 币种
  - `value`: 金额

### 3. factory_insight_factory_product_stats
**功能**: 工厂产品统计分析

根据工厂主体名称，获取工厂的产品统计信息，包括服务品牌数量、主营产品数量、产品标签、产品类目统计等。

**参数**:
- `matchKeyword` (必需): 匹配关键词 - 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举 - name/nameId/regNumber/socialCreditCode

**返回值**:
- `serviceBrandCount`: 服务品牌数量
- `mainProductCount`: 主营产品数量
- `tagNames`: 产品标签
- `productCategoriesStatInfo`: 产品类目统计信息
  - `name`: 类目
  - `value`: 数量

### 4. factory_insight_factory_capabilities
**功能**: 工厂生产能力评估

查询指定企业的工厂生产实力和资质信息，包括生产线配置、人员配置、设备详情、质量管理及相关资质等。

**参数**:
- `matchKeyword` (必需): 匹配关键词 - 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举 - name/nameId/regNumber/socialCreditCode

**返回值**:
- `assemblyLine`: 生产流水线数量
- `monthlyProductionAmountValue`: 月产值
- `boarderStaffNumber`: 打版人数
- `inspectionStaffNumber`: 检验人数
- `inspectionGroup`: 检验小组
- `isSupportProofing`: 是否支持打样
- `companyTechnicList`: 工厂工艺
- `managementSystemCertification`: 管理体系认证
- `enterpriseCertification`: 生产质量认证
- `mainDeviceList`: 设备列表
  - `equipName`: 设备名称
  - `brand`: 设备品牌
  - `equipVersion`: 设备型号
  - `equipNum`: 设备数量
- `patentCertificateImageList`: 相关资质列表
  - `patentName`: 资质名称
  - `image`: 图片
  - `imageLink`: 图片链接

### 5. factory_insight_factory_search
**功能**: 工厂搜索筛选

根据用户输入的条件（如工厂名称、主营产品、产品名称以及地理位置）搜索符合条件的工厂信息。

**参数**:
- `matchKeyword` (必需): 匹配关键词 - 工厂名称/主营产品/产品名称
- `keywordType` (必需): 主体类型 - 综合搜索/工厂名称/主营产品/产品名称
- `pageIndex` (可选): 页码 - 从1开始
- `pageSize` (可选): 分页大小 - 一页最多获取10条
- `address` (可选): 地区 - 格式：[["省份","市"],["省份","市"]]

**返回值**:
- `total`: 总数 - 最大显示100001
- `resultList`: 列表结果
  - `nameId`: 企业id
  - `name`: 企业名称
  - `foundTime`: 成立日期
  - `mainProducts`: 主营产品
  - `regCapital`: 注册资本

## 使用场景

1. **供应商评估**: 评估制造商的生产能力和技术水平，筛选优质供应商
2. **投资分析**: 了解制造企业的生产实力和发展潜力，支持投资决策
3. **合作伙伴选择**: 寻找具备特定生产能力的合作伙伴，优化供应链布局
4. **竞争分析**: 分析竞争对手的制造优势和生产能力，制定竞争策略
5. **产业研究**: 研究特定行业的制造业分布和发展水平，把握市场趋势
6. **采购决策**: 评估工厂的产品质量和生产规模，优化采购决策
7. **风险评估**: 评估供应商的账期风险和生产稳定性

## 使用注意事项

1. **企业全称要求**: 在调用需要企业全称的接口时，如果没有企业全称则先调取factory_insight_fuzzy_search接口获取企业全称
2. **产能数据**: 产能数据可能为设计产能或实际产能，需注意区分和验证
3. **设备信息**: 设备信息的准确性取决于数据来源和更新频率，建议实地验证
4. **工艺保密**: 部分核心工艺信息可能不会完全公开，存在信息限制
5. **地区筛选**: 地区搜索需按照指定格式输入，支持多地区组合查询
6. **分页限制**: 工厂搜索一页最多返回10条记录，需合理设置分页参数

## 使用提问示例

### factory_insight_factory_profile (工厂概况信息查询)
3. 富士康的工厂规模如何？月产值是多少？
4. 比亚迪的工厂地址分布在哪些地区？注册资本是多少？
5. 华为的制造工厂类型有哪些？账期风险情况如何？

### factory_insight_factory_product_stats (工厂产品统计分析)
6. 富士康服务了多少个品牌？主营产品数量有多少？
7. 比亚迪的产品类目统计情况如何？产品标签有哪些？
8. 华为工厂的产品分类分布是怎样的？

### factory_insight_factory_capabilities (工厂生产能力评估)
9. 富士康有多少条生产流水线？主要设备都有哪些品牌？
10. 比亚迪的生产人员配置如何？检验团队规模有多大？
11. 华为的工厂工艺有哪些？管理体系认证情况如何？
12. 富士康是否支持打样？相关资质证书有哪些？

### factory_insight_factory_search (工厂搜索筛选)
13. 广东省有哪些电子制造工厂？注册资本都是多少？
14. 搜索一下主营"手机配件"的工厂，主要分布在哪些地区？
15. 浙江省的纺织工厂有哪些？成立时间都是什么时候？