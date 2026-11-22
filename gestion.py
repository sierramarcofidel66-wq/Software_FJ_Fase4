
"""Administración de clientes y reservas en memoria."""

from cliente import Cliente
from reserva import Reserva

from excepciones import (
    ClienteInvalidoError,
    ReservaInvalidaError
)


class GestionSoftwareFJ:
    """Gestiona listas internas del sistema."""

    def __init__(self):
        self.__clientes = []
        self.__reservas = []

    def registrar_cliente(self, cliente):
        """Registra clientes evitando duplicados."""

        if not isinstance(cliente, Cliente):
            raise ClienteInvalidoError(
                "Se requiere un objeto Cliente."
            )

        for registrado in self.__clientes:
            if (
                registrado.identificacion
                == cliente.identificacion
            ):
                raise ClienteInvalidoError(
                    "Ya existe un cliente con esa identificación."
                )

        self.__clientes.append(cliente)
        return cliente

    def agregar_reserva(self, reserva):
        """Almacena reservas válidas en la lista."""

        if not isinstance(reserva, Reserva):
            raise ReservaInvalidaError(
                "Se requiere un objeto Reserva."
            )

        self.__reservas.append(reserva)
        return reserva

    @property
    def clientes(self):
        return tuple(self.__clientes)

    @property
    def reservas(self):
        return tuple(self.__reservas)
