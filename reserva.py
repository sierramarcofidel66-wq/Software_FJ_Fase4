
from cliente import Cliente
from servicios import Servicio


class Reserva:
    """Gestiona las reservas de clientes y servicios."""

    contador = 0

    def __init__(self, cliente, servicio, duracion):
        if not isinstance(cliente, Cliente):
            raise TypeError("El cliente no es válido.")

        if not isinstance(servicio, Servicio):
            raise TypeError("El servicio no es válido.")

        servicio.validar_duracion(duracion)
        servicio.validar_parametros()

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
        if self.__estado != "Pendiente":
            raise ValueError(
                "Solo se pueden confirmar reservas pendientes."
            )

        self.__estado = "Confirmada"
        return "Reserva confirmada correctamente."

    def cancelar(self):
        if self.__estado == "Cancelada":
            raise ValueError("La reserva ya está cancelada.")

        if self.__estado == "Procesada":
            raise ValueError(
                "No se puede cancelar una reserva procesada."
            )

        self.__estado = "Cancelada"
        return "Reserva cancelada correctamente."

    def procesar(self):
        if self.__estado != "Confirmada":
            raise ValueError(
                "La reserva debe estar confirmada para procesarse."
            )

        total = self.__servicio.calcular_costo(
            self.__duracion
        )

        self.__estado = "Procesada"
        return total

    def mostrar_reserva(self):
        return (
            f"\nCódigo: {self.__codigo}"
            f"\nCliente: {self.__cliente.nombre}"
            f"\nServicio: {self.__servicio.describir_servicio()}"
            f"\nDuración: {self.__duracion} horas"
            f"\nEstado: {self.__estado}"
        )
