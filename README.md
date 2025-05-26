# 🤖 AI-Powered Chatbot with RAG (Retrieval-Augmented Generation)

An intelligent chatbot that answers user questions based on uploaded documents. Built using FastAPI, React, OpenAI GPT, and vector search with FAISS.

![Screenshot](./assets/chatbot-demo.png)

---

## 🚀 Features

- 📄 Upload PDFs and get context-aware answers
- 🔍 Vector search with `sentence-transformers` + FAISS
- 🧠 GPT-powered reasoning over your own data
- ⚡ Full-stack: FastAPI backend + React frontend
- 📦 Easy to run locally or deploy via Docker

---

## 🛠️ Tech Stack

- **Frontend**: React (TypeScript), Tailwind CSS
- **Backend**: FastAPI, LangChain, OpenAI API
- **Embeddings**: `all-MiniLM-L6-v2`
- **Vector DB**: FAISS
- **Document Support**: PDF (more coming)

---

## 🧪 Demo

Try it locally:

```bash
# 1. Clone the repo
git clone https://github.com/abhaybraja/ai-chatbot-with-rag.git
cd ai-chatbot-with-rag

# 2. Start backend
cd backend
cp .env.example .env  # Add your OpenAI key
docker build -t rag-backend .
docker run -p 8000:8000 --env-file .env rag-backend

# 3. Start frontend
cd ../frontend
npm install
npm run dev
```

Then open: http://localhost:5173
