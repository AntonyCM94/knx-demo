# knx_bus.py
import datetime

class BusKNXVirtual:
    def __init__(self):
        self.estado = False
        self.log = []
    
    def enviar_comando(self, origen, valor): # recibe comandos de los pulsados
        self.estado = valor
        evento = self._registrar_evento(origen, valor)
        print(evento)
        self.log.append(evento)
        self._guardar_log(evento)

    def leer_estado(self): # cambia el estado de la luz
        return self.estado
    
    def _registrar_evento(self, origen, valor):  # registra eventos en consola y los guarda en un log
        estado_str = 'ENCENDIDA' if valor else 'APAGADA'
        timestamp = datetime.datetime.now().strftime("[%H:%M:%S]")
        return f"{timestamp} {origen} activado -> Grupo 0/0/1 -> Luz {estado_str}"
    
    def _guardar_log(self, mensaje):
        with open("eventos.log", "a") as f:
            f.write(mensaje + "\n")