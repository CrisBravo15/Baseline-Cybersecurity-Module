import subprocess
import json
import platform
import re
import os
from pathlib import Path
import sys

# Configurar las salidas
ruta = Path.cwd()

if ruta.name == "scripts":
    OUTDIR = Path("../outputs/output_recon")   
    OUTDIR.mkdir(parents=True, exist_ok=True)
else:
    OUTDIR = Path("outputs/output_recon")
    OUTDIR.mkdir(parents=True, exist_ok=True)

# Configuramos la ruta
module_path = Path(__file__).parent
if str(module_path) not in sys.path:
    sys.path.append(str(module_path))

# Inicializar el Logger
import helpers
import uuid
EXECUTION_ID = str(uuid.uuid4())[:8]
logs = helpers.setup_logging(execution_id=EXECUTION_ID)


def run_command(command):
    """Ejecuta un comando del SO y devuelve stdout como texto."""
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout.strip()

def obtener_ip_con_ping(domain):
    """Obtiene la IP haciendo ping al dominio."""
    sistema = platform.system()

    if sistema == "Windows":
        output = run_command(["ping", "-n", "1", domain])
        # Ejemplo: "Haciendo ping a example.com [93.184.216.34]..."
        match = re.search(r"\[([0-9\.]+)\]", output)
    else:
        output = run_command(["ping", "-c", "1", domain])
        # Ejemplo Linux: "PING example.com (93.184.216.34)"
        match = re.search(r"\(([\d\.]+)\)", output)

    if match:
        logs.info("Se logró obtener la IP")
        return match.group(1), output
    logs.error("Hubo un error al obtener la IP")
    return None, output

def obtener_dns_nslookup(domain):
    """Ejecuta nslookup y extrae registros relevantes."""
    output = run_command(["nslookup", domain])
    
    # Obtener Address y Name Servers
    ips = re.findall(r"Address:\s+([\d\.]+)", output)
    servers = re.findall(r"Server:\s+(.+)", output)

    logs.info("Se terminó de ejecutar nslookup")
    return {"ips_detectadas": ips, "servidores_dns": servers, "raw": output}

def main():
    domain = input("Ingresa el dominio a analizar: ").strip()

    logs.info("El usuario va a realizar un reconocimiento de " + domain)

    ip, ping_raw = obtener_ip_con_ping(domain)

    dns_info = obtener_dns_nslookup(domain)

    datos = {
        "dominio": domain,
        "ip_ping": ip,
        "salida_ping": ping_raw,
        "nslookup": dns_info
    }

    with open("outputs/output_recon/recon.json", "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
    
    print("Reporte finalizado y guardado en output/output_recon/recon.json")
    logs.info("Reporte finalizado y guardado en output/output_recon/recon.json")

if __name__ == "__main__":
    main()
