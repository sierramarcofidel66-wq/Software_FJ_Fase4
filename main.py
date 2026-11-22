
from cliente import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva

print("======================================")
print(" SISTEMA DE GESTIÓN - SOFTWARE FJ")
print("======================================")

try:
    cliente1 = Cliente(
        "123456789",
        "Carlos Martinez",
        "carlos@gmail.com",
        "3101234567"
    )

    print("\nCLIENTE REGISTRADO CORRECTAMENTE")
    print(cliente1.mostrar_informacion())

    sala = ReservaSala(20)
    equipo = AlquilerEquipo("Computador portátil")
    asesoria = AsesoriaEspecializada("Programación Python")

    print("\nSERVICIOS DISPONIBLES")

    for servicio in [sala, equipo, asesoria]:
        print("\n" + servicio.describir_servicio())
        print(f"Costo por 2 horas: ${servicio.calcular_costo(2):,.0f}")

    print("\nGESTIÓN DE RESERVAS")

    reserva1 = Reserva(cliente1, sala, 2)

    print(reserva1.mostrar_reserva())
    print(reserva1.confirmar())

    total = reserva1.procesar()
    print(f"Valor total: ${total:,.0f}")
    print(reserva1.mostrar_reserva())

    print("\nPRUEBA DE CANCELACIÓN")

    reserva2 = Reserva(cliente1, equipo, 3)
    print(reserva2.cancelar())
    print(reserva2.mostrar_reserva())

except (ValueError, TypeError) as error:
    print(f"Error controlado: {error}")




