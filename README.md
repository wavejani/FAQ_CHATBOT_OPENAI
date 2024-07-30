# FAQ Chatbot

This project implements a chatbot that answers customer questions based on an FAQ list.

This projext has NOT been fully tested. My OPENAI API KEY ran out of credits. Will do another version with Hugging Face API.

## Setup

1. Clone the repository: FAQ_CHATBOT_OPENAI from github

2. Install the dependencies

   ```bash

   pip install -r requirements.txt

   ```

3. Put OPENAI API KEY on chatbot.py and preprocess_faqs.py

4. Run the preprocessing script (faqs.json already done, before running preprocess_faqs.py, delete the old faqs.json):
   cd src
   python3 preprocess_faqs.py

5. Run the script to create Faiss index:

   python3 create_index.py

6. Run the Gradio application:
   python app.py (or) python3 app.py

Access the Gradio FAQ_CHATBOT_OPENAI interface at http://localhost:7860 in your web browser. You can change the port by inputting a new port to app.py and docker-compose.yml files
