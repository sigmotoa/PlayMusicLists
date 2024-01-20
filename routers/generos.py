from typing import List
from fastapi import APIRouter, Request, Path, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

templates = Jinja2Templates(directory="templates")
from models import generos
from models.generos import Genero

router = APIRouter()

@router.get("/home", response_class=HTMLResponse)
def home_genero(request:Request):
    return templates.TemplateResponse("generic.html", {"request": request, "title": "Home de Generos", "texto": "Bienvenido a la Home de Generos"})

@router.get("/intro", response_class=HTMLResponse)
def home_generos(request:Request):
    return templates.TemplateResponse("generic.html", {"request": request, "title": "Intro de Generos", "texto": "Esta es una pagina adicional"})


@router.get("/", response_class=HTMLResponse)
def show_generos(request:Request):
    return templates.TemplateResponse("generos.html", {"request": request, "title": "Generos", "generos": generos.generos})
    #return list(generos.generos)



@router.get("/create", response_class=HTMLResponse, status_code=201)
def create_genero(request:Request):
    return templates.TemplateResponse("newgenero.html", {"request": request, "title": "Nuevo Genero"})


@router.post("/new", status_code=201)
def adicionar_genero(id: int =Form(...), nombre: str =Form(...)):
    body_genero = {"id": id, "nombre": nombre}
    generos.generos.append(body_genero)
    return RedirectResponse(url="/generos/", status_code=303)


@router.get("/{id_genero}", response_class=HTMLResponse)
def show_genero(request:Request, id_genero: int=Path(...)):
    genero = generos.generos.__getitem__(id_genero)
    response = templates.TemplateResponse("generos.html", {"request": request, "title": "Genero", "generos": genero})
    if not genero:
        response.status_code= 404
    return response