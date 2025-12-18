from fastapi import FastAPI
from app.auth.routes import router as auth_router
from app.evaluation.routes import router as evaluate


app = FastAPI(title="YouTube Evaluation API")

app.include_router(auth_router)
app.include_router(evaluate)
