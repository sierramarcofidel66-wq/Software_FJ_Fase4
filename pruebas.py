
"""Pruebas funcionales y manejo de excepciones."""

from cliente import Cliente

from servicios import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)

from reserva import Reserva
from gestion import GestionSoftwareFJ

from excepciones import (
    ErrorSistema,
    ClienteInvalidoError,
    ReservaInvalidaError
)

from registro import (
    registrar_evento,
    registrar_error
)


def ejecutar_pruebas():
    """Ejecuta las pruebas principales y complementarias."""

    sistema = GestionSoftwareFJ()

    registrar_evento("Inicio de las 10 pruebas.")

    print("PRUEBAS DE MANEJO DE EXCEPCIONES")

    realizadas = 0
    correctas = 0

    cliente = None
    sala = None
    equipo = None
    asesoria = None

    def probar(numero, descripcion, operacion,
               error_esperado=False):
        """Evalúa una operación y registra su resultado."""

        nonlocal realizadas, correctas

        realizadas += 1

        try:
            resultado = operacion()

        except (ErrorSistema, ValueError, TypeError) as error:
            registrar_error(error)

            if error_esperado:
                correctas += 1
                print(
                    f"Prueba {numero}: OK - "
                    f"error controlado ({descripcion}): {error}"
                )
            else:
                print(
                    f"Prueba {numero}: FALLÓ "
                    f"inesperadamente: {error}"
                )

        else:
            if error_esperado:
                print(
                    f"Prueba {numero}: FALLÓ, "
                    f"debía producir un error: {descripcion}"
                )
            else:
                correctas += 1

                print(
                    f"Prueba {numero}: OK - "
                    f"{descripcion}: {resultado}"
                )

                registrar_evento(
                    f"Prueba {numero} exitosa: {descripcion}"
                )

        finally:
            registrar_evento(
                f"Prueba {numero} finalizada."
            )

    # PRUEBA 1: Cliente válido
    def registrar_cliente_valido():
        nonlocal cliente

        cliente = sistema.registrar_cliente(
            Cliente(
                "123456789",
                "Carlos Martinez",
                "carlos@gmail.com",
                "3101234567"
            )
        )

        return cliente.nombre

    probar(
        1, "cliente válido", registrar_cliente_valido
    )

    # PRUEBA 2: Cliente con nombre vacío
    def registrar_cliente_invalido():
        try:
            Cliente(
                "987654321",
                "",
                "correo@gmail.com",
                "3101234567"
            )

        except ClienteInvalidoError as error:
            raise ClienteInvalidoError(
                "No fue posible registrar el cliente."
            ) from error

    probar(
        2,
        "nombre vacío",
        registrar_cliente_invalido,
        True
    )

    # PRUEBA 3: Reserva con duración negativa
    def reserva_duracion_invalida():
        try:
            Reserva(
                cliente,
                ReservaSala(20),
                -2
            )

        except ErrorSistema as error:
            raise ReservaInvalidaError(
                "La duración de la reserva no es válida."
            ) from error

    probar(
        3,
        "duración negativa",
        reserva_duracion_invalida,
        True
    )

    # PRUEBA 4: Alquiler de equipo válido
    def crear_equipo():
        nonlocal equipo

        equipo = AlquilerEquipo(
            "Computador portátil"
        )

        return equipo.describir_servicio()

    probar(
        4, "equipo válido", crear_equipo
    )

    # PRUEBA 5: Sala con capacidad negativa
    probar(
        5,
        "capacidad de sala negativa",
        lambda: ReservaSala(-5),
        True
    )

    # PRUEBA 6: Asesoría válida
    def crear_asesoria():
        nonlocal asesoria

        asesoria = AsesoriaEspecializada(
            "Programación Python"
        )

        return asesoria.describir_servicio()

    probar(
        6, "asesoría válida", crear_asesoria
    )

    # PRUEBA 7: Cálculo inválido
    sala = ReservaSala(20)

    probar(
        7,
        "cálculo con duración negativa",
        lambda: sala.calcular_costo(-3),
        True
    )

    # PRUEBA 8: Reserva exitosa
    def procesar_correctamente():
        reserva = sistema.agregar_reserva(
            Reserva(cliente, sala, 2)
        )

        reserva.confirmar()
        total = reserva.procesar()

        return f"Total ${total:,.0f}"

    probar(
        8, "reserva válida", procesar_correctamente
    )

    # PRUEBA 9: Procesamiento sin confirmación
    probar(
        9,
        "procesamiento sin confirmar",
        lambda: Reserva(
            cliente, equipo, 2
        ).procesar(),
        True
    )

    # PRUEBA 10: Cancelación duplicada
    def cancelar_dos_veces():
        reserva = sistema.agregar_reserva(
            Reserva(cliente, asesoria, 1)
        )

        reserva.cancelar()
        reserva.cancelar()

    probar(
        10,
        "cancelación duplicada",
        cancelar_dos_veces,
        True
    )

    # PRUEBAS ADICIONALES
    extras = [
        (
            "descuento inválido como texto",
            lambda: sala.calcular_costo(
                2, descuento="diez"
            )
        ),
        (
            "impuesto superior a 100",
            lambda: sala.calcular_costo(
                2, impuesto=120
            )
        ),
        (
            "cliente duplicado",
            lambda: sistema.registrar_cliente(cliente)
        ),
        (
            "tarifa negativa",
            lambda: ReservaSala(
                5, tarifa_hora=-100
            )
        ),
        (
            "correo inválido",
            lambda: Cliente(
                "55", "Ana",
                "correo-invalido",
                "3101234567"
            )
        ),
        (
            "parámetro faltante en reserva",
            lambda: Reserva(cliente, sala)
        )
    ]

    for descripcion, operacion in extras:
        try:
            operacion()

        except (ErrorSistema, ValueError, TypeError) as error:
            registrar_error(error)

            print(
                f"Prueba adicional OK: "
                f"{descripcion}: {error}"
            )

        else:
            raise AssertionError(
                f"No se detectó el error en: {descripcion}"
            )

    # Comprobación de descuento e impuesto
    assert sala.calcular_costo(
        2, descuento=10, impuesto=19
    ) == 107100.0

    # Servicio no disponible
    servicio_inactivo = AlquilerEquipo(
        "Proyector"
    )

    servicio_inactivo.cambiar_disponibilidad(False)

    try:
        Reserva(
            cliente, servicio_inactivo, 1
        )

    except ReservaInvalidaError as error:
        registrar_error(error)

        print(
            "Prueba adicional OK: "
            f"servicio no disponible: {error}"
        )

    else:
        raise AssertionError(
            "Se aceptó una reserva con servicio inactivo."
        )

    # Comprobación de listas internas
    assert len(sistema.clientes) == 1
    assert len(sistema.reservas) == 2

    registrar_evento(
        f"Pruebas finalizadas: {correctas}/{realizadas}."
    )

    print(
        f"RESUMEN: {correctas} de "
        f"{realizadas} pruebas correctas."
    )

    if correctas != realizadas:
        raise SystemExit(1)


if __name__ == "__main__":
    ejecutar_pruebas()
