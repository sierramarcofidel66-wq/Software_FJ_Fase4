
from abc import ABC, abstractmethod


class Entidad(ABC):
    """Clase abstracta general del sistema."""

    @abstractmethod
    def mostrar_informacion(self):
        pass


class Cliente(Entidad):
    """Representa un cliente de Software FJ."""

    def __init__(self, identificacion, nombre, correo, telefono):
        self.__identificacion = self.validar_texto(
            identificacion, "identificación"
        )
        self.__nombre = self.validar_texto(nombre, "nombre")
        self.__correo = self.validar_correo(correo)
        self.__telefono = self.validar_telefono(telefono)

    @staticmethod
    def validar_texto(valor, campo):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError(
                f"El campo {campo} no puede estar vacío."
            )
        return valor.strip()

    @staticmethod
    def validar_correo(correo):
        if not isinstance(correo, str):
            raise ValueError("El correo debe ser un texto.")

        correo = correo.strip()

        if (
            correo.count("@") != 1
            or "." not in correo.split("@")[1]
            or not correo.split("@")[0]
        ):
            raise ValueError("El correo electrónico no es válido.")

        return correo

    @staticmethod
    def validar_telefono(telefono):
        telefono = str(telefono).strip()

        if not telefono.isdigit() or len(telefono) != 10:
            raise ValueError(
                "El teléfono debe contener exactamente 10 dígitos."
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
        return (
            f"Identificación: {self.identificacion}\n"
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.correo}\n"
            f"Teléfono: {self.telefono}"
        )
