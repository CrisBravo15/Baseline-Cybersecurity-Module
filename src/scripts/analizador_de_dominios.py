import json
import re
import sys
from pathlib import Path
import requests
import scripts.vuln_test as vuln

# Inicializar el Logger
import scripts.helpers as helpers
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
        "Key": "-----------------------"
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
    
def validar_dominio(domain: str) -> bool:
    patron = r"^(?!:\/\/)([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"
    return re.match(patron, domain) is not None

# Función principal
def main():
    """Realiza análisis completo de Threat Intelligence básico."""
    while True:
        opcion = input("Usar dominio anterior? (Si/No): ").lower()
        
        if opcion == "si" or opcion == "sí":
            logs.info("Proceso de obtención del dominio anteriormente reconocido")
            target, carpeta = vuln.obtener_dominio()
            
            if not target:
                print("No se pudo obtener el dominio")
                target = input("Ingrese el nombre del dominio" + helpers.bold + " (ejemplo: ejemplo.com): " + helpers.default).strip()
                carpeta = target.replace(".","-") + f"_{helpers.horaact}"
            break
        else:
            target = input("Ingrese el dominio a analizar (ejemplo: ejemplo.com): ").strip()
            carpeta = target.replace(".", "-") + f"_{helpers.horaact}"

    # Validación del dominio
    if not validar_dominio(target):
        print(f"\nDominio inválido: {target}")
        print("Ejemplo válido: google.com | servicios.empresa.mx")
        logs.error(f"Dominio inválido ingresado: {target}")
        return

    logs.info(f"Dominio válido recibido: {target}")
    
    ruta = Path.cwd()
    if ruta.name == "scripts":
        OUTDIR = Path(f"../outputs/{carpeta}/output_add")   
        OUTDIR.mkdir(parents=True, exist_ok=True)
    else:
        OUTDIR = Path(f"{carpeta}/output_add")
        OUTDIR.mkdir(parents=True, exist_ok=True)

    # Configuramos la ruta
    module_path = Path(__file__).parent
    if str(module_path) not in sys.path:
        sys.path.append(str(module_path))

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
    analisis_final = {"IPs": ipv4s}
    analisis_final["ioCs"] = []
 
    # Procesar cada IP encontrada
    for ip in ipv4s:
        logs.info(f"Analizando la IP: {ip}")
        reputacion = consultar_reputacion_abuseipdb(ip)

        analisis_final["ioCs"].append({
            "ip": ip,
            "reputacion": reputacion
        })

    out_path = OUTDIR / f"add_reporte.json"
    # Guardar en JSONL (una línea por objeto)
    with out_path.open("w", encoding="utf-8") as fh:
        json.dump(analisis_final, fh, ensure_ascii=False, indent=4)

    logs.debug(f"Reporte finalizado y guardado en {out_path}")
    print("\nAnálsis completado de reputacion de las ips del dominio")
    print(f"Reporte finalizado y guardado en {out_path}")

if __name__ == "__main__":
    main()

