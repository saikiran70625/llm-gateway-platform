from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="LLM Gateway",
    description="A learning project for routing and observing LLM requests",
    version="0.1.0",
)


class ChatRequest(BaseModel):
    message: str
    provider: str = "mock"
    model: str = "demo"


class ChatResponse(BaseModel):
    request_id: str
    provider: str
    model: str
    answer: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/v1/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    return ChatResponse(
        request_id="demo-request-001",
        provider=request.provider,
        model=request.model,
        answer=f"Mock response for: {request.message}",
    )
