from pydantic import BaseModel
from typing import Optional, List
from .generos import Genero

class Artista(BaseModel):
    id: int
    nombre: str
    genero: Genero


#Create a list of 50 artistas using all the genereos

artistas = [
    Artista(id=1, nombre="Adele", genero=Genero(id=2, nombre="Pop")),
    Artista(id=2, nombre="Aerosmith", genero=Genero(id=1, nombre="Rock")),
    Artista(id=3, nombre="Alejandro Sanz", genero=Genero(id=9, nombre="Balada")),
    Artista(id=4, nombre="Alicia Keys", genero=Genero(id=31, nombre="Soul")),
    Artista(id=5, nombre="Amy Winehouse", genero=Genero(id=31, nombre="Soul")),
    Artista(id=6, nombre="Andres Calamaro", genero=Genero(id=9, nombre="Balada")),
    Artista(id=7, nombre="Andres Calamaro", genero=Genero(id=1, nombre="Rock")),
    Artista(id=8, nombre="Andres Calamaro", genero=Genero(id=36, nombre="Fusion")),
    Artista(id=9, nombre="Andres Calamaro", genero=Genero(id=17, nombre="Rap")),
    Artista(id=10, nombre="Andres Calamaro", genero=Genero(id=2, nombre="Pop")),
    Artista(id=11, nombre="Andres Calamaro", genero=Genero(id=32, nombre="Gospel")),
    Artista(id=12, nombre="Andres Calamaro", genero=Genero(id=31, nombre="Soul")),
    Artista(id=13, nombre="Andres Calamaro", genero=Genero(id=3, nombre="Cumbia")),
    Artista(id=14, nombre="Andres Calamaro", genero=Genero(id=4, nombre="Reggaeton")),
    Artista(id=15, nombre="Andres Calamaro", genero=Genero(id=5, nombre="Salsa")),
    Artista(id=16, nombre="Andres Calamaro", genero=Genero(id=6, nombre="Bachata")),
    Artista(id=17, nombre="Andres Calamaro", genero=Genero(id=7, nombre="Merengue")),
    Artista(id=18, nombre="Andres Calamaro  ", genero=Genero(id=8, nombre="Vallenato"))]