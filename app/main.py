from fastapi import FastAPI
from app.api.v1.endpoints.metadata import router as metadata_router
from app.api.v1.endpoints.sql_query import router as sql_query_router

app = FastAPI()

app.include_router(metadata_router)
app.include_router(sql_query_router)

