
from abc import ABC, abstractmethod
from numbers import Real


class Servicio(ABC):
    """Clase abstracta para los servicios de Software FJ."""

    def __init__(self, nombre, tarifa_hora):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El servicio debe tener un nombre.")

        if (
            isinstance(tarifa_hora, bool)
            or not isinstance(tarifa_hora, Real)
            or not 0 < tarifa_hora < float("inf")
        ):
            raise ValueError("La tarifa debe ser un número positivo.")

        self._nombre = nombre.strip()
        self._tarifa_hora = tarifa_hora

    @staticmethod
    def validar_duracion(horas):
        if (
            isinstance(horas, bool)
            or not isinstance(horas, Real)
            or not 0 < horas < float("inf")
        ):
            raise ValueError("La duración debe ser un número positivo.")

    @abstractmethod
    def calcular_costo(self, horas, descuento=0, impuesto=0):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    @abstractmethod
    def validar_parametros(self):
        pass

    def calcular_total(self, horas, descuento=0, impuesto=0):
        self.validar_duracion(horas)

        if not 0 <= descuento <= 100:
            raise ValueError("El descuento debe estar entre 0 y 100.")

        if not 0 <= impuesto <= 100:
            raise ValueError("El impuesto debe estar entre 0 y 100.")

        subtotal = self._tarifa_hora * horas
        subtotal *= (1 - descuento / 100)
        return round(subtotal * (1 + impuesto / 100), 2)


class ReservaSala(Servicio):
    """Servicio de reserva de salas."""

    def __init__(self, capacidad, tarifa_hora=50000):
        super().__init__("Reserva de sala", tarifa_hora)
        self.capacidad = capacidad
        self.validar_parametros()

    def validar_parametros(self):
        if type(self.capacidad) is not int or self.capacidad <= 0:
            raise ValueError("La capacidad de la sala no es válida.")

    def calcular_costo(self, horas, descuento=0, impuesto=0):
        return self.calcular_total(horas, descuento, impuesto)

    def describir_servicio(self):
        return f"Sala para {self.capacidad} personas."


class AlquilerEquipo(Servicio):
    """Servicio de alquiler de equipos."""

    def __init__(self, equipo, tarifa_hora=30000):
        super().__init__("Alquiler de equipo", tarifa_hora)
        self.equipo = equipo
        self.validar_parametros()

    def validar_parametros(self):
        if not isinstance(self.equipo, str) or not self.equipo.strip():
            raise ValueError("Debe indicar el nombre del equipo.")

    def calcular_costo(self, horas, descuento=0, impuesto=0):
        return self.calcular_total(horas, descuento, impuesto)

    def describir_servicio(self):
        return f"Alquiler del equipo: {self.equipo}."


class AsesoriaEspecializada(Servicio):
    """Servicio de asesoría especializada."""

    def __init__(self, especialidad, tarifa_hora=80000):
        super().__init__("Asesoría especializada", tarifa_hora)
        self.especialidad = especialidad
        self.validar_parametros()

    def validar_parametros(self):
        if (
            not isinstance(self.especialidad, str)
            or not self.especialidad.strip()
        ):
            raise ValueError("Debe indicar la especialidad.")

    def calcular_costo(self, horas, descuento=0, impuesto=0):
        return self.calcular_total(horas, descuento, impuesto)

    def describir_servicio(self):
        return f"Asesoría en {self.especialidad}."
