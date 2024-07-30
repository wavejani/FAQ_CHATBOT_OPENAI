
import os
import json
import openai
import numpy as np

# Set your OpenAI API key
openai.api_key = 'PUT_OPENAI_API_KEY_HERE'

# Directory containing FAQ .txt files
script_dir = os.path.dirname(os.path.abspath(__file__))
faq_dir = os.path.join(script_dir, '../data/faq_files')

# Check if faq_dir exists
if not os.path.exists(faq_dir):
    raise FileNotFoundError(f"The directory {faq_dir} does not exist. Please check the path.")

# Read FAQ files
faqs = []
for filename in os.listdir(faq_dir):
    if filename.endswith('.txt'):
        with open(os.path.join(faq_dir, filename), 'r') as file:
            content = file.read().strip().split('\n', 1)
            if len(content) == 2:
                question, answer = content
                faqs.append({'question': question, 'answer': answer})

# Save FAQs to a JSON file
output_faq_path = os.path.join(script_dir, '../data/faqs.json')
with open(output_faq_path, 'w') as f:
    json.dump(faqs, f)

# Generate embeddings for the questions
questions = [faq['question'] for faq in faqs]
response = openai.Embedding.create(input=questions, model="text-embedding-ada-002")
faq_embeddings = np.array([embedding['embedding'] for embedding in response['data']])

# Save embeddings
output_embeddings_path = os.path.join(script_dir, '../data/faq_embeddings.npy')
np.save(output_embeddings_path, faq_embeddings)




