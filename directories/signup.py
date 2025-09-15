from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

user_data = []

class SignupUser(BaseModel):
    name: str
    email: str
    password: str

@router.post("/register/")
async def signup(user: SignupUser):
    user_data.append({
        "name":user.name,
        "email":user.email,
        "password":user.password
    })
    return user_data