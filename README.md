# Simulador Domotico KNX en Terminal 

Proyecto de demostración de una instalación KNX funcional, simulada 100% por terminal usando Python. Ideal para fines educativos, técnicos o como muestra de competencias en automatización y domótica.

## Simula lo siguiente:
        -- Pulsadores multiples 
        -- Actuador de conmutacion (luz virtual)
        -- Logica de escalera
        -- Temporizador (apagado automatico)
        -- Registro de eventos con timestamps
        -- Interfaz por terminal (menu simple y funcional)

## Estructura  
        -- knx_demo.py  #script principal
        -- knx_bus.py   # simulacion del bus KNX
        -- dispositivos.py  # class pulsador y actuador
        -- temporizador.py  # logica temporizador
        -- eventos.py   # log generado automaticamente

        ## modo de uso
        1. ejecuta el script 
        ```bash 
            python knx_demo.py

        o usa el .exe 

    # Requisitos
    Python 3.10+ (solo para código fuente)
    Compatible con Windows, Linux, Mac
    Sin necesidad de hardware KNX

LICENCIA
    Uso libre con fines educativos y demostrativos.
    Creado por Antony R Cachay Mendoza