
from cliente import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from registro import registrar_evento, registrar_error
from excepciones import (
    ClienteInvalidoError,
    ReservaInvalidaError
)


def ejecutar_pruebas():
    print("\nPRUEBAS DE MANEJO DE EXCEPCIONES")

    registrar_evento("Inicio de las pruebas del sistema.")

    # Prueba 1: cliente válido
    try:
        cliente = Cliente(
            "123456789",
            "Carlos Martinez",
            "carlos@gmail.com",
            "3101234567"
        )
    except ValueError as error:
        registrar_error(error)
        print("Error:", error)
    else:
        print("Prueba 1: Cliente registrado correctamente.")
        registrar_evento("Cliente registrado correctamente.")
    finally:
        print("Prueba 1 finalizada.")

    # Prueba 2: cliente con nombre vacío
    try:
        Cliente(
            "987654321",
            "",
            "correo@gmail.com",
            "3101234567"
        )
    except ValueError as error:
        try:
            raise ClienteInvalidoError(
                "No fue posible registrar el cliente."
            ) from error
        except ClienteInvalidoError as nuevo_error:
            registrar_error(nuevo_error)
            print("Prueba 2: Error controlado:", nuevo_error)
    finally:
        print("Prueba 2 finalizada.")

    # Prueba 3: reserva inválida
    try:
        sala = ReservaSala(20)
        reserva = Reserva(cliente, sala, -2)
        reserva.confirmar()
    except ValueError as error:
        try:
            raise ReservaInvalidaError(
                "La duración de la reserva no es válida."
            ) from error
        except ReservaInvalidaError as nuevo_error:
            registrar_error(nuevo_error)
            print("Prueba 3: Error controlado:", nuevo_error)
    finally:
        print("Prueba 3 finalizada.")

    # Prueba 4: servicio válido de alquiler de equipos
    try:
        equipo = AlquilerEquipo("Computador portátil")
        print("Prueba 4: Servicio creado correctamente.")
        registrar_evento("Prueba 4 exitosa.")
    except (ValueError, TypeError) as error:
        registrar_error(error)
        print("Prueba 4: Error:", error)

    # Prueba 5: servicio con capacidad incorrecta
    try:
        ReservaSala(-5)
        print("Prueba 5: Servicio creado.")
    except (ValueError, TypeError) as error:
        registrar_error(error)
        print("Prueba 5: Error controlado:", error)

    # Prueba 6: asesoría válida
    try:
        asesoria = AsesoriaEspecializada("Programación Python")
        print("Prueba 6: Asesoría creada correctamente.")
        registrar_evento("Prueba 6 exitosa.")
    except (ValueError, TypeError) as error:
        registrar_error(error)
        print("Prueba 6: Error:", error)

    # Prueba 7: cálculo de costo inválido
    try:
        sala = ReservaSala(20)
        sala.calcular_costo(-3)
        print("Prueba 7: Cálculo realizado.")
    except (ValueError, TypeError) as error:
        registrar_error(error)
        print("Prueba 7: Error controlado:", error)

    # Prueba 8: reserva exitosa
    try:
        reserva = Reserva(cliente, sala, 2)
        reserva.confirmar()
        total = reserva.procesar()

        print(
            f"Prueba 8: Reserva procesada. Total: ${total:,.0f}"
        )
        registrar_evento("Prueba 8 exitosa.")
    except (ValueError, TypeError) as error:
        registrar_error(error)
        print("Prueba 8: Error:", error)

    # Prueba 9: intento de procesar sin confirmar
    try:
        reserva = Reserva(cliente, equipo, 2)
        reserva.procesar()
        print("Prueba 9: Reserva procesada.")
    except (ValueError, TypeError) as error:
        registrar_error(error)
        print("Prueba 9: Error controlado:", error)

    # Prueba 10: cancelar dos veces la misma reserva
    try:
        reserva = Reserva(cliente, asesoria, 1)
        reserva.cancelar()
        reserva.cancelar()
        print("Prueba 10: Reserva cancelada.")
    except (ValueError, TypeError) as error:
        registrar_error(error)
        print("Prueba 10: Error controlado:", error)

    registrar_evento("Finalización de las pruebas.")


if __name__ == "__main__":
    ejecutar_pruebas()
