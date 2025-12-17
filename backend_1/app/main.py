from fastapi import FastAPI
from auth.routes import router as auth_router
from evaluation.routes import router as eval_router

app = FastAPI(title="YouTube Evaluation API")

app.include_router(auth_router)
app.include_router(eval_router)
