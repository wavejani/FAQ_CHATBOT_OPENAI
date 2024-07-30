# FAQ Chatbot

This project implements a chatbot that answers customer questions based on an FAQ list.

This projext has NOT been fully tested. My OPENAI API KEY ran out of credits. Will do another version with Hugging Face API.

## Setup

1. Clone the repository: https://github.com/wavejani/FAQ_CHATBOT_OPENAI

3. Install the dependencies

   ```bash

   pip install -r requirements.txt

   ```

4. Put OPENAI API KEY on chatbot.py and preprocess_faqs.py

5. Run the preprocessing script (faqs.json already done, before running preprocess_faqs.py, delete the old faqs.json):
   cd src
   python3 preprocess_faqs.py

6. Run the script to create Faiss index:

   python3 create_index.py

7. Run the Gradio application:
   python app.py (or) python3 app.py

Access the Gradio FAQ_CHATBOT_OPENAI interface at http://localhost:7860 in your web browser. You can change the port by inputting a new port to app.py and docker-compose.yml files
