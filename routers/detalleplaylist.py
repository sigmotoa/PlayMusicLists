from typing import List
from fastapi import APIRouter, HTTPException, status

from models import detalleplaylis
from models.detalleplaylis import DetallePlaylist

router = APIRouter()
@router.get(path="/" , response_model=List[DetallePlaylist])
async def list_Detalle():
    return list(detalleplaylis.detalleplaylists)