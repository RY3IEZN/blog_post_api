from fastapi import FastAPI
from database import Base, engine

app = FastAPI()


Base.metadata.create_all(bind=engine)


@app.get("/home")
async def home():
    return {"hello": "world``"}
