from typing import List
from fastapi import APIRouter, Path,Body

from models import artistas
from models.artistas import Artista

router = APIRouter()
@router.get("/",response_model=list[Artista])
async def listar_artistas():
    return list(artistas.artistas)

@router.put("/{artista_id}")
def insert_artista(
            artista_id: int=Path(...,
            description="Id de artista",
            title="Id de artista",
            gt=0),
            artista: Artista=Body(...)):
    tmp = artistas.artistas
    tmp.append(artista)
    return artista