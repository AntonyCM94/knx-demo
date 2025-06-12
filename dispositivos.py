import knx_bus

class Pulsador:
    def __init__(self, nombre, bus):
        self.nombre = nombre
        self.bus = bus

    def pulsar(self):
        nuevo_estado = not self.bus.leer_estado()
        self.bus.enviar_comando(self.nombre, nuevo_estado)

class Actuador:
    def __init__(self, bus):
        self.bus = bus

    def leer_estado(self):
        estado = self.bus.leer_estado()
        estado_str = 'ENCENDIDA' if estado else 'APAGADA'
        print(f"[Actuado] luz actualmente {estado_str}")
        return estado