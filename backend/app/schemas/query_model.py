from pydantic import BaseModel


class QueryRequest(BaseModel):
    natural_language: str
    max_rows: int = 100
    

class QueryResponse(BaseModel):
    sql: str
    results: list | None = None
    row_count: int
    error: str | None = None
