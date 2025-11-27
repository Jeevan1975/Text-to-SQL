from fastapi import APIRouter
from ..database.schema_loader import load_schema


router = APIRouter()


@router.get("/", response_model=SchemaResponse)
async def get_schema():
    return {"schema": load_schema()}