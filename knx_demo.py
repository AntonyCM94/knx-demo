from knx_bus import BusKNXVirtual
from dispositivos import Pulsador, Actuador
from temporizador import Temporizador

def mostrar_menu():
    print("\n=== SIMULADOR DOMOTICO KNX ===")
    print("[1] Pulsador 1")
    print("[2] Pulsador 2")
    print("[T] Activar luz con temporizador (10s)")
    print("[E] Ver estado de la luz")
    print("[Q] Salir")

if __name__ == "__main__":
    bus = BusKNXVirtual()
    pulsador1 = Pulsador("Pulsador 1", bus)
    pulsador2 = Pulsador("Pulsador 2", bus)
    actuador = Actuador(bus)
    temporizador = Temporizador(bus, segundos=10)

    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opcion:").strip().lower()

        if opcion == "1":
            pulsador1.pulsar()
        elif opcion == "2":
            pulsador2.pulsar()
        elif opcion == "t":
            temporizador.activar()
        elif opcion == "e":
            actuador.leer_estado()
        elif opcion == "q":
            print("\n[Salida] Cerrando simulador...")
            break
        else:
            print("\n[Error] Opcion no valida")