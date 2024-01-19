from typing import List
from fastapi import APIRouter, HTTPException, status

from models import generos
from models.generos import Genero

router = APIRouter()
@router.get(path="/", response_model=List[Genero])
async def listar_generos():
    return list(generos.generos)