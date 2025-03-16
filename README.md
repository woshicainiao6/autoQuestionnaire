# AutoQuestionnaire

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/woshicainiao6/autoQuestionnaire/releases/tag/v1.0.0)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/woshicainiao6/autoQuestionnaire/blob/master/LICENSE)

自动问卷填写工具，基于Python实现的自动化问卷填写系统。

## 版本说明 (v1.0.0)

这是 AutoQuestionnaire 的首个正式发布版本，提供了以下核心功能：

- ✨ 多线程并发问卷填写
- 🔒 代理IP池支持
- 🤖 AI智能答案生成
- 📝 支持多种题型自动填写
- 🛡️ 完善的错误处理机制
- 📊 实时进度显示

### 支持的题型
- 单选题
- 多选题
- 填空题
- 下拉菜单
- 矩阵量表题
- 排序题
- 时间选择题

### 更新日期
2024-03-16

## 项目简介

AutoQuestionnaire 是一个强大的自动化问卷填写工具，使用Python开发，支持多线程并发执行，可以高效地完成大量问卷的自动填写任务。该工具主要用于问卷测试。

## 主要特性

- 多线程并发执行，提高填写效率
- 支持代理IP池，避免IP限制
- 可配置的填写参数
- 智能随机答案生成
- 异常处理机制
- 实时进度显示
- 支持多种题型自动填写：
  - 单选题
  - 多选题
  - 填空题
  - 下拉菜单
  - 矩阵量表题
  - 排序题
  - 时间选择题

## 技术栈

- Python 3.x
- Selenium WebDriver
- Chrome浏览器
- 多线程处理
- OpenAI API（用于智能答案生成）

## 目录结构

```
autoQuestionnaire/
├── main.py                 # 主程序入口
├── static/                 # 静态配置文件
│   └── configuration.py    # 配置参数
├── mainCode/              # 核心代码
├── openAi/                # AI相关功能
├── differentQuestion/     # 不同问题类型处理
├── randomChoice/         # 随机选择逻辑
└── proxy/                # 代理相关功能
```

## 详细安装说明

### 1. 环境要求

- Python 3.10 或更高版本
- Google Chrome 浏览器
- 稳定的网络连接

### 2. 克隆项目

```bash
git clone [repository-url]
cd autoQuestionnaire
```

### 3. 安装Python依赖

```bash
pip install -r requirements.txt
```

所需的主要依赖包括：
- selenium>=4.16.0：用于浏览器自动化
- requests>=2.31.0：用于HTTP请求
- openai>=1.12.0：用于AI答案生成
- webdriver-manager>=4.0.1：用于管理ChromeDriver

### 4. 配置Chrome浏览器和WebDriver

#### Windows系统：

1. 安装Chrome浏览器：
   - 访问 [Chrome官网](https://www.google.com/chrome/) 下载并安装最新版本

2. 安装ChromeDriver：
   - 访问 [ChromeDriver下载页面](https://chromedriver.chromium.org/downloads)
   - 下载与您的Chrome浏览器版本匹配的ChromeDriver
   - 将ChromeDriver解压到系统PATH环境变量包含的任意目录中
   - 或者将ChromeDriver放在项目根目录下

#### Linux系统：

1. 安装Chrome浏览器：
```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get install -f
```

2. 安装ChromeDriver：
```bash
CHROME_VERSION=$(google-chrome --version | cut -d " " -f3 | cut -d "." -f1)
wget https://chromedriver.storage.googleapis.com/LATEST_RELEASE_${CHROME_VERSION}
wget https://chromedriver.storage.googleapis.com/$(cat LATEST_RELEASE_${CHROME_VERSION})/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/local/bin/
```

#### MacOS系统：

1. 使用Homebrew安装Chrome浏览器：
```bash
brew install --cask google-chrome
```

2. 安装ChromeDriver：
```bash
brew install chromedriver
```

## 配置说明

在 `static/configuration.py` 中配置以下参数：

```python
# API密钥配置
api_key = "your-api-key"  # OpenAI API密钥

# 问卷配置
questionAire_url = "https://www.example.com/survey"  # 目标问卷URL
questionAire_num = 500  # 需要填写的问卷数量

# 执行配置
max_threads = 5  # 最大并发线程数
wait_time = 5  # 基础等待时间（秒）
open_Browser = False  # 是否显示浏览器界面

# 代理配置（可选）
proxypool_url = 'your-proxy-pool-url'  # 代理池API地址
```

## 使用方法

1. 配置参数：
   - 在 `static/configuration.py` 中设置目标问卷URL和填写数量
   - 配置API密钥（如果需要使用AI生成答案）
   - 配置代理池（如果需要使用代理）

2. 运行程序：
```bash
python main.py
```

3. 监控进度：
   - 程序会实时显示填写进度
   - 可以在控制台查看完成情况

## 注意事项

1. 请确保遵守目标网站的使用条款和政策
2. 建议合理设置并发数和填写间隔
3. 使用代理IP时需确保代理的可用性
4. 建议在测试环境下先进行小规模测试
5. 定期更新ChromeDriver以匹配Chrome浏览器版本
6. 确保系统防火墙不会阻止程序的网络访问
7. 使用代理时注意IP质量和访问频率限制

## 错误处理

程序包含完善的错误处理机制：
- 线程异常捕获
- 网络连接错误处理
- 浏览器操作超时处理
- 自动重试机制

## 常见问题解决

1. ChromeDriver版本不匹配：
   - 确保ChromeDriver版本与Chrome浏览器版本相匹配
   - 可以使用webdriver-manager自动管理版本

2. 网络连接问题：
   - 检查网络连接
   - 确认代理服务器是否可用
   - 适当增加等待时间

3. 元素定位失败：
   - 检查页面结构是否发生变化
   - 增加等待时间
   - 使用更可靠的元素定位方式

## 贡献指南

欢迎提交问题和改进建议，您可以：
1. 提交Issue
2. 创建Pull Request
3. 联系项目维护者

## 许可证

MIT License

Copyright (c) 2025 LutongZhang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## 联系方式

如果您有任何问题或建议，欢迎通过以下方式联系我们：

- Email 1: 1609213626@qq.com
- Email 2: zhanglutong6518@163.com