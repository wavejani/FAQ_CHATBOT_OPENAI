import json
import numpy as np
import faiss
import openai

# Set your OpenAI API key
openai.api_key = 'PUT_OPENAI_API_KEY_HERE'

# Load the index and FAQs
index = faiss.read_index('../data/faq_index.faiss')
with open('../data/faqs.json') as f:
    faqs = json.load(f)

def get_response(query):
    query_embedding = openai.Embedding.create(input=[query], model="text-embedding-ada-002")['data'][0]['embedding']
    query_embedding = np.array(query_embedding).astype('float32').reshape(1, -1)
    
    D, I = index.search(query_embedding, k=1)
    faq_index = I[0][0]
    
    # Define an appropriate threshold
    threshold = 0.5
    if D[0][0] < threshold:
        return faqs[faq_index]['answer']
    else:
        return "Sorry, I couldn't find an answer to your question."

# Test the response function
if __name__ == "__main__":
    print(get_response("How do I reset my password?"))
