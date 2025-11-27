from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from .routers import query_router, schema_router
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "static"
TEMPLATES_DIR = BASE_DIR / "frontend"

app = FastAPI(title="Text-to-SQL API")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

templates = Jinja2Templates(directory=TEMPLATES_DIR)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(query_router.router, prefix="/query", tags=["query"])
app.include_router(schema_router.router, prefix="/schema", tags=["schema"])

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})


@app.get("/health")
async def health():
    return {"status": "ok"}