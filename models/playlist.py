from pydantic import BaseModel
from typing import Optional, List




class Playlist(BaseModel):
    id: int
    nombre: str


# create a list of playlists
playlists = [
    Playlist(id=1, nombre="Rock"),
    Playlist(id=2, nombre="Pop"),
    Playlist(id=3, nombre="Cumbia"),
    Playlist(id=4, nombre="Reggaeton"),
    Playlist(id=5, nombre="Salsa"),
    Playlist(id=6, nombre="Bachata"),
    Playlist(id=7, nombre="Merengue"),
    Playlist(id=8, nombre="Vallenato"),
    Playlist(id=9, nombre="Balada"),
    Playlist(id=10, nombre="Ranchera"),
    Playlist(id=11, nombre="Banda"),
    Playlist(id=12, nombre="Ska"),
    Playlist(id=13, nombre="Punk"),
    Playlist(id=14, nombre="Metal"),
    Playlist(id=15, nombre="Jazz"),
    Playlist(id=16, nombre="Blues"),
    Playlist(id=17, nombre="Rap"),
    Playlist(id=18, nombre="Hip Hop"),
    Playlist(id=19, nombre="Folklore"),
    Playlist(id=20, nombre="Country"),
    Playlist(id=21, nombre="Clasica"),
    Playlist(id=22, nombre="Electronica"),
    Playlist(id=23, nombre="Reggae"),
    Playlist(id=24, nombre="Tango"),
    Playlist(id=25, nombre="Disco"),
    Playlist(id=26, nombre="Candombe"),
    Playlist(id=27, nombre="Murga"),
    Playlist(id=28, nombre="Marcha"),
    Playlist(id=29, nombre="Cuarteto"),
    Playlist(id=30, nombre="Funk"),
    Playlist(id=31, nombre="Soul"),
    Playlist(id=32, nombre="Gospel"),
    Playlist(id=33, nombre="Fado"),
    Playlist(id=34, nombre="Bolero"),
    Playlist(id=35, nombre="Tropical"),
    Playlist(id=36, nombre="Fusion"),
    Playlist(id=37, nombre="Flamenco"),
    Playlist(id=38, nombre="Bossa Nova"),
    Playlist(id=39, nombre="Samba"),
    Playlist(id=40, nombre="Bachata")]
