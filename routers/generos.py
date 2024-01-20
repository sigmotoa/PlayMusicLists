from fastapi import APIRouter, Body
from typing import List

from fastapi.params import Path

from models import generos
from models.generos import Genero

router = APIRouter()

@router.get("/",response_model=List[Genero])
async def list_generos():
    return list(generos.generos)

@router.put("/generos/{genero_id}")
def insert_genero(
        genero_id: int=Path(...,
        description="Id de Genero",
        title="Genero de la cancion",
        gt=0),
        genero: Genero = Body(...)
    ):
    tmpg=generos.generos
    tmpg.append(genero)
    return genero