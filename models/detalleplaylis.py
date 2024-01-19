from pydantic import BaseModel


class DetallePlaylist(BaseModel):
    id: int
    idPlaylist: int
    idCancion: int


# create a list of detalleplaylist
detalleplaylists = [
    DetallePlaylist(id=1, idPlaylist=1, idCancion=1),
    DetallePlaylist(id=2, idPlaylist=1, idCancion=2),
    DetallePlaylist(id=3, idPlaylist=1, idCancion=3),
    DetallePlaylist(id=4, idPlaylist=1, idCancion=4),
    DetallePlaylist(id=5, idPlaylist=1, idCancion=5),
    DetallePlaylist(id=6, idPlaylist=1, idCancion=6),
    DetallePlaylist(id=7, idPlaylist=1, idCancion=7),
    DetallePlaylist(id=8, idPlaylist=1, idCancion=8),
    DetallePlaylist(id=9, idPlaylist=1, idCancion=9),
    DetallePlaylist(id=10, idPlaylist=2, idCancion=1),
    DetallePlaylist(id=11, idPlaylist=2, idCancion=2),
    DetallePlaylist(id=12, idPlaylist=2, idCancion=3),
    DetallePlaylist(id=13, idPlaylist=2, idCancion=4),
    DetallePlaylist(id=14, idPlaylist=2, idCancion=5),
    DetallePlaylist(id=15, idPlaylist=2, idCancion=6),
    DetallePlaylist(id=16, idPlaylist=2, idCancion=7),
    DetallePlaylist(id=17, idPlaylist=2, idCancion=8),
    DetallePlaylist(id=18, idPlaylist=2, idCancion=9),
    DetallePlaylist(id=19, idPlaylist=3, idCancion=1),
    DetallePlaylist(id=20, idPlaylist=3, idCancion=2),
    DetallePlaylist(id=21, idPlaylist=3, idCancion=3),
    DetallePlaylist(id=22, idPlaylist=3, idCancion=4),
    DetallePlaylist(id=23, idPlaylist=3, idCancion=5),
    DetallePlaylist(id=24, idPlaylist=3, idCancion=6),
    DetallePlaylist(id=25, idPlaylist=3, idCancion=7)]