from typing import List
from fastapi import APIRouter, HTTPException, status

from models import artistas
from models.artistas import Artista

router = APIRouter()
@router.get(path="/" , response_model=List[Artista])
async def list_artistas():
    return list(artistas.artistas)