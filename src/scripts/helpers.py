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

# Función de Configuración e Inicialización
def setup_logging(execution_id: str):    
    # Configuración global básica
    logging.basicConfig(
        filename=ruta_log,
        level=logging.DEBUG,
        # Incluye %(module)s y el campo personalizado %(run_id)s
        format="%(asctime)s - %(levelname)s - [RUN_ID: %(run_id)s] - [Module: %(module)s] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        encoding="utf-8"
    )

    # Obtener el logger estándar (usando el nombre 'app' como base)
    logger_base = logging.getLogger('app')

    # Crear y devolver la instancia del adaptador con el contexto
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
