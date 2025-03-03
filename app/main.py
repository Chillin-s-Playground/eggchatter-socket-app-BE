from fastapi import FastAPI

from app.routers.ws import chat

app = FastAPI()
