from typing import List
from fastapi import APIRouter, HTTPException, status, Path, Body

from models import artistas
from models.artistas import Artista

router = APIRouter()
@router.get(path="/" , response_model=List[Artista])
async def list_artistas():
    return list(artistas.artistas)

@router.put(path="/", response_model=Artista)
def insert_artista(artista_id: int=Path(...,
            description="Id de artista",
            title="Id de artista",
            gt=0),
            artista: Artista=Body(...)):
    tmp = artistas.artistas
    tmp.append(artista)
    return artista