from fastapi import FastAPI
from app.api import router

app = FastAPI(title="GPU-Accelerated Fraud Detection Engine")
app.include_router(router)