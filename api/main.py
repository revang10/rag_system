from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="Enterprise RAG System",
    description="PDF-based Retrieval Augmented Generation API",
    version="1.0.0"
)

app.include_router(router)
