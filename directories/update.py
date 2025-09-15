from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from .signup import user_data

router = APIRouter()

class User_Update(BaseModel):
    name : str
    email : str
    password : str

@router.put('/update/')
async def update(user: User_Update):
    for i in user_data:
        if (i['name'] == user.name):
            i['email'] = user.email
            i['password'] = user.password
            return {
                f"{user.name}'s account is successfully updated."
            }
    return "Some error occured!"
            