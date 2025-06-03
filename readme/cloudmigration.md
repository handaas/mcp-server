# 云迁移服务

该服务提供上云资产相关服务信息，包括云服务使用情况、技术栈分析、云迁移方案等功能，帮助用户了解企业的上云使用情况。

## 主要功能

- 🔍 企业关键词模糊搜索
- ☁️ 上云资产分析
- 🌐 域名信息查询
- 📊 云服务使用评估
- 📈 上云资产分布

## 可用工具

### 1. fuzzy_search
**功能**: 企业关键词模糊查询

根据提供的企业名称、人名、品牌、产品、岗位等关键词模糊查询相关企业列表。

**参数**:
- `matchKeyword` (必需): 匹配关键词 - 查询各类信息包含匹配关键词的企业
- `pageIndex` (可选): 分页开始位置
- `pageSize` (可选): 分页结束位置 - 一页最多获取50条数据

**返回值**:
- `total`: 总数
- `resultList`: 结果列表，包含企业基本信息

### 2. cloud_assets
**功能**: 云上资产分析

查询企业的云上资产信息，输出企业在云上的各种资产状况及特征信息，如有效域名、云服务厂商及云用量等。

**参数**:
- `matchKeyword` (必需): 匹配关键词 - 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举 - name/nameId/regNumber/socialCreditCode

**返回值**:
- `effectiveSubDomainNum`: 有效域名数量
- `subDomainNum`: 子域名数量
- `effectiveSubDomainList`: 有效域名列表
- `subDomainList`: 子域名列表
- `cloudServerList`: 云服务厂商列表
- `cloudConsumptionScale`: 上云资产等级
- `cloudServerNumInterval`: 云用量范围
- `cloudServiceProviderRatio`: 云服务厂商比例
  - `cloudService`: 云服务商名称
  - `ratio`: 云服务厂商比例
- `hasOverseasCloudService`: 有无海外服务器（0:无 1：有）
- `hasCdn`: 有无使用CDN（0:无 1：有）
- `cdnServerNum`: CDN使用规模
- `cdnServerList`: CDN服务商列表
- `hasIDC`: 有无使用IDC（0:无 1：有）
- `hasCloudStorage`: 有无使用云存储（0:无 1：有）

### 3. domain_info
**功能**: 域名信息查询

根据企业标识信息查询与该企业相关的所有已注册的域名信息，包括域名名称、对应网址、审核时间等详情。

**参数**:
- `matchKeyword` (必需): 匹配关键词 - 企业名称/注册号/统一社会信用代码/企业id
- `keywordType` (可选): 主体类型枚举 - name/nameId/regNumber/socialCreditCode
- `pageIndex` (可选): 页码
- `pageSize` (可选): 分页大小 - 一页最多获取50条数据

**返回值**:
- `total`: 总数
- `resultList`: 列表结果
  - `domainName`: 域名名称
  - `domainUrl`: 网址
  - `websiteRecord`: 网站备案号
  - `filingAuditTime`: 审核时间
  - `isHomePage`: 是否官网

## 使用场景

1. **云迁移规划**: 企业制定云迁移策略和技术选型，评估现有云资产
2. **技术选型**: 了解行业内企业的云技术使用情况，制定技术路线
3. **竞争分析**: 分析竞争对手的云计算应用水平和技术架构
4. **投资决策**: 评估企业的数字化转型程度和云化水平
5. **成本优化**: 参考同行企业的云计算成本控制经验和资源配置
6. **品牌保护**: 监控企业域名资产，防范品牌侵权和域名抢注
7. **合规审查**: 进行域名备案审查和网站合规性检查

## 使用注意事项

1. **企业全称要求**: 在调用需要企业全称的接口时，如果没有企业全称则先调取fuzzy_search接口获取企业全称
2. **技术保密**: 部分核心技术信息可能不会完全公开，存在信息限制
3. **成本数据**: 成本数据可能为估算值，仅供参考，建议结合实际情况分析
4. **技术更新**: 云技术发展迅速，需关注数据的时效性和技术演进
5. **域名验证**: 域名信息需要验证其真实性和有效性，避免误判
6. **资产评估**: 云资产等级评估基于多项指标，需综合分析 