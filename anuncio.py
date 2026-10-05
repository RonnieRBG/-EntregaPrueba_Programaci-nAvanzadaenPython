from abc import ABC, abstractmethod
from error import SubTipoInvalidoError

class Anuncio(ABC):
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str):
        self.__ancho = 1
        self.__alto = 1
        self.__url_archivo = ""
        self.__url_clic = ""
        self.__sub_tipo = ""
        
        
        self.ancho = ancho
        self.alto = alto
        self.url_archivo = url_archivo
        self.url_clic = url_clic
        self.sub_tipo = sub_tipo

    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self, value):
        self.__ancho = value if value > 0 else 1

    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, value):
        self.__alto = value if value > 0 else 1

    @property
    def url_archivo(self):
        return self.__url_archivo

    @url_archivo.setter
    def url_archivo(self, value):
        self.__url_archivo = value

    @property
    def url_clic(self):
        return self.__url_clic

    @url_clic.setter
    def url_clic(self, value):
        self.__url_clic = value

    @property
    def sub_tipo(self):
        return self.__sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, value):
        
        if isinstance(self, Anuncio) and type(self) is not Anuncio:
            if value not in type(self).SUB_TIPOS:
                raise SubTipoInvalidoError(f"El subtipo '{value}' no es válido para el formato {type(self).FORMATO}.")
        self.__sub_tipo = value

    @staticmethod
    def mostrar_formatos():
        print("FORMATO Video:\n==========")
        for t in Video.SUB_TIPOS: print(f"- {t}")
        print("\nFORMATO Display:\n==========")
        for t in Display.SUB_TIPOS: print(f"- {t}")
        print("\nFORMATO Social:\n==========")
        for t in Social.SUB_TIPOS: print(f"- {t}")

    @abstractmethod
    def comprimir_anuncio(self):
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
        pass


class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, url_archivo: str, url_clic: str, sub_tipo: str, duracion: int):
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo)
        self.__duracion = 5
        self.duracion = duracion

   
    @property
    def ancho(self):
        return self._Anuncio__ancho

    @ancho.setter
    def ancho(self, value):
        pass 

    @property
    def alto(self):
        return self._Anuncio__alto

    @alto.setter
    def alto(self, value):
        pass 

    @property
    def duracion(self):
        return self.__duracion

    @duracion.setter
    def duracion(self, value):
        self.__duracion = value if value > 0 else 5

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")


class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")


class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")