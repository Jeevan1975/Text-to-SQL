from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import query_router, schema_router

app = FastAPI(title="Text-to-SQL API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(query_router.router, prefix="/query", tags=["query"])
app.include_router(schema_router.router, prefix="/schema", tags=["schema"])


@app.get("/health")
async def health():
    return {"status": "ok"}