from fastapi import APIRouter, Request
from pydantic import BaseModel

router = APIRouter()


class AskRequest(BaseModel):
    question: str


@router.post("/ask")
def ask(req: AskRequest, request: Request):
    service = request.app.state.document_service
    return service.ask(req.question)