from datetime import date
from error import LargoExcedidoError
from anuncio import Video, Display, Social

class Campania:
    def __init__(self, nombre: str, fecha_inicio: date, fecha_termino: date, anuncios_data: list):
        self.__anuncios = []
        self.__nombre = ""
        self.nombre = nombre
        self.__fecha_inicio = None
        self.__fecha_termino = None
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        
        self.__instanciar_anuncios(anuncios_data)

    def __instanciar_anuncios(self, anuncios_data: list):
        
        for ad in anuncios_data:
            tipo = ad.get("tipo", "").lower()
            if tipo == "video":
                instancia = Video(ad.get("url_archivo", ""), ad.get("url_clic", ""), ad.get("sub_tipo", ""), ad.get("duracion", 0))
            elif tipo == "display":
                instancia = Display(ad.get("ancho", 0), ad.get("alto", 0), ad.get("url_archivo", ""), ad.get("url_clic", ""), ad.get("sub_tipo", ""))
            elif tipo == "social":
                instancia = Social(ad.get("ancho", 0), ad.get("alto", 0), ad.get("url_archivo", ""), ad.get("url_clic", ""), ad.get("sub_tipo", ""))
            else:
                continue
            self.__anuncios.append(instancia)

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value: str):
        if len(value) > 250:
            raise LargoExcedidoError("El nombre de la campaña no puede superar los 250 caracteres.")
        self.__nombre = value

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, value: date):
        self.__fecha_inicio = value

    @property
    def fecha_termino(self):
        return self.__fecha_termino

    @fecha_termino.setter
    def fecha_termino(self, value: date):
        self.__fecha_termino = value

    @property
    def anuncios(self):
        return self.__anuncios

    def __str__(self):
        v_count = sum(1 for a in self.__anuncios if isinstance(a, Video))
        d_count = sum(1 for a in self.__anuncios if isinstance(a, Display))
        s_count = sum(1 for a in self.__anuncios if isinstance(a, Social))
        
        return f"Nombre de la campaña: {self.nombre}\nAnuncios: {v_count} Video, {d_count} Display, {s_count} Social"