from fastapi import APIRouter, UploadFile, File, Request
import os

from app.pdf_reader import extract_text

router = APIRouter()


@router.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...),
    request: Request = None
):
    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDF files are allowed"}

    # Save temporarily
    temp_path = f"data/{file.filename}"

    with open(temp_path, "wb") as f:
        content = await file.read()
        f.write(content)

    # Get service from app state
    service = request.app.state.document_service

    # 🔥 THIS IS THE IMPORTANT PART
    service.load_document(temp_path)

    os.remove(temp_path)

    return {
        "message": "Document uploaded and indexed successfully",
        "filename": file.filename
    }

