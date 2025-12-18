from fastapi import FastAPI
from app.evaluation.routes import auth_router, eval_router

app = FastAPI(title="YouTube Evaluation API")

app.include_router(auth_router)
app.include_router(eval_router)
