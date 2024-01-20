from typing import List
from fastapi import APIRouter, HTTPException, status, Path, Body, Request, Form
from fastapi.responses import HTMLResponse, PlainTextResponse, RedirectResponse, FileResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

from models import canciones
from models.canciones import Cancion

router = APIRouter()

@router.get("/",response_class=HTMLResponse)
def show_canciones(request:Request):
    return templates.TemplateResponse("canciones.html", {"request": request, "title": "canciones", "canciones": canciones.canciones})

@router.get("/create",response_class=HTMLResponse,status_code=201)
def create_cancion(request: Request):
    return templates.TemplateResponse("newCancion.html",{
        "request":request,
        "title":"Nueva Cancion"
    })

@router.post("/new",status_code=201)
def adicionar_cancion(id: int=Form(...),nombre: str=Form(...),idArtista:int=Form(...), nomartista: str =Form(...), idgenero: int =Form(...), nomgenero: str =Form(...), idgenero2: int =Form(...), nomgenero2: str =Form(...), duracion: int =Form(...)):
    body_artista = {"id":id, "nombre":nombre, "idArtista":idArtista, "nomartista":nomartista, "idgenero":idgenero, "nomGenero":nomgenero, "idgenero2":idgenero2, "nomGenero2":nomgenero2, "duracion":duracion}
    canciones.canciones.append(body_artista)
    return RedirectResponse(url="/canciones/",status_code=303)

@router.get("/{id_cancion}",response_class=HTMLResponse)
def get_artista(request: Request,id_cancion: int=Path(...)):
    cancion= canciones.canciones.__getitem__(id_cancion)
    response = templates.TemplateResponse("cancion.html",{
        "request": request,
        "title": "Cacion",
        "cancion": cancion
        })
    if not cancion:
        response.status_code=404
    return response