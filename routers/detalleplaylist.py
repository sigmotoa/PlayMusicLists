from typing import List
from fastapi import APIRouter, HTTPException, status, Path, Body, Request, Form
from fastapi.responses import HTMLResponse, PlainTextResponse, RedirectResponse, FileResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

from models import detalleplaylis
from models.detalleplaylis import DetallePlaylist

router = APIRouter()
@router.get(path="/{viejito}" , response_model=List[DetallePlaylist])
async def list_Detalle():
    return list(detalleplaylis.detalleplaylists)

@router.put("/{detalleplaylis_id}")
def insert_Detalle(
        detalleplaylis_id: int=Path(...,
        description="Id de detalle" ,
        title="detalle",
        gt=0),
        detalleplaylisn: DetallePlaylist= Body(...)
    ):
    tmp2=detalleplaylis.detalleplaylists
    tmp2.append(detalleplaylisn)
    return detalleplaylisn
@router.get("/",response_class=HTMLResponse)
def show_detalles(request:Request):
    return templates.TemplateResponse(
        "detalleplaylists.html",
        {"request": request, "title": "detalles", "detalles":
            detalleplaylis.detalleplaylists})