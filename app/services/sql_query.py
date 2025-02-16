from google import genai
from sqlalchemy.orm import Session
from app.api.v1.endpoints.metadata import get_db_metadata
import os
import logging
import re

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = genai.Client(api_key=os.getenv("GEMINI_API"))

async def generate_sql_query(db: Session, nl_query):
    schema_info = await get_db_metadata(db)

    prompt = f"""Convert the following natural language query into an optimized SQL query.

    Schema:
    {schema_info}

    Query:
    {nl_query}

    SQL Query:"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )

    sql_query = re.sub(r"```sql|```", "", response.text).strip()
    sql_query = sql_query.replace("\n", " ")
    logger.info("SQL query generated successfully.")
    return sql_query