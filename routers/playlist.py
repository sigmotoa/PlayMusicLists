from typing import List
from fastapi import APIRouter, HTTPException, status, Path, Body, Request, Form
from fastapi.responses import HTMLResponse, PlainTextResponse, RedirectResponse, FileResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

from models import playlist
from models.playlist import Playlist

router = APIRouter()

@router.get("/{tradicional}",response_model=List[Playlist])
async def list_playlsts():
    return list(playlist.playlists)

@router.put("/{playlist_id}")
def insert_playlist(
        playlist_id: int=Path(...,
        description="Id de lista",
        title="lista",
        gt=0),
        playlists: Playlist = Body(...)
    ):
    tmpp=playlist.playlists
    tmpp.append(playlists)
    return playlists

@router.get("/",response_class=HTMLResponse)
def show_playlist(request:Request):
    return templates.TemplateResponse("playlists.html", {"request": request, "title": "playlists", "playlists": playlist.playlists})