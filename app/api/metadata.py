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
        column_data = [
            {"column_name": column.name, 
             "data_type": str(column.type)}
            for column in table.columns
        ]

        primary_keys = [
            pk.name for pk in table.primary_key.columns
        ]

        foreign_keys = [
            {"local_column": fk.parent.name, 
             "referenced_table": fk.column.table.name,
             "referenced_column": fk.column.name}
            for fk in table.foreign_keys
        ]

        tables_info.append({
            "table_name": table_name,
            "columns": column_data,
            "primary_keys": primary_keys,
            "foreign_keys": foreign_keys
        })

    return jsonable_encoder({"metadata": tables_info})