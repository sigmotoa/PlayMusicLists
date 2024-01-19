from typing import List
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

templates = Jinja2Templates(directory="templates")
from models import generos
from models.generos import Genero

router = APIRouter()

@router.get("/home", response_class=HTMLResponse)
def home_generos(request:Request):
    return templates.TemplateResponse("generic.html", {"request": request, "title": "Home de Generos", "texto": "Bienvenido a la Home de Generos"})

@router.get("/intro", response_class=HTMLResponse)
def home_generos(request:Request):
    return templates.TemplateResponse("generic.html", {"request": request, "title": "Intro de Generos", "texto": "Esta es una pagina adicional"})


@router.get("/", response_class=HTMLResponse)
def show_generos(request:Request):
    return templates.TemplateResponse("generos.html", {"request": request, "title": "Generos", "generos": generos.generos})
    #return list(generos.generos)

@router.get("/{id_genero}", response_model=Genero)
def show_genero(id_genero: int):
    for genero in generos.generos:
        if genero.id == id_genero:
            return genero
    return {"message": "Genero no encontrado"}

@router.post("/", response_model=Genero, status_code=201)
def create_genero(genero: Genero):
    generos.generos.append(genero)
    return genero