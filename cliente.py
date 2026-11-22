
"""Entidades y gestión de datos de clientes."""

from abc import ABC, abstractmethod
from excepciones import ClienteInvalidoError


class Entidad(ABC):
    """Clase abstracta general del sistema."""

    @abstractmethod
    def mostrar_informacion(self):
        """Devuelve la información de la entidad."""
        pass


class Cliente(Entidad):
    """Representa un cliente de Software FJ."""

    def __init__(
        self,
        identificacion,
        nombre,
        correo,
        telefono
    ):
        self.__identificacion = self.validar_texto(
            identificacion, "identificación"
        )
        self.__nombre = self.validar_texto(
            nombre, "nombre"
        )
        self.__correo = self.validar_correo(correo)
        self.__telefono = self.validar_telefono(telefono)

    @staticmethod
    def validar_texto(valor, campo):
        """Verifica que un campo de texto no esté vacío."""
        if not isinstance(valor, str) or not valor.strip():
            raise ClienteInvalidoError(
                f"El campo {campo} no puede estar vacío."
            )
        return valor.strip()

    @staticmethod
    def validar_correo(correo):
        """Comprueba la estructura básica del correo."""
        if not isinstance(correo, str):
            raise ClienteInvalidoError(
                "El correo debe ser texto."
            )

        correo = correo.strip()
        partes = correo.split("@")

        if (
            len(partes) != 2
            or not partes[0]
            or "." not in partes[1]
            or partes[1].startswith(".")
            or partes[1].endswith(".")
        ):
            raise ClienteInvalidoError(
                "El correo electrónico no es válido."
            )

        return correo

    @staticmethod
    def validar_telefono(telefono):
        """Comprueba que el teléfono tenga diez dígitos."""
        telefono = str(telefono).strip()

        if len(telefono) != 10 or not telefono.isdigit():
            raise ClienteInvalidoError(
                "El teléfono debe contener 10 dígitos."
            )

        return telefono

    @property
    def identificacion(self):
        return self.__identificacion

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def mostrar_informacion(self):
        """Presenta los datos del cliente."""
        return (
            f"Identificación: {self.identificacion}\n"
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.correo}\n"
            f"Teléfono: {self.telefono}"
        )

