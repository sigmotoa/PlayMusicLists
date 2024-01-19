from pydantic import BaseModel
from typing import Optional, List

class Genero(BaseModel):
    id: int
    nombre: str


# create a list of generos
generos = [
    Genero(id=1, nombre="Rock"),
    Genero(id=2, nombre="Pop"),
    Genero(id=3, nombre="Cumbia"),
    Genero(id=4, nombre="Reggaeton"),
    Genero(id=5, nombre="Salsa"),
    Genero(id=6, nombre="Bachata"),
    Genero(id=7, nombre="Merengue"),
    Genero(id=8, nombre="Vallenato"),
    Genero(id=9, nombre="Balada"),
    Genero(id=10, nombre="Ranchera"),
    Genero(id=11, nombre="Banda"),
    Genero(id=12, nombre="Ska"),
    Genero(id=13, nombre="Punk"),
    Genero(id=14, nombre="Metal"),
    Genero(id=15, nombre="Jazz"),
    Genero(id=16, nombre="Blues"),
    Genero(id=17, nombre="Rap"),
    Genero(id=18, nombre="Hip Hop"),
    Genero(id=19, nombre="Folklore"),
    Genero(id=20, nombre="Country"),
    Genero(id=21, nombre="Clasica"),
    Genero(id=22, nombre="Electronica"),
    Genero(id=23, nombre="Reggae"),
    Genero(id=24, nombre="Tango"),
    Genero(id=25, nombre="Disco"),
    Genero(id=26, nombre="Candombe"),
    Genero(id=27, nombre="Murga"),
    Genero(id=28, nombre="Marcha"),
    Genero(id=29, nombre="Cuarteto"),
    Genero(id=30, nombre="Funk"),
    Genero(id=31, nombre="Soul"),
    Genero(id=32, nombre="Gospel"),
    Genero(id=33, nombre="Fado"),
    Genero(id=34, nombre="Bolero"),
    Genero(id=35, nombre="Tropical"),
    Genero(id=36, nombre="Fusion"),
    Genero(id=37, nombre="Flamenco"),
    Genero(id=38, nombre="Bossa Nova"),
    Genero(id=39, nombre="Samba"),
    Genero(id=40, nombre="Bachata")]