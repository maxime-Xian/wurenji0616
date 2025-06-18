# 手机微信访问网页指南

## 当前状态
- ✅ 网页已优化移动端显示
- ✅ 添加了微信浏览器兼容性
- ✅ 响应式设计适配手机屏幕

## 访问方案

### 方案一：使用免费内网穿透工具

#### 1. 安装 ngrok（推荐）
```bash
# 下载并安装 ngrok
brew install ngrok/ngrok/ngrok
# 或访问 https://ngrok.com/ 下载

# 启动内网穿透
ngrok http 8000
```

#### 2. 使用 localtunnel
```bash
# 安装
npm install -g localtunnel

# 启动
lt --port 8000
```

#### 3. 使用 serveo
```bash
# 无需安装，直接使用
ssh -R 80:localhost:8000 serveo.net
```

### 方案二：部署到免费托管平台

#### GitHub Pages
1. 将文件上传到 GitHub 仓库
2. 启用 GitHub Pages
3. 获得 `https://username.github.io/repository` 链接

#### Netlify Drop
1. 访问 https://app.netlify.com/drop
2. 直接拖拽 HTML 文件
3. 获得临时访问链接

#### Vercel
1. 访问 https://vercel.com
2. 导入项目或拖拽文件
3. 获得永久访问链接

### 方案三：局域网访问
如果手机和电脑在同一WiFi网络：
1. 查看电脑IP地址：`ifconfig | grep inet`
2. 手机访问：`http://电脑IP:8000/drone_motor_factory.html`

## 移动端优化特性
- 🔧 禁用缩放，防止误操作
- 📱 响应式布局适配各种屏幕
- 🎨 优化字体大小和间距
- 🚀 微信浏览器兼容性优化
- 🎯 触摸友好的交互设计

## 使用建议
1. **临时分享**：使用 ngrok 或 localtunnel
2. **长期使用**：部署到 GitHub Pages 或 Vercel
3. **内部演示**：使用局域网访问

## 注意事项
- 免费内网穿透工具通常有时间限制
- 部署到公共平台时注意数据安全
- 微信可能会缓存页面，清除缓存后重新访问