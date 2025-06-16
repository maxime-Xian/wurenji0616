# 无人机电机工厂投资规划网页

## 项目简介

这是一个专为无人机电机工厂投资规划设计的现代化网页项目。该网页采用响应式设计，完美适配桌面端和移动端设备，特别针对微信浏览器进行了优化。

## 项目特点

### 🎨 现代化设计
- 采用渐变背景和现代化UI设计
- 响应式布局，适配各种屏幕尺寸
- 优雅的动画效果和交互体验

### 📱 移动端优化
- 针对移动设备优化的字体大小和间距
- 微信浏览器兼容性优化
- 触摸友好的交互设计

### 💼 投资规划功能
- 详细的投资计划展示
- 市场分析和前景预测
- 财务规划和收益分析

## 文件结构

```
├── drone_motor_factory.html    # 主网页文件
├── mobile_access_guide.md      # 移动端访问指南
├── crawler.py                  # 网页爬虫工具
├── crawled_content.txt         # 爬取的内容
├── iframe_content.txt          # iframe内容
├── iframe_error.log           # 错误日志
├── page_screenshot.png        # 页面截图
├── page_source.html           # 页面源码
└── README.md                  # 项目说明文档
```

## 快速开始

### 本地访问

1. 启动本地HTTP服务器：
```bash
python3 -m http.server 8000
```

2. 在浏览器中访问：
```
http://localhost:8000/drone_motor_factory.html
```

### 移动端访问

#### 方法一：本地网络访问
1. 确保手机和电脑连接同一WiFi网络
2. 获取电脑IP地址（如：192.168.43.209）
3. 在手机浏览器中访问：
```
http://192.168.43.209:8000/drone_motor_factory.html
```

#### 方法二：GitHub Pages
1. 项目已部署到GitHub Pages
2. 访问：https://maxime-xian.github.io/wurenji0616/drone_motor_factory.html

更多移动端访问方法请参考 [移动端访问指南](mobile_access_guide.md)

## 技术栈

- **HTML5**: 语义化标记
- **CSS3**: 现代化样式和动画
- **JavaScript**: 交互功能
- **响应式设计**: 适配多种设备
- **Python**: 爬虫工具

## 浏览器兼容性

- ✅ Chrome (推荐)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ 微信内置浏览器
- ✅ 移动端浏览器

## 项目亮点

### 响应式设计
- 桌面端：1200px以上屏幕优化显示
- 平板端：768px-1199px适配
- 手机端：768px以下专门优化

### 微信优化
- 针对微信浏览器的特殊优化
- 解决微信环境下的兼容性问题
- 优化触摸交互体验

### 性能优化
- 轻量级代码结构
- 快速加载时间
- 优化的图片和资源

## 部署说明

### GitHub Pages部署
项目已自动部署到GitHub Pages，可直接访问在线版本。

### 自定义部署
1. 将项目文件上传到任何Web服务器
2. 确保服务器支持静态文件托管
3. 访问对应的URL即可

## 开发工具

项目包含一个Python爬虫工具 `crawler.py`，用于：
- 网页内容抓取
- 页面截图生成
- 内容分析和处理

## 贡献指南

欢迎提交Issue和Pull Request来改进项目！

## 许可证

MIT License

## 联系方式

如有问题或建议，请通过GitHub Issues联系。

---

**注意**: 本项目专为无人机电机工厂投资规划展示设计，包含详细的市场分析和投资建议。适合投资者、企业家和相关行业从业者参考使用。