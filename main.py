from urllib import response
from fastapi import Depends, FastAPI, APIRouter
from fastapi.responses import HTMLResponse
from config import settings, get_settings, Settings
from endpoints import draw
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# v0 = APIRouter(prefix="/experimental")
# v0.include_router(device_show_commands_route.router)
# v0.include_router(device_config_commands_route.router)
# app.include_router(v0)
v1 = APIRouter(prefix="/api")
v1.include_router(draw.router)
app.include_router(v1)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def root(settings: Settings = Depends(get_settings)):
    response_html = """
    Authorized access only
    """
    return HTMLResponse(content=response_html, status_code=200)

