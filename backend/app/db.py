from sentence_transformers import SentenceTransformer
import faiss
import pickle

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.IndexFlatL2(384)
data = []

def store_chunks(chunks, metadata=None):
    embeddings = model.encode(chunks)
    index.add(embeddings)
    data.extend([{"text": chunk, "meta": metadata} for chunk in chunks])
    with open("vectorstore/data.pkl", "wb") as f:
        pickle.dump(data, f)

def get_relevant_chunks(query, top_k=3):
    q_emb = model.encode([query])
    D, I = index.search(q_emb, top_k)
    return "\n".join([data[i]["text"] for i in I[0]])
