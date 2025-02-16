from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.sql_query import generate_sql_query

router = APIRouter()

@router.get("/sql_query")
async def get_sql_query(db: Session = Depends(get_db)):
    try:
        nl_query = "Give list of albems with respective artist name"
        sql_query = await generate_sql_query(db, nl_query)
        if not sql_query:
            raise HTTPException(status_code=400, detail="Failed to generate SQL query.")
        return sql_query
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating SQL query: {str(e)}")