import gradio as gr
from huggingface_hub import InferenceClient
import time
from huggingface_hub.utils._errors import HfHubHTTPError

client = InferenceClient("HuggingFaceH4/zephyr-7b-beta", token="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")

def respond(message, history: list[tuple[str, str]], system_message="", max_tokens=512, temperature=0.7, top_p=0.95):
    
    messages = [{"role": "system", "content": system_message}]

    for val in history:
        if val[0]:
            messages.append({"role": "user", "content": val[0]})
        if val[1]:
            messages.append({"role": "assistant", "content": val[1]})

    messages.append({"role": "user", "content": message})

    response = ""
    attempt = 0
    max_attempts = 5

    while attempt < max_attempts:
        try:
            for message in client.chat_completion(
                messages,
                max_tokens=max_tokens,
                stream=True,
                temperature=temperature,
                top_p=top_p,
            ):
                token = message.choices[0].delta.content
                response += token
                yield response
            break  # Exit the loop if successful
        except HfHubHTTPError as e:
            if e.response.status_code == 429:
                attempt += 1
                time.sleep(2 ** attempt)  # Exponential backoff
            else:
                raise
# Define custom CSS
custom_css =""" 

.body{
}
.gradio-container {
    display:flex;
    justify-content:center;
    align_items:center;
    padding: 20px;
    border-radius: 10px;
}
.gradio-chatbot-message-assistant {
    background-color: #e0e0e0;
    color: black;
    padding: 10px;
    border-radius: 15px;
    margin-bottom: 10px;
    text-align: right
}
/* Target the gradio-app element directly */
gradio-app {
    background-color: #f5f5f5 !important; /* Example of overriding inline background color */
    padding: 20px 60px !important; /* Example of overriding padding */
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1) !important; /* Adding a shadow */
}
"""

# Create the Gradio app
demo = gr.ChatInterface(
    fn=respond,
    additional_inputs=[
        gr.Textbox(value="You are a Chatbot. Your name is Evy. You are Developed By Joe.", label="System message"),
        gr.Slider(minimum=1, maximum=2048, value=512, step=1, label="Max new tokens"),
        gr.Slider(minimum=0.1, maximum=4.0, value=0.7, step=0.1, label="Temperature"),
        gr.Slider(
            minimum=0.1,
            maximum=1.0,
            value=0.95,
            step=0.05,
            label="Top-p (nucleus sampling)",
        ),
    ],
    
css=custom_css
)

if __name__ == "__main__":
    demo.launch(server_port=7861, share=True)
