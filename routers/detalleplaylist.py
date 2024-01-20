from typing import List
from fastapi import APIRouter, HTTPException, status, Path, Body, Request, Form
from fastapi.responses import HTMLResponse, PlainTextResponse, RedirectResponse, FileResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

from models import detalleplaylis

router = APIRouter()

@router.get("/home", response_class=HTMLResponse)
def home_detalles(request: Request):
    return templates.TemplateResponse("generic.html",
    {"request": request,
     "title": "Play lista de Usuario",
     "texto": "Detalles de playlist de  Usuarios "
     })

@router.get("/",response_class=HTMLResponse)
def show_detalle(request: Request):
    return templates.TemplateResponse("detalleplaylists.html",{
        "request": request ,
        "title": "listas de Musica",
        "detalleplaylists":detalleplaylis
    })

@router.get("/create", response_class=HTMLResponse,status_code=201)
def create_Detalle(request: Request):
    return templates.TemplateResponse("newPlaylistDetail.html",{
        "request": request,
        "title": "Nueva lista de Usuario"
    })

@router.post("/new", status_code=201)
def add_Detalle( id: int =Form(...),id_playlist: int =Form(...),id_cancion: int=Form(...)):
    body_detalle = {
        "id":id, "id_playlist":id_playlist, "id_cancion":id_cancion
    }
    detalleplaylis.detalleplaylists.append(body_detalle)
    return RedirectResponse(url="/detalles/",status_code=303)

@router.get("/{id_detail}", response_class=HTMLResponse)
def show_detalle(request: Request, id_detail : int = Path(...)):
    detalle= detalleplaylis.detalleplaylists.__getitem__(id_detail)
    response = templates.TemplateResponse("detalleplaylist.html",{
        "request": request,
        "title": "lista",
        "detalleplaylist":detalle
    })
    if not detalle:
        response.status_code=404
    return response


