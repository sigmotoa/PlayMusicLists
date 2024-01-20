from typing import List
from fastapi import APIRouter, HTTPException, status, Path, Body, Request, Form
from fastapi.responses import HTMLResponse, PlainTextResponse, RedirectResponse, FileResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

from models import canciones
from models.canciones import Cancion

router = APIRouter()

@router.get("/",response_class=HTMLResponse)
def show_canciones(request:Request):
    return templates.TemplateResponse("canciones.html", {"request": request, "title": "canciones", "canciones": canciones.canciones})


@router.get("/{pruebas}", response_model=List[Cancion])
async def listar_canciones():
    return list(canciones.canciones)

@router.put("/{cancion_id}")
def insert_cancion(
        cancion_id: int = Path(...,
        description="Id de cancion",
        title="Id Cancion",
        gt=0
         ),
        cancion1: Cancion =Body(...)
        ):
    tmpc=canciones.caciones
    tmpc.append(cancion1)
    return cancion1