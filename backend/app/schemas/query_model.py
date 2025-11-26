from pydantic import BaseModel


class QueryRequest(BaseModel):
    natural_language: str
    max_rows: int = 50
    

class QueryResponse(BaseModel):
    sql: str
    results: list
    warnings: list = []
    
