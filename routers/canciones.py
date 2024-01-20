from typing import List
from fastapi import APIRouter, HTTPException, status, Path, Body
from fastapi.responses import HTMLResponse, PlainTextResponse, RedirectResponse, FileResponse

from models import canciones
from models.canciones import Cancion

router = APIRouter()

@router.get("/", response_model=List[Cancion])
async def listar_canciones():
    return list(canciones.canciones)

@router.put("/canciones/{cancion_id}")
def insert_cancion(
        cancion_id: int = Path(...,
                description="Id de cancion", title="Id Cancion",
                gt=0
         ),
        cancion: Cancion =Body(...)
        ):
    tmpc=canciones.caciones
    tmpc.append(cancion)
    return cancion