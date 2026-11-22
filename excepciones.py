
"""Excepciones específicas del sistema Software FJ."""


class ErrorSistema(Exception):
    """Error general del sistema."""
    pass


class ClienteInvalidoError(ErrorSistema):
    """Error por información incorrecta de un cliente."""
    pass


class ServicioNoDisponibleError(ErrorSistema):
    """Error de disponibilidad o parámetros de servicios."""
    pass


class ReservaInvalidaError(ErrorSistema):
    """Error por una reserva u operación no permitida."""
    pass


class CalculoInvalidoError(ErrorSistema):
    """Error por parámetros incorrectos en cálculos."""
    pass

