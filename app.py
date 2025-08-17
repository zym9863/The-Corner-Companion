import gradio as gr
import requests
import urllib.parse
import json
import time
from typing import Optional


class PollinationsAPI:
    """Pollinations AI API client for text generation"""
    
    def __init__(self):
        self.base_url = "https://text.pollinations.ai"
    
    def generate_text(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """Generate text using Pollinations AI API"""
        try:
            # Encode the prompt
            encoded_prompt = urllib.parse.quote(prompt)
            
            # Prepare parameters
            params = {
                "model": "openai",
                "seed": int(time.time()),  # Use timestamp for randomness
            }
            
            # Add system prompt if provided
            if system_prompt:
                params["system"] = system_prompt
            
            # Build URL
            url = f"{self.base_url}/{encoded_prompt}"
            
            # Make request
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()
            
            return response.text.strip()
            
        except requests.exceptions.RequestException as e:
            return f"抱歉，我现在无法回应。请稍后再试。(错误: {str(e)})"
        except Exception as e:
            return f"发生了意外错误，请稍后再试。(错误: {str(e)})"


class HeartCornerCompanion:
    """心隅陪伴者主类"""
    
    def __init__(self):
        self.api = PollinationsAPI()
    
    def mood_diary_response(self, user_input: str) -> str:
        """心情树洞功能 - 提供温柔的陪伴和理解"""
        if not user_input.strip():
            return "我在这里陪着你，想说什么都可以..."
        
        system_prompt = """你是一个温柔、共情的陪伴者。用户会向你倾诉他们的烦恼、失落或情绪。
        
请遵循以下原则：
1. 以温柔、理解的语气回应
2. 不要急于提供解决方案或建议
3. 专注于情感支持和陪伴
4. 承认和验证用户的感受
5. 使用温暖、安慰的语言
6. 回应长度适中，不要过长
7. 用中文回应

你的角色是一个安静的陪伴者，就像歌词中那样陪着用户伤心难过，提供一个安全的情感出口。"""

        prompt = f"用户说：{user_input}\n\n请给予温柔的陪伴和理解。"
        
        return self.api.generate_text(prompt, system_prompt)
    
    def smile_extractor_response(self, user_input: str) -> str:
        """微笑提取器功能 - 从日常中发现美好"""
        if not user_input.strip():
            return "分享一下你今天的日常吧，让我帮你发现其中的小确幸..."
        
        system_prompt = """你是一个善于发现生活美好的陪伴者。用户会分享他们的日常生活片段。

请遵循以下原则：
1. 仔细阅读用户的日常描述
2. 从中发现并提取值得微笑的、积极的细节
3. 以温暖、鼓励的语气指出这些小确幸
4. 帮助用户重新审视生活中被忽略的美好
5. 用具体的细节来说明为什么这些时刻值得珍惜
6. 语言要温暖而真诚
7. 用中文回应

你的目标是帮助用户发现平凡生活中的闪光点。"""

        prompt = f"用户分享的日常：{user_input}\n\n请帮我从中发现值得微笑的美好细节。"
        
        return self.api.generate_text(prompt, system_prompt)


def create_app():
    """创建Gradio应用"""
    companion = HeartCornerCompanion()
    
    # 自定义CSS样式
    custom_css = """
    .gradio-container {
        max-width: 800px !important;
        margin: auto !important;
    }
    .mood-diary {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
    }
    .smile-extractor {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
    }
    """
    
    with gr.Blocks(
        title="心隅陪伴者 | Heart Corner Companion",
        theme=gr.themes.Soft(),
        css=custom_css
    ) as app:
        
        gr.Markdown("""
        # 🌸 心隅陪伴者
        ### *A gentle companion in the corner of your heart*
        
        在这里，你的每一份情感都被温柔接纳。无论是需要倾诉的烦恼，还是想要分享的日常，我都在这里陪伴你。
        """)
        
        with gr.Tabs():
            # 心情树洞标签页
            with gr.Tab("💭 心情树洞", elem_classes=["mood-diary"]):
                gr.Markdown("""
                ### 倾诉你的心声
                这里是一个安全的情感空间。无论你现在感到烦恼、失落，还是有什么无人可说的情绪，都可以在这里倾诉。
                我会以温柔的心陪伴你，不加评判地理解你的感受。
                """)
                
                with gr.Row():
                    with gr.Column():
                        mood_input = gr.Textbox(
                            label="说出你的心声",
                            placeholder="今天发生了什么让你感到困扰的事情吗？或者有什么想要倾诉的情绪...",
                            lines=4,
                            max_lines=8
                        )
                        mood_submit = gr.Button("倾诉", variant="primary")
                    
                    with gr.Column():
                        mood_output = gr.Textbox(
                            label="温柔的陪伴",
                            lines=6,
                            max_lines=10,
                            interactive=False
                        )
                
                mood_submit.click(
                    fn=companion.mood_diary_response,
                    inputs=mood_input,
                    outputs=mood_output
                )
                
                # 添加回车键提交
                mood_input.submit(
                    fn=companion.mood_diary_response,
                    inputs=mood_input,
                    outputs=mood_output
                )
            
            # 微笑提取器标签页
            with gr.Tab("😊 微笑提取器", elem_classes=["smile-extractor"]):
                gr.Markdown("""
                ### 发现生活中的小确幸
                分享你的日常生活片段，让我帮你发现其中值得微笑的美好细节。
                有时候，幸福就藏在那些看似平凡的时刻里。
                """)
                
                with gr.Row():
                    with gr.Column():
                        smile_input = gr.Textbox(
                            label="分享你的日常",
                            placeholder="今天做了什么呢？哪怕是很平常的事情，比如喝了一杯咖啡、看到了夕阳、听到了喜欢的歌...",
                            lines=4,
                            max_lines=8
                        )
                        smile_submit = gr.Button("发现美好", variant="secondary")
                    
                    with gr.Column():
                        smile_output = gr.Textbox(
                            label="发现的小确幸",
                            lines=6,
                            max_lines=10,
                            interactive=False
                        )
                
                smile_submit.click(
                    fn=companion.smile_extractor_response,
                    inputs=smile_input,
                    outputs=smile_output
                )
                
                # 添加回车键提交
                smile_input.submit(
                    fn=companion.smile_extractor_response,
                    inputs=smile_input,
                    outputs=smile_output
                )
        
        gr.Markdown("""
        ---
        *💝 记住，你的感受都是有效的，你的存在本身就很珍贵。*
        """)
    
    return app


if __name__ == "__main__":
    app = create_app()
    app.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        show_error=True
    )