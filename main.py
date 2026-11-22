
"""Programa principal de Software FJ."""

from cliente import Cliente

from servicios import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)

from reserva import Reserva
from gestion import GestionSoftwareFJ
from excepciones import ErrorSistema

from registro import (
    registrar_evento,
    registrar_error
)


def main():
    """Ejecuta una demostración completa del sistema."""

    sistema = GestionSoftwareFJ()

    registrar_evento("Inicio del programa principal.")

    print("=== SISTEMA DE GESTIÓN - SOFTWARE FJ ===")

    try:
        # Registro de cliente
        cliente = sistema.registrar_cliente(
            Cliente(
                "123456789",
                "Carlos Martinez",
                "carlos@gmail.com",
                "3101234567"
            )
        )

        print("\nCLIENTE REGISTRADO CORRECTAMENTE")
        print(cliente.mostrar_informacion())

        # Creación de servicios especializados
        servicios = [
            ReservaSala(20),
            AlquilerEquipo("Computador portátil"),
            AsesoriaEspecializada("Programación Python")
        ]

        print("\nSERVICIOS DISPONIBLES")

        for servicio in servicios:
            descripcion = servicio.describir_servicio()
            costo = servicio.calcular_costo(2)

            print(
                f"{descripcion} "
                f"Costo por 2 horas: ${costo:,.0f}"
            )

        # Primera reserva
        primera = sistema.agregar_reserva(
            Reserva(cliente, servicios[0], 2)
        )

        print("\nGESTIÓN DE RESERVAS")
        print(primera.mostrar_reserva())

        print(primera.confirmar())

        total = primera.procesar()
        print(f"Valor total: ${total:,.0f}")

        print(primera.mostrar_reserva())

        # Segunda reserva: cancelación
        segunda = sistema.agregar_reserva(
            Reserva(cliente, servicios[1], 3)
        )

        print("\nPRUEBA DE CANCELACIÓN")
        print(segunda.cancelar())
        print(segunda.mostrar_reserva())

        registrar_evento(
            "Programa principal finalizado correctamente."
        )

    except (ErrorSistema, ValueError, TypeError) as error:
        registrar_error(error)
        print(f"Error controlado: {error}")

    finally:
        print("\nFin de la ejecución del programa.")


if __name__ == "__main__":
    main()

"""Programa principal de Software FJ."""

from cliente import Cliente

from servicios import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)

from reserva import Reserva
from gestion import GestionSoftwareFJ
from excepciones import ErrorSistema

from registro import (
    registrar_evento,
    registrar_error
)


def main():
    """Ejecuta una demostración completa del sistema."""

    sistema = GestionSoftwareFJ()

    registrar_evento("Inicio del programa principal.")

    print("=== SISTEMA DE GESTIÓN - SOFTWARE FJ ===")

    try:
        # Registro de cliente
        cliente = sistema.registrar_cliente(
            Cliente(
                "123456789",
                "Carlos Martinez",
                "carlos@gmail.com",
                "3101234567"
            )
        )

        print("\nCLIENTE REGISTRADO CORRECTAMENTE")
        print(cliente.mostrar_informacion())

        # Creación de servicios especializados
        servicios = [
            ReservaSala(20),
            AlquilerEquipo("Computador portátil"),
            AsesoriaEspecializada("Programación Python")
        ]

        print("\nSERVICIOS DISPONIBLES")

        for servicio in servicios:
            descripcion = servicio.describir_servicio()
            costo = servicio.calcular_costo(2)

            print(
                f"{descripcion} "
                f"Costo por 2 horas: ${costo:,.0f}"
            )

        # Primera reserva
        primera = sistema.agregar_reserva(
            Reserva(cliente, servicios[0], 2)
        )

        print("\nGESTIÓN DE RESERVAS")
        print(primera.mostrar_reserva())

        print(primera.confirmar())

        total = primera.procesar()
        print(f"Valor total: ${total:,.0f}")

        print(primera.mostrar_reserva())

        # Segunda reserva: cancelación
        segunda = sistema.agregar_reserva(
            Reserva(cliente, servicios[1], 3)
        )

        print("\nPRUEBA DE CANCELACIÓN")
        print(segunda.cancelar())
        print(segunda.mostrar_reserva())

        registrar_evento(
            "Programa principal finalizado correctamente."
        )

    except (ErrorSistema, ValueError, TypeError) as error:
        registrar_error(error)
        print(f"Error controlado: {error}")

    finally:
        print("\nFin de la ejecución del programa.")


if __name__ == "__main__":
    main()
