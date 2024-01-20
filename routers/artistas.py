from typing import List
from fastapi import APIRouter, Path, Body, Path, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

templates  = Jinja2Templates(directory="templates")
from models import artistas
from models.artistas import Artista

router = APIRouter()
@router.get("/home",response_class=HTMLResponse)
def home_artistas(request: Request):
    return templates.TemplateResponse("generic.html",{
        "request":request,
        "title":"Home de Artistas",
        "texto":"Bienvenido a la pagina de los artistas"
    })

@router.get("/",response_class=HTMLResponse)
def show_artistas(request: Request):
    return templates.TemplateResponse("artistas.html",{
        "request":request,
        "title":"Artistas",
        "artistas":artistas.artistas
    })


@router.get("/create",response_class=HTMLResponse,status_code=201)
def create_artistas(request: Request):
    return templates.TemplateResponse("newArtista.html",{
        "request":request,
        "title":"Nuevo Artistas"
    })

@router.post("/new",status_code=201)
def adicionar_artista(id: int=Form(...),nombre: str=Form(...),idgenero:int=Form(...), genero: str =Form(...)):
    body_artista = {"id":id, "nombre":nombre, idgenero:"idgenero", genero:"genero"}
    artistas.artistas.append(body_artista)
    return RedirectResponse(url="/artistas/",status_code=303)

@router.get("/{id_artista}",response_class=HTMLResponse)
def get_artista(request: Request,id_artista: int=Path(...)):
    artista= artistas.artistas.__getitem__(id_artista)
    response = templates.TemplateResponse("artista.html",{
        "request": request,
        "title": "Artista",
        "artista": artista
        })
    if not artista:
        response.status_code=404
    return response
