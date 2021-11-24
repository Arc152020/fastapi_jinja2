from fastapi import FastAPI, APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
# from typing import Optional, Any
from pathlib import Path


BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

app = FastAPI(title="Demonstrating FastAPI Template", openapi_url="/openapi.js")

api_router = APIRouter()


@api_router.get("/", status_code=200, response_class=HTMLResponse)
def root(request: Request):
    """
    Root GET
    :param request:
    :return:
    """

    return TEMPLATES.TemplateResponse(
        "index.html",
        {"request": request, "recipes": {"bread": ["Flour", "Egg"]}})


@api_router.get("/person/{id}", response_class=HTMLResponse)
async def get_person(request: Request, id: str):
    return TEMPLATES.TemplateResponse('person.html', {"request": request, "id": id})


app.include_router(api_router)
app.mount("/static", StaticFiles(directory="static"), name="static")