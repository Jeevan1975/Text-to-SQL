from fastapi import APIRouter
from ..schemas.query_model import QueryRequest, QueryResponse
from ..langchain_engine.runner import nl_to_results

router = APIRouter()


@router.post("/execute", response_model=QueryResponse)
async def execute_query(request: QueryRequest):
    result = nl_to_results(nl_query=request.natural_language, max_rows=request.max_rows)
    
    if "error" in result:
        return QueryResponse(sql=result["sql"], results=[], row_count=0, error=result["error"])
    
    return QueryResponse(
        sql=result["sql"],
        results=result["results"],
        row_count=result["row_count"],
        error=None
    )