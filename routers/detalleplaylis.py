from typing import List
from fastapi import APIRouter, Path, Body

from models import detalleplaylis
from models.detalleplaylis import DetallePlaylist

router = APIRouter()
@router.get("/",response_model=list[DetallePlaylist])
async def listar_detalleplaylis():
    return list(detalleplaylis.detalleplaylists)

@router.put("/detalles/{detalleplaylis_id}")
def insert_detalleplaylis(id_detalleplaylist: int=Path(...,
            description="Id de detalleplaylis",
            title="Id de detalleplaylis",
            gt=0),
            detalleplaylist: DetallePlaylist=Body(...)):
    tmp = detalleplaylis.detalleplaylists
    tmp.append(detalleplaylist)
    return detalleplaylist