from fastapi import APIRouter
from app.database.schema_loader import load_schema


router = APIRouter()


@router.get("/")
async def get_schema():
    return {"schema": load_schema()}