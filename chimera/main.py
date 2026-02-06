from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from contextlib import asynccontextmanager
import os

from chimera.db import db
from chimera.skills.trend_fetcher import TrendFetcher

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await db.connect()
    yield
    # Shutdown
    await db.disconnect()

app = FastAPI(title="Project Chimera", version="0.1.0", lifespan=lifespan)

# Mount static files
static_dir = os.path.join(os.path.dirname(__file__), "static")
os.makedirs(static_dir, exist_ok=True)
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Templates
templates_dir = os.path.join(os.path.dirname(__file__), "templates")
os.makedirs(templates_dir, exist_ok=True)
templates = Jinja2Templates(directory=templates_dir)

fetcher = TrendFetcher()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    trends = await fetcher.fetch_trends("technology")
    return templates.TemplateResponse("index.html", {"request": request, "trends": trends})

@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "services": {"redis": "connected", "weaviate": "connected"}}

@app.get("/api/trends/{topic}")
async def get_trends(topic: str):
    return await fetcher.fetch_trends(topic)
