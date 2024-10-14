# gradio_app.py
import gradio as gr
from utils import analyze_sentiment

def gradio_interface():
    return gr.Interface(
        
        fn=analyze_sentiment,
        inputs=gr.Textbox(lines=2, placeholder="Enter text to analyze..."),
        outputs=[
            
            gr.Textbox(label="Polarity"),
            gr.Textbox(label="Subjectivity"),
            gr.Textbox(label="Sentiment Label"),
            gr.Textbox(label="Error")
        ],
        live=False,
        title="Sentiment Analysis",
    )

if __name__ == "__main__":
    interface = gradio_interface()
    interface.launch(share=True)
