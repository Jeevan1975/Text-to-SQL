from fastapi import APIRouter
from ..schemas.query_model import QueryRequest, QueryResponse

router = APIRouter()


@router.post("/execute", response_model=QueryResponse)
async def execute_query(request: QueryRequest):
    """
    Dummy endpoint
    """
    nl = request.natural_language
    
    dummy_sql = "SELECT * FROM users LIMIT 5;"
    
    return QueryResponse(sql=dummy_sql, results=[{"message": f"Received NL: {nl}"}], warnings=[])