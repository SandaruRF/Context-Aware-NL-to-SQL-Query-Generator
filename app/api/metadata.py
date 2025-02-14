from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import Session
from app.core.database import get_db, get_metadata

router = APIRouter()

@router.get("/metadata")
async def get_db_metadata(db: Session = Depends(get_db)):
    metadata = get_metadata()

    tables_info = []

    for table_name, table in metadata.tables.items():
        columns = [column.name for column in table.columns]

        foreign_keys = [
            {"column": fk.column.name, "referenced_table": fk.target_fullname}
            for fk in table.foreign_keys
        ]

        tables_info.append({
            "table_name": table_name,
            "columns": columns,
            "foreign_keys": foreign_keys
        })

    return jsonable_encoder({"metadata": tables_info})