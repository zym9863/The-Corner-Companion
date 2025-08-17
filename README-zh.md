---
title: 心隅陪伴者 | Heart Corner Companion
emoji: 🌸
colorFrom: pink
colorTo: purple
sdk: gradio
sdk_version: 5.42.0
app_file: app.py
pinned: false
license: mit
short_description: 温柔的AI陪伴者，提供情感支持并帮助发现生活中的美好
---

# 🌸 心隅陪伴者

[English](README.md) | **中文**

*一个温柔的AI陪伴者，提供情感支持并帮助您发现日常生活中的美好时刻*

## 📖 概述

心隅陪伴者是一个富有同情心的AI应用程序，旨在提供情感支持并帮助用户发现日常生活中的美好。基于Gradio构建，为情感表达和对生活小确幸的用心感受提供了一个安全的空间。

## ✨ 功能特色

### 💭 心情树洞
一个安全的情感空间，您可以：
- 分享您的担忧、挫折或任何正在经历的情绪
- 获得温柔、富有同理心的回应，没有任何评判
- 在支持性的环境中感受到被倾听和理解
- 与富有同情心的陪伴者一起处理您的感受

### 😊 微笑提取器
通过以下方式发现日常时刻的美好：
- 分享您的日常经历，无论多么平凡
- 获得帮助识别您可能错过的积极细节
- 学会欣赏小小的快乐和"微幸福"
- 培养对日常生活更加用心的视角

## 🚀 快速开始

### 环境要求
- Python 3.12 或更高版本
- `pyproject.toml` 中列出的依赖项

### 安装

1. 克隆此仓库：
```bash
git clone https://github.com/zym9863/the-corner-companion.git
cd the-corner-companion
```

2. 使用 uv 安装依赖（推荐）：
```bash
uv sync
```

或使用 pip：
```bash
pip install -r requirements.txt
```

### 运行应用程序

#### 本地开发
```bash
python app.py
```

应用程序将在 `http://localhost:7860` 可用

#### 使用主模块
```bash
python main.py
```

## 🛠️ 技术细节

### 架构
- **前端**：带有自定义CSS样式的Gradio网页界面
- **后端**：Python与Pollinations AI API集成
- **AI模型**：通过Pollinations API使用OpenAI模型
- **语言**：主要支持中文，同时支持英文

### 核心组件
- `PollinationsAPI`：使用Pollinations AI服务处理文本生成
- `HeartCornerCompanion`：管理心情树洞和微笑提取器功能的主应用程序类
- 具有响应式设计和温柔色彩方案的自定义Gradio界面

### API集成
应用程序使用Pollinations AI API进行文本生成，提供：
- 可靠的AI情感支持回应
- 对情绪支持和快乐发现的上下文理解
- 稳健用户体验的错误处理机制

## 🎨 设计理念

此应用程序围绕以下原则构建：
- **温柔陪伴**：提供无评判的情感支持
- **用心感受**：帮助用户注意到日常生活的积极方面
- **安全空间**：创造一个所有情绪都被认可和欢迎的环境
- **文化敏感性**：考虑中文语言和文化背景而设计

## 🤝 贡献

欢迎贡献！请随时提交问题或拉取请求来改进应用程序。

## 📄 许可证

此项目采用MIT许可证 - 详情请参阅LICENSE文件。

## 🙏 致谢

- 使用 [Gradio](https://gradio.app/) 构建网页界面
- 由 [Pollinations AI](https://pollinations.ai/) 提供文本生成支持
- 受到对可访问情感支持工具需求的启发

---

*💝 请记住：您的感受是有效的，您的存在是珍贵的。*