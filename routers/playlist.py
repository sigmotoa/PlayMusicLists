from typing import List
from fastapi import APIRouter, HTTPException, status, Path, Body, Request, Form
from fastapi.responses import HTMLResponse, PlainTextResponse, RedirectResponse, FileResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

from models import playlist
from models.playlist import Playlist

router = APIRouter()

@router.get("/",response_class=HTMLResponse)
def show_playlist(request:Request):
    return templates.TemplateResponse("playlists.html", {"request": request, "title": "playlists", "playlists": playlist.playlists})

@router.get("/create",response_class=HTMLResponse,status_code=201)
def create_artistas(request: Request):
    return templates.TemplateResponse("newPlaylist.html",{
        "request":request,
        "title":"Nueva Playlist"
    })

@router.post("/new",status_code=201)
def adicionar_artista(id: int =Form(...), nombre: str =Form(...)):
    body_playlist = {"id": id, "nombre": nombre}
    playlist.playlists.append(body_playlist)
    return RedirectResponse(url="/playlists/",status_code=303)

@router.get("/{id_artista}",response_class=HTMLResponse)
def get_playlist(request: Request,id_playlist: int=Path(...)):
    playlists= playlist.playlists.__getitem__(id_playlist)
    response = templates.TemplateResponse("artista.html",{
        "request": request,
        "title": "Playlist",
        "artista": playlists
        })
    if not playlists:
        response.status_code=404
    return response