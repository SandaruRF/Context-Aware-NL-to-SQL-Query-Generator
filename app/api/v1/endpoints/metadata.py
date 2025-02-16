from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.metadata import fetch_db_metadata

router = APIRouter()

@router.get("/metadata")
async def get_db_metadata(db: Session = Depends(get_db)):
    try:
        metadata = fetch_db_metadata(db)
        if not metadata["metadata"]:
            raise HTTPException(status_code=404, detail=metadata["message"])
        return jsonable_encoder(metadata)
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))