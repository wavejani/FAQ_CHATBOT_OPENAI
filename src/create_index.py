import faiss
import numpy as np

# Load the generated embeddings
faq_embeddings = np.load('../data/faq_embeddings.npy')
dimension = faq_embeddings.shape[1]

# Create and populate the Faiss index
index = faiss.IndexFlatL2(dimension)
index.add(faq_embeddings)

# Save the index
faiss.write_index(index, '../data/faq_index.faiss')
