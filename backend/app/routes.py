from fastapi import APIRouter, UploadFile, File, Form
from app.rag_engine import ask_question, add_document

router = APIRouter(tags=["upload", "chat"])

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    content = await file.read()
    add_document(file.filename, content)
    return {"message": "File uploaded and indexed"}

@router.post("/chat")
async def chat(query: str = Form(...)):
    answer = ask_question(query)
    return {"response": answer}
