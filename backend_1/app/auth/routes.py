from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import authenticate_user, create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form.username, form.password)
    if not user:
        return {"error": "Invalid credentials"}
    token = create_access_token({"sub": user["username"]})
    return {"access_token": token, "token_type": "bearer"}
