from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def get_schema():
    """
    Example schema for testing the connection
    """
    example = {
        "tables": {
            "users": ["id", "name", "email", "created_at"],
            "orders": ["id", "user_id", "total", "created_at"]
        }
    }
    return example