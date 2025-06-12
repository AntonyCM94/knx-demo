import threading
import time
from datetime import datetime

class Temporizador:
    def __init__(self, bus, segundos=10):
        self.bus = bus
        self.segundos = segundos
        self.timer = None

    def activar(self):
        if self.timer and self.timer.is_alive():
            print("[Temporizador] Ya esta en marcha. Esperando a que termine...")
            return

        print(f"[{self._hora()}] Temporizador activado -> Luz ENCENDIDA ({self.segundos}s)")
        self.bus.enviar_comando("Temporizador", True)

        self.timer = threading.Thread(target=self._cuenta_regresiva)
        self.timer.start()

    def _cuenta_regresiva(self):
        time.sleep(self.segundos)
        self.bus.enviar_comando("Temporizador", False)
        print(f"[{self._hora()}] Temporizador expirado -> Luz APAGADA")

    def _hora(self):
        return datetime.now().strftime("%H:%M:%S")