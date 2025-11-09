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

# Configuración de logs
logging.basicConfig(
    filename=str(ruta_log),
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8"
)

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
