from fastapi import APIRouter
from pydantic import BaseModel

from app.services.document_service import document_service

router = APIRouter()


class AskRequest(BaseModel):
    question: str


@router.post("/ask")
def ask(req: AskRequest):
    return document_service.ask(req.question)