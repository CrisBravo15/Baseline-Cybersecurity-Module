import logging
import os
from datetime import datetime
from pathlib import Path
import sys

# Configurar donde se guarda bcm.log
ruta = Path.cwd()

if ruta.name == "scripts":
    os.makedirs("../../logs", exist_ok=True)
    ruta_log = "../../logs/bcm.log"
else:
    os.makedirs("logs", exist_ok=True)
    ruta_log = "logs/bcm.log"    

# Adaptador para inyectar contexto (el RUN_ID) 
class ContextAdapter(logging.LoggerAdapter):
    """Adaptador que inyecta datos de contexto (como el run_id) en el log."""
    def process(self, msg, kwargs):
        # Asegura que el diccionario extra esté presente
        if 'extra' not in kwargs:
            kwargs['extra'] = {}
        # Inyecta el run_id en el diccionario 'extra' para que el formato lo use
        kwargs['extra']['run_id'] = self.extra['run_id']
        return msg, kwargs
    
#CUSTOM FORMATTER QUE NO SE ROMPE
class SafeFormatter(logging.Formatter):
    def format(self, record):
        run_id = getattr(record, "run_id", None)
        if run_id:
            record.run_id = f"{run_id} "  # lo mostramos entre corchetes
        else:
            record.run_id = ""  # no imprime nada
        return super().format(record)
    
# Función de Configuración e Inicialización
def setup_logging(execution_id: str):    
    # Configuración global básica
    # Handler para archivo
    handler = logging.FileHandler(ruta_log, encoding="utf-8")
    handler.setLevel(logging.DEBUG)

    # Aplicamos el formatter SEGURO
    formatter = SafeFormatter(
        "%(asctime)s - %(levelname)s - %(run_id)s%(module)s - %(message)s",
        "%Y-%m-%d %H:%M:%S"
    )
    handler.setFormatter(formatter)

    # Obtener el logger estándar (usando el nombre 'app' como base)
    # Configuramos logger raíz
    logger_base = logging.getLogger()
    logger_base.setLevel(logging.DEBUG)
    for h in logger_base.handlers[:]:
        logger_base.removeHandler(h)
    
    logger_base.addHandler(handler)

    # Crear y devolver la instancia del adaptador con el contexto
    logs = ContextAdapter(logging.getLogger("app"), {'run_id': execution_id})
    return logs

import uuid
import json
EXECUTION_ID = str(uuid.uuid4())[:8]
logs = setup_logging(execution_id=EXECUTION_ID)

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

