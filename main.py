from fastapi import FastAPI, status, HTTPException, Depends
from directories import signup
from directories import login, delete_account, update, read
from pydantic import BaseModel

app = FastAPI()

app.include_router(login.router, prefix="/auth", tags=["Login"])
app.include_router(signup.router, prefix="/auth", tags=["Signup"])
app.include_router(delete_account.router, prefix="/auth", tags=["Delete"])
app.include_router(update.router, prefix="/auth", tags=["Update"])
app.include_router(read.router, prefix="/auth", tags=["Read"])