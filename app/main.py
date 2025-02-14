from fastapi import FastAPI
from app.api import metadata

app = FastAPI()

app.include_router(metadata.router)

