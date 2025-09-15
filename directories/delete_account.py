from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from .signup import user_data
from pydantic import BaseModel

router = APIRouter()

class Delete_Account(BaseModel):
    email : str

@router.delete('/delete/')
async def delete_account(user : Delete_Account):
    for i in user_data:
        if (i["email"] == user.email):
            user_data.remove(i)
            return "I'd is now deleted successfully."
    return "I'd is not found. Please try again."