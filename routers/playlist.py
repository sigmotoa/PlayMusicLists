from fastapi import APIRouter, Body
from typing import List

from fastapi.params import Path

from models import playlist
from models.playlist import Playlist

router = APIRouter()

@router.get("/",response_model=List[Playlist])
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