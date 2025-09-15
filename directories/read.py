from fastapi import FastAPI, APIRouter
from .signup import user_data

router = APIRouter()

@router.get('/read/')
async def read():
    return user_data