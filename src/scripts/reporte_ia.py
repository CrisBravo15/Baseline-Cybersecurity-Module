import json
from openai import OpenAI

client = OpenAI(api_key="-----------------------------------------------------------------------------------------------------------------------------")

def cargar_iocs(archivo):
    with open(archivo, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data["ioCs"]


def analizar_ioc(ip):
    prompt = f"""
Analiza esta IP con fines de ciberseguridad y devuelve:

- riesgo
- tipo_detectado
- descripcion
- tecnicas_mitre
- recomendaciones

IP objetivo: {ip}
"""

    resp = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un analista SOC experto."},
            {"role": "user", "content": prompt}
        ]
    )

    return resp.choices[0].message.content


archivo = "../outputs/output_add/Add_reporte_2025-11-21_20-12-15.jsonl"
lista = cargar_iocs(archivo)

for item in lista:
    ip = item["ip"]
    print(f"📌 Analizando {ip}")
    print(analizar_ioc(ip))
    print()
