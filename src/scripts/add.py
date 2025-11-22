import json
import re
import sys
from pathlib import Path
import recon
import requests
import vuln_test as vuln


# Configurar las salidas
ruta = Path.cwd()

if ruta.name == "scripts":
    OUTDIR = Path("../outputs/output_add")   
    OUTDIR.mkdir(parents=True, exist_ok=True)
else:
    OUTDIR = Path("outputs/output_add")
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


# Revisar reputación con AbuseIPDB
def consultar_reputacion_abuseipdb(ip):
    """Consulta la reputación de una IP usando la API de AbuseIPDB."""
    url = "https://api.abuseipdb.com/api/v2/check"

    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }

    headers = {
        "Accept": "application/json",
        "Key": "9619a6591152ab555ec813a197d0c64134d4b2283979b3b073c6442ad1afa5bd48c043770aa14485"
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        logs.debug(f"Respuesta de AbuseIPDB para {ip}: {data}")
        
        # Devuelve resultados estructurados
        if "data" in data:
            logs.info(f"Reputación obtenida para {ip}.")
            return {
                "ip": ip,
                "abuse_score": data["data"]["abuseConfidenceScore"],
                "total_reports": data["data"]["totalReports"],
                "es_maliciosa": data["data"]["abuseConfidenceScore"] > 0,
                "informacion_completa": data["data"]
            }
            
        else:
            logs.error(f"Respuesta no válida o error de AbuseIPDB para {ip}.")
            return {"error": "Respuesta no válida de AbuseIPDB", "raw": data}

    except Exception as e:
        return {"error": str(e)}

# Función principal
def main():
    """Realiza análisis completo de Threat Intelligence básico."""
    target = vuln.obtener_dominio()

    if target:
        print(f"Dominio obtenido automáticamente desde recon.json: {target}")
        logs.info("Dominio obtenido automáticamente desde recon.json")
    else:
        # Si no existe recon.json o está vacío, se pide al usuario
        target = input("Ingrese el nombre del dominio" + helpers.bold + " (ejemplo: ejemplo.com): " + helpers.default).strip()
        logs.info(f"Dominio ingresado manualmente: {target}")

    target = target.strip()
    logs.info(f"Iniciando consulta DNS para el dominio: {target}")
    query = vuln.query_dns(target)
    
    ipv4s = []

    for value in query.values():
        if isinstance(value, list):
            texto = " ".join(value)
            ipv4s.extend(re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', texto))

        elif isinstance(value, str):
            ipv4s.extend(re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', value))
    
    logs.info(f"IPs extraídas del registro DNS: {ipv4s}")
    print(f"\n Analizando IPs: {ipv4s}")
    analisis_final = {"IPs": ipv4s}
    analisis_final["ioCs"] = []
 
    # Procesar cada IP encontrada
    for ip in ipv4s:
        print(f"   → Procesando IP encontrada: {ip}")
        logs.info(f"Analizando la IP: {ip}")
        reputacion = consultar_reputacion_abuseipdb(ip)

        analisis_final["ioCs"].append({
            "ip": ip,
            "reputacion": reputacion
        })
    print("\n Análisis completado.")

    out_path = OUTDIR / f"Add_reporte_{helpers.horaact}.jsonl"
    # Guardar en JSONL (una línea por objeto)
    with out_path.open("w", encoding="utf-8") as fh:
        fh.write(json.dumps(analisis_final, ensure_ascii=False) + "\n")

    logs.debug(f"Reporte finalizado y guardado en {out_path}")
    print(f"Reporte finalizado y guardado en {out_path}")

if __name__ == "__main__":
    main()

