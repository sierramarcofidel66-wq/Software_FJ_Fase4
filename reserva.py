
"""Gestión de reservas de Software FJ."""

from cliente import Cliente
from servicios import Servicio
from excepciones import ReservaInvalidaError


class Reserva:
    """Relaciona cliente, servicio, duración y estado."""

    contador = 0

    def __init__(self, cliente, servicio, duracion):
        if not isinstance(cliente, Cliente):
            raise ReservaInvalidaError(
                "El cliente no es válido."
            )

        if not isinstance(servicio, Servicio):
            raise ReservaInvalidaError(
                "El servicio no es válido."
            )

        try:
            servicio.validar_duracion(duracion)
            servicio.validar_parametros()
            servicio.validar_disponibilidad()

        except Exception as error:
            raise ReservaInvalidaError(
                "Los parámetros de la reserva no son válidos."
            ) from error

        Reserva.contador += 1

        self.__codigo = Reserva.contador
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"

    @property
    def estado(self):
        return self.__estado

    def confirmar(self):
        """Confirma únicamente reservas pendientes."""
        if self.__estado != "Pendiente":
            raise ReservaInvalidaError(
                "Solo se pueden confirmar reservas pendientes."
            )

        self.__estado = "Confirmada"
        return "Reserva confirmada correctamente."

    def cancelar(self):
        """Cancela reservas que aún lo permitan."""
        if self.__estado == "Cancelada":
            raise ReservaInvalidaError(
                "La reserva ya está cancelada."
            )

        if self.__estado == "Procesada":
            raise ReservaInvalidaError(
                "No se puede cancelar una reserva procesada."
            )

        self.__estado = "Cancelada"
        return "Reserva cancelada correctamente."

    def procesar(self):
        """Calcula y procesa una reserva confirmada."""
        if self.__estado != "Confirmada":
            raise ReservaInvalidaError(
                "La reserva debe estar confirmada para procesarse."
            )

        total = self.__servicio.calcular_costo(
            self.__duracion
        )

        self.__estado = "Procesada"
        return total

    def mostrar_reserva(self):
        """Devuelve la información de la reserva."""
        return (
            f"Código: {self.__codigo}\n"
            f"Cliente: {self.__cliente.nombre}\n"
            f"Servicio: "
            f"{self.__servicio.describir_servicio()}\n"
            f"Duración: {self.__duracion} horas\n"
            f"Estado: {self.__estado}"
        )
