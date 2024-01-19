from typing import List
from fastapi import APIRouter, HTTPException, status

from models import canciones
from models.canciones import Cancion

router = APIRouter()

@router.get("/", response_model=List[Cancion])
async def listar_canciones():
    return list(canciones.canciones)