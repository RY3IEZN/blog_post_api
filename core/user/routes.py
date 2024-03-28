from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import session
from models import User

user_router = APIRouter()


@user_router.post("/signup")
async def signup():
    return {"sign up"}
