from fastapi import APIRouter
from ..schemas.query_model import QueryRequest, QueryResponse
from ..langchain_engine.executor import SQLExecutor

router = APIRouter()


@router.post("/execute", response_model=QueryResponse)
async def execute_query(request: QueryRequest):
    result = SQLExecutor.execute(request.sql, request.max_rows)
    
    if "error" in result:
        return QueryResponse(results=[], row_count=0, error=result["error"])
    
    return QueryResponse(
        results=result["rows"],
        row_count=result["row_count"],
        error=None
    )