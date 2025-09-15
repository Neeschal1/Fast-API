from fastapi import APIRouter
from pydantic import BaseModel
from .signup import user_data

router = APIRouter()

class LoginUser(BaseModel):
    email: str
    password: str

@router.post("/create/")
async def login(user: LoginUser):
    for user_identity in user_data:
        if(user_identity['email'] == user.email and user_identity['password'] == user.password):
            return {
                "Message":"Congratulations! You've Logged in!"
            }
    return {
        "Message":"Check your details and try again."
    }
    
