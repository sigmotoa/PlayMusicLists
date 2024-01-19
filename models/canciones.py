from pydantic import BaseModel
from typing import Optional, List
from .generos import Genero
from .artistas import Artista

class Cancion(BaseModel):
    id: int
    nombre: str
    artista: Artista
    genero: Genero
    duracion: int

# create a list of 100 canciones
canciones = [
    Cancion(id=1, nombre="Hello", artista=Artista(id=1, nombre="Adele", genero=Genero(id=2, nombre="Pop")), genero=Genero(id=2, nombre="Pop"), duracion=295),
    Cancion(id=2, nombre="Dream On", artista=Artista(id=2, nombre="Aerosmith", genero=Genero(id=1, nombre="Rock")), genero=Genero(id=1, nombre="Rock"), duracion=290),
    Cancion(id=3, nombre="No Me Compares", artista=Artista(id=3, nombre="Alejandro Sanz", genero=Genero(id=9, nombre="Balada")), genero=Genero(id=9, nombre="Balada"), duracion=295),
    Cancion(id=4, nombre="Fallin", artista=Artista(id=4, nombre="Alicia Keys", genero=Genero(id=31, nombre="Soul")), genero=Genero(id=31, nombre="Soul"), duracion=195),
    Cancion(id=5, nombre="Back To Black", artista=Artista(id=5, nombre="Amy Winehouse", genero=Genero(id=31, nombre="Soul")), genero=Genero(id=31, nombre="Soul"), duracion=240),
    Cancion(id=6, nombre="Flaca", artista=Artista(id=6, nombre="Andres Calamaro", genero=Genero(id=9, nombre="Balada")), genero=Genero(id=9, nombre="Balada"), duracion=240),
    Cancion(id=7, nombre="Flaca", artista=Artista(id=7, nombre="Andres Calamaro", genero=Genero(id=1, nombre="Rock")), genero=Genero(id=1, nombre="Rock"), duracion=240),
    Cancion(id=8, nombre="Flaca", artista=Artista(id=8, nombre="Andres Calamaro", genero=Genero(id=36, nombre="Fusion")), genero=Genero(id=36, nombre="Fusion"), duracion=240),
    Cancion(id=9, nombre="Flaca", artista=Artista(id=9, nombre="Andres Calamaro", genero=Genero(id=17, nombre="Rap")), genero=Genero(id=17, nombre="Rap"), duracion=240)]