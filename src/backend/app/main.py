from fastapi import FastAPI

from app.upload_engine.api.v1.routes_upload import router as upload_router

from fastapi import FastAPI
from app.youtube_engine.evaluation.routes import router as youtube_router

app = FastAPI()

app.include_router(youtube_router)


app.include_router(upload_router, prefix="/api/v1")
app.include_router(youtube_router, prefix="/api/v1")

