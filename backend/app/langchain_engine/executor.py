from sqlalchemy import text
from app.database.connection import engine
from .query_validator import SQLValidator


class SQLExecutor:
    @staticmethod
    def execute(sql: str, max_rows: int = 100):
        if not SQLValidator.is_safe(sql):
            return {
                "error": "Unsafe SQL detected. Only SELECT queries are allowed for database safety."
            }
        try:
            with engine.connect() as conn:
                result = conn.execute(text(sql))
                rows = result.fetchmany(max_rows)
                
                formatted = [
                    dict(row._mapping) for row in rows
                ]
                
                return {
                    "rows": formatted,
                    "row_count": len(formatted)
                }
        except Exception as e:
            return {"error": str(e)}