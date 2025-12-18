from pydantic import BaseModel, HttpUrl

class EvaluationRequest(BaseModel):
    youtube_url: HttpUrl
