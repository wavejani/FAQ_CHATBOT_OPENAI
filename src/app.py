import gradio as gr
from chatbot import get_response

def chatbot(query):
    return get_response(query)

iface = gr.Interface(fn=chatbot, inputs="text", outputs="text", title="FAQ Chatbot OpenAI")
iface.launch(server_port=7860) # you can change the port, change it here and in the docker-compose.yml file
