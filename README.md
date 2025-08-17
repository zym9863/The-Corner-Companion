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
short_description: A gentle AI companion for emotional support and finding joy
---

# 🌸 心隅陪伴者 | Heart Corner Companion

**English** | [中文](README-zh.md)

*A gentle AI companion that provides emotional support and helps you discover joy in everyday moments*

## 📖 Overview

心隅陪伴者 (Heart Corner Companion) is a compassionate AI application designed to provide emotional support and help users find beauty in their daily lives. Built with Gradio, it offers a safe space for emotional expression and mindful appreciation of life's small pleasures.

## ✨ Features

### 💭 心情树洞 (Mood Diary)
A safe emotional space where you can:
- Share your worries, frustrations, or any emotions you're experiencing
- Receive gentle, empathetic responses without judgment
- Feel heard and understood in a supportive environment
- Process your feelings with a compassionate companion

### 😊 微笑提取器 (Smile Extractor)
Discover the beauty in everyday moments by:
- Sharing your daily experiences, no matter how ordinary
- Getting help to identify positive details you might have missed
- Learning to appreciate small joys and "micro-happiness"
- Developing a more mindful perspective on daily life

## 🚀 Getting Started

### Prerequisites
- Python 3.12 or higher
- Dependencies listed in `pyproject.toml`

### Installation

1. Clone this repository:
```bash
git clone https://github.com/zym9863/the-corner-companion.git
cd the-corner-companion
```

2. Install dependencies using uv (recommended):
```bash
uv sync
```

Or using pip:
```bash
pip install -r requirements.txt
```

### Running the Application

#### Local Development
```bash
python app.py
```

The application will be available at `http://localhost:7860`

#### Using the Main Module
```bash
python main.py
```

## 🛠️ Technical Details

### Architecture
- **Frontend**: Gradio web interface with custom CSS styling
- **Backend**: Python with Pollinations AI API integration
- **AI Model**: OpenAI model via Pollinations API
- **Language**: Primarily Chinese with English support

### Key Components
- `PollinationsAPI`: Handles text generation using the Pollinations AI service
- `HeartCornerCompanion`: Main application class managing both mood diary and smile extractor features
- Custom Gradio interface with responsive design and gentle color schemes

### API Integration
The application uses the Pollinations AI API for text generation, providing:
- Reliable AI responses for emotional support
- Contextual understanding for both mood support and joy discovery
- Fallback error handling for robust user experience

## 🎨 Design Philosophy

This application is built around the principles of:
- **Gentle Companionship**: Providing non-judgmental emotional support
- **Mindful Appreciation**: Helping users notice positive aspects of their daily lives
- **Safe Space**: Creating an environment where all emotions are valid and welcome
- **Cultural Sensitivity**: Designed with Chinese language and cultural context in mind

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests to improve the application.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with [Gradio](https://gradio.app/) for the web interface
- Powered by [Pollinations AI](https://pollinations.ai/) for text generation
- Inspired by the need for accessible emotional support tools

---

*💝 Remember: Your feelings are valid, and your existence is precious.*
