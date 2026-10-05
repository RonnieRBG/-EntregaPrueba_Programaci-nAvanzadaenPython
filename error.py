class Error(Exception):
    pass

class LargoExcedidoError(Error):
    """Excepción para cuando el nombre de la campaña supera los 250 caracteres."""
    pass

class SubTipoInvalidoError(Error):
    """Excepción para cuando se intenta asignar un subtipo no válido para el formato del anuncio."""
    pass
