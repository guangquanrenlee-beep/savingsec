# ProductPick - 商品评测与优惠聚合平台

一个基于 Hugo 的以商品为核心的内容电商网站，用于联盟营销（Affiliate Marketing）。

## 特性

- **SEO 优化**: Schema.org JSON-LD 结构化数据、语义化 HTML、Open Graph、Twitter Cards
- **GEO 优化**: 针对 ChatGPT/Perplexity/Google SGE 的内容结构设计
- **EEAT 信号**: 作者信息、最后更新时间、验证状态、专业内容结构
- **主题集群**: 商品 → 优惠券 → 评测 → 文章的内链网络
- **快速加载**: Hugo SSG + Tailwind CSS + Cloudflare CDN
- **站内搜索**: Pagefind 客户端搜索
- **一键复制**: 优惠码一键复制功能

## 快速开始

### 环境要求

- Hugo >= 0.120.0
- Node.js >= 18

### 开发模式

```bash
# 安装依赖
npm install

# 编译 Tailwind CSS
npm run build

# 启动开发服务器
hugo server

# 生产构建
hugo --minify
```

## 项目结构

```
chanpintuijian/
├── content/
│   ├── product/     # 商品页面（核心SEO入口）
│   ├── coupon/      # 优惠券
│   ├── deal/        # 促销活动
│   ├── review/      # 评测文章
│   └── blog/        # 购买指南/SEO长文
├── layouts/
│   ├── product/     # 商品页模板
│   ├── coupon/      # 优惠券页模板
│   ├── deal/        # 促销页模板
│   ├── review/      # 评测页模板
│   ├── blog/        # 博客页模板
│   ├── brand/       # 品牌聚合页
│   ├── category/    # 分类页
│   └── partials/    # 可复用组件
├── archetypes/      # 内容模板
├── static/          # 静态资源
└── assets/css/      # Tailwind CSS 源码
```

## URL 结构

| 路径 | 说明 |
|------|------|
| /product/{slug}/ | 商品页（核心SEO入口） |
| /coupon/{slug}/ | 优惠券页 |
| /deal/{slug}/ | 促销页 |
| /review/{slug}/ | 评测页 |
| /brand/{brand}/ | 品牌聚合页 |
| /category/{category}/ | 分类页 |
| /blog/{article}/ | 文章页 |

## 内容维护

### 添加商品

```bash
hugo new product/your-product-name.md
```

编辑 frontmatter 字段：

| 字段 | 说明 |
|------|------|
| title | 商品名称 |
| brand | 品牌 |
| category | 分类数组 |
| rating | 评分 (1-5) |
| price | 当前价格 |
| original_price | 原价 |
| affiliate_link | 联盟营销链接 |
| pros | 优点列表 |
| cons | 缺点列表 |
| faq | 常见问题 (question/answer) |

### 批量生成内容

可以使用 Python 脚本批量生成 Markdown 文件，配合爬虫或 API 自动填充内容。

## 部署

### Cloudflare Pages

项目已配置 GitHub Actions 自动部署到 Cloudflare Pages。

需要设置以下 Secrets：
- `CLOUDFLARE_API_TOKEN`
- `CLOUDFLARE_ACCOUNT_ID`

### 手动部署

```bash
hugo --minify
npx pagefind --site public
# 上传 public/ 目录到你的托管服务
```

## SEO 优化

- 每个页面自动生成 JSON-LD（Product/Article/FAQ/Breadcrumb）
- 语义化 HTML 结构（H1-H3 层级清晰）
- 内部链接网络（Topic Cluster）
- 干净的 URL 结构 `/product/{slug}/`
- Core Web Vitals 友好

## AI 搜索优化（GEO）

- last_updated 时间信号
- verified 验证状态
- 结构化数据（JSON-LD）
- 自然语言 FAQ
- Entity 统一命名

## License

MIT
