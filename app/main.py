from fastapi import FastAPI
from app.api.v1.endpoints import predict

app = FastAPI(
    title="Email Spam Classifier",
    description="A FastAPI app to classify emails as spam or ham",
    version="1.0.0"
)

app.include_router(predict.router, prefix="/api/v1")