from pydantic import BaseModel


class QueryRequest(BaseModel):
    sql: str
    max_rows: int = 50
    

class QueryResponse(BaseModel):
    results: list
    row_count: int
    error: str | None = None
