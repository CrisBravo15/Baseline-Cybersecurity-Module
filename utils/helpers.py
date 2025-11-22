import logging
import os
from datetime import datetime
from pathlib import Path
import sys

# Configurar donde se guarda bcm.log
ruta = Path.cwd()

if ruta.name == "scripts":
    os.makedirs("../logs", exist_ok=True)
    ruta_log = "../logs/bcm.log"
else:
    os.makedirs("logs", exist_ok=True)
    ruta_log = "logs/bcm.log"    

# Adaptador para el RUN_ID 
class ContextAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        # Asegura que el diccionario extra esté presente
        if 'extra' not in kwargs:
            kwargs['extra'] = {}
        # Inyecta el run_id en el diccionario 'extra' para que el formato lo use
        kwargs['extra']['run_id'] = self.extra['run_id']
        return msg, kwargs

# Función de Configuración e Inicialización
def setup_logging(execution_id: str):
    logger_base = logging.getLogger('app')
    logger_base.setLevel(logging.DEBUG) # Establecer el nivel global del logger

    log_format = logging.Formatter(
        fmt="%(asctime)s - %(levelname)s - [RUN_ID: %(run_id)s] - [Module: %(module)s] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    file_handler = logging.FileHandler(ruta_log, encoding="utf-8")
    file_handler.setFormatter(log_format)
    file_handler.setLevel(logging.DEBUG) # Opcional: establecer el nivel del manejador

    if logger_base.hasHandlers():
        logger_base.handlers.clear()

    logger_base.propagate = False
    
    logger_base.addHandler(file_handler)

    logs = ContextAdapter(logger_base, {'run_id': execution_id})
    return logs

# Codigos para estilos
bold = "\033[1m"
verde = "\033[32m"
default = "\033[0m"
azul = "\033[34m"
rojo = "\033[31m"

# Hora actual
horaact = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Funcion para limpiar la consola
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


