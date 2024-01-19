from typing import List
from fastapi import APIRouter, HTTPException, status

from models import playlist
from models.playlist import Playlist

router = APIRouter()
@router.get(path="/" , response_model=List[Playlist])
async def listar_playlists():
    return list(playlist.playlists)