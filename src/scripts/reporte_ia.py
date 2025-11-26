import json
import os
from openai import OpenAI
from pathlib import Path

client = OpenAI(api_key="------------------------------")

# Inicializar el Logger
import scripts.helpers as helpers
import uuid
EXECUTION_ID = str(uuid.uuid4())[:8]
logs = helpers.setup_logging(execution_id=EXECUTION_ID)

ultima = max((p for p in Path("outputs/").iterdir() if p.is_dir()),
            key=lambda p: p.stat().st_mtime,
            default=None)

ruta = Path.cwd()

def unir_reportes():
    carpetas = ["output_add","output_recon","output_vuln"]
    reportes = ""
    for x in carpetas:
        carpetas_f = ultima / Path(x)
        for archivo in os.listdir(carpetas_f):
            ruta_f = ruta / carpetas_f / archivo
            try:
                with open(str(ruta_f),"r",encoding="utf-8") as archivo_f:
                    reportes += json.dumps(json.load(archivo_f), ensure_ascii=False, indent=4) + "\n"
            except:
                logs.error(f"No se encontró el archivo de reporte en {carpetas_f}")
                pass
    return reportes

def realizar_prompt():
    datos = unir_reportes()

    if datos == "":
        logs.error("No se encontraron reportes hechos")
        print("No se encontraron reportes hechos")
        return None
        
    prompt = f"""
Tu tarea es analizar la información que te proporcionaré, la cual puede incluir:
- Reportes de escaneo de vulnerabilidades de un sitio web
- Resultados de herramientas como DNS, WHOIS, CRT.SH
- Reportes de IP's analizadas con AbuseIPDB
Quiero que generes un análisis profesional y estructurado con los siguientes apartados:
- Resumen ejecutivo (explicación clara y breve para alguien no técnico)
- Descripción técnica detallada de los hallazgos
- Vulnerabilidades identificadas, clasificadas por severidad (Crítica, Alta, Media, Baja)
- Análisis de IPs sospechosas (incluye reputación, riesgo, actividades asociadas, correlación con MITRE ATT&CK)
- Impacto potencial para el negocio/sistema
- Riesgos asociados con explicación técnica
- Evidencias basadas en los datos proporcionados
- Recomendaciones corregidas y priorizadas (por severidad + acciones inmediatas)
- Indicadores de Compromiso (IOCs) relevantes
- Conclusión final del estado de seguridad
Sé claro, organizado, profesional y específico
Aquí están los datos para analizar:
{datos}
            """

    resp = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un analista de ciberseguridad experto"},
            {"role": "user", "content": prompt}
        ]
    )

    ruta_archivo = ruta / ultima / Path("reporte_ia.txt")
    with open(ruta_archivo, "w") as f:
        f.write(resp.choices[0].message.content)
    return 0

if __name__ == "__main__":
    realizar_prompt()
