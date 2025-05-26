from app.db import get_relevant_chunks, store_chunks
from app.utils import extract_text, chunk_text
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import os

llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

def add_document(filename, content):
    text = extract_text(content)
    chunks = chunk_text(text)
    store_chunks(chunks, metadata={"source": filename})

def ask_question(query):
    context = get_relevant_chunks(query)
    prompt = f"Answer based on context:\n{context}\n\nQuestion: {query}"
    response = llm([HumanMessage(content=prompt)])
    return response.content
