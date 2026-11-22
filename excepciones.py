
class ErrorSistema(Exception):
    """Excepción general de Software FJ."""
    pass


class ClienteInvalidoError(ErrorSistema):
    """Error relacionado con datos de clientes."""
    pass


class ServicioNoDisponibleError(ErrorSistema):
    """Error relacionado con servicios."""
    pass


class ReservaInvalidaError(ErrorSistema):
    """Error relacionado con las reservas."""
    pass


class CalculoInvalidoError(ErrorSistema):
    """Error relacionado con cálculos."""
    pass
