
"""Gestión de servicios de la empresa Software FJ."""

from abc import ABC, abstractmethod
from numbers import Real
from math import isfinite

from excepciones import (
    ServicioNoDisponibleError,
    CalculoInvalidoError
)


class Servicio(ABC):
    """Clase abstracta general de los servicios."""

    def __init__(self, nombre, tarifa_hora):

        if not isinstance(nombre, str) or not nombre.strip():
            raise ServicioNoDisponibleError(
                "Debe indicar el nombre del servicio."
            )

        if (
            isinstance(tarifa_hora, bool)
            or not isinstance(tarifa_hora, Real)
            or not isfinite(tarifa_hora)
            or tarifa_hora <= 0
        ):
            raise ServicioNoDisponibleError(
                "La tarifa debe ser un número positivo."
            )

        self._nombre = nombre.strip()
        self._tarifa_hora = tarifa_hora
        self._disponible = True

    @property
    def disponible(self):
        """Consulta la disponibilidad del servicio."""
        return self._disponible

    def cambiar_disponibilidad(self, disponible):
        """Activa o desactiva un servicio."""

        if not isinstance(disponible, bool):
            raise ServicioNoDisponibleError(
                "La disponibilidad debe ser True o False."
            )

        self._disponible = disponible

    def validar_disponibilidad(self):
        """Verifica que el servicio esté disponible."""

        if not self._disponible:
            raise ServicioNoDisponibleError(
                "El servicio no está disponible."
            )

    @staticmethod
    def validar_duracion(horas):
        """Valida una duración positiva y finita."""

        if (
            isinstance(horas, bool)
            or not isinstance(horas, Real)
            or not isfinite(horas)
            or horas <= 0
        ):
            raise CalculoInvalidoError(
                "La duración debe ser un número positivo."
            )

    @abstractmethod
    def calcular_costo(
        self, horas, descuento=0, impuesto=0
    ):
        """Calcula el costo del servicio."""
        pass

    @abstractmethod
    def describir_servicio(self):
        """Devuelve la descripción del servicio."""
        pass

    @abstractmethod
    def validar_parametros(self):
        """Valida los parámetros particulares."""
        pass

    def calcular_total(
        self, horas, descuento=0, impuesto=0
    ):
        """Calcula el costo con impuestos y descuentos."""

        self.validar_disponibilidad()
        self.validar_parametros()
        self.validar_duracion(horas)

        for nombre, valor in [
            ("descuento", descuento),
            ("impuesto", impuesto)
        ]:
            if (
                isinstance(valor, bool)
                or not isinstance(valor, Real)
                or not isfinite(valor)
                or not 0 <= valor <= 100
            ):
                raise CalculoInvalidoError(
                    f"El {nombre} debe estar entre 0 y 100."
                )

        subtotal = self._tarifa_hora * horas

        subtotal_con_descuento = (
            subtotal * (1 - descuento / 100)
        )

        total = (
            subtotal_con_descuento * (1 + impuesto / 100)
        )

        if not isfinite(total):
            raise CalculoInvalidoError(
                "El cálculo produjo un valor no válido."
            )

        return round(total, 2)


class ReservaSala(Servicio):
    """Servicio especializado de reserva de salas."""

    def __init__(
        self, capacidad, tarifa_hora=50000
    ):
        super().__init__(
            "Reserva de sala", tarifa_hora
        )

        self.capacidad = capacidad
        self.validar_parametros()

    def validar_parametros(self):
        """Comprueba la capacidad de la sala."""

        if (
            type(self.capacidad) is not int
            or self.capacidad <= 0
        ):
            raise ServicioNoDisponibleError(
                "La capacidad de la sala no es válida."
            )

    def calcular_costo(
        self, horas, descuento=0, impuesto=0
    ):
        """Calcula el precio de la reserva de sala."""

        return self.calcular_total(
            horas, descuento, impuesto
        )

    def describir_servicio(self):
        """Devuelve las características de la sala."""

        return (
            f"Sala para {self.capacidad} personas."
        )


class AlquilerEquipo(Servicio):
    """Servicio especializado de alquiler de equipos."""

    def __init__(
        self, equipo, tarifa_hora=30000
    ):
        super().__init__(
            "Alquiler de equipo", tarifa_hora
        )

        self.equipo = equipo
        self.validar_parametros()

    def validar_parametros(self):
        """Verifica el nombre del equipo."""

        if (
            not isinstance(self.equipo, str)
            or not self.equipo.strip()
        ):
            raise ServicioNoDisponibleError(
                "Debe indicar el nombre del equipo."
            )

    def calcular_costo(
        self, horas, descuento=0, impuesto=0
    ):
        """Calcula el costo del alquiler."""

        return self.calcular_total(
            horas, descuento, impuesto
        )

    def describir_servicio(self):
        """Describe el equipo solicitado."""

        return (
            f"Alquiler del equipo: {self.equipo}."
        )


class AsesoriaEspecializada(Servicio):
    """Servicio especializado de asesorías."""

    def __init__(
        self, especialidad, tarifa_hora=80000
    ):
        super().__init__(
            "Asesoría especializada", tarifa_hora
        )

        self.especialidad = especialidad
        self.validar_parametros()

    def validar_parametros(self):
        """Comprueba la especialidad de la asesoría."""

        if (
            not isinstance(self.especialidad, str)
            or not self.especialidad.strip()
        ):
            raise ServicioNoDisponibleError(
                "Debe indicar la especialidad."
            )

    def calcular_costo(
        self, horas, descuento=0, impuesto=0
    ):
        """Calcula el costo de la asesoría."""

        return self.calcular_total(
            horas, descuento, impuesto
        )

    def describir_servicio(self):
        """Describe la asesoría solicitada."""

        return (
            f"Asesoría en {self.especialidad}."
        )
