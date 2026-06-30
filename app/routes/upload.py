from fastapi import APIRouter, UploadFile, File
import os
from app.pdf_reader import extract_text

router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDF files are allowed"}


    temp_path = f"data/{file.filename}"

    with open(temp_path, "wb") as f:
        content = await file.read()
        f.write(content)

    text = extract_text(temp_path)

    response = {
        "filename": file.filename,
        "characters": len(text),
        "preview": text[:500] if text else "No text found"
    }

    os.remove(temp_path)

    return response