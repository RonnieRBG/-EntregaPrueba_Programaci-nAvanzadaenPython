from datetime import date
from campania import Campania
from error import SubTipoInvalidoError, LargoExcedidoError


datos_anuncios = [
    {
        "tipo": "video",
        "url_archivo": "https://ejemplo.com/video1.mp4",
        "url_clic": "https://ejemplo.com",
        "sub_tipo": "instream",
        "duracion": 15
    }
]


campania = Campania("Campaña inicial de Marketing", date.today(), date.today(), datos_anuncios)


try:
    nuevo_nombre = input("Ingrese el nuevo nombre para la campaña: ")
    nuevo_subtipo = input("Ingrese el nuevo subtipo para el anuncio de Video: ")

    campania.nombre = nuevo_nombre
    campania.anuncios[0].sub_tipo = nuevo_subtipo

    print("\n¡Datos actualizados exitosamente!")
    print(campania)

except (SubTipoInvalidoError, LargoExcedidoError, Exception) as e:
 
    with open("error.log", "a", encoding="utf-8") as f:
        f.write(f"Error detectado: {e}\n")
    print("\nOcurrió un error. Se ha registrado el mensaje en el archivo 'error.log'.")