# Entregable 2 : Footprinting Pasivo

Este archivo contiene el avance de la **segunda tarea** del módulo: una herramienta de **footprinting pasivo** de un dominio. La herramienta recopila información pública sin interacción activa dirigida al objetivo, usando principalmente técnicas y fuentes como:

* **DNS** (resolución de registros A, NS, MX, TXT, etc.)
* **WHOIS** (información de registro del dominio)
* **crt.sh** (búsqueda de certificados para obtener subdominios observados)
* Consultas HTTP a servicios públicos (cuando aplica)

El propósito es reunir y almacenar subdominios, metadatos temporales y registros útiles para etapas posteriores de reconocimiento o para mantener un inventario de superficie de ataque.


## ¿Qué se implementó en este entregable?
1. Script principal `vuln_test.py` que es el conjunto de todas las técnicas pasivas.
2. Módulo `helpers.py` con utilidades compartidas (formato de fecha/hora, manejo de rutas `Path`, funciones de logging y helpers para guardar JSON/CSV).
3. Uso de librerías públicas para:
   * Resolver registros DNS.
   * Consultar WHOIS y parsear datos relevantes.
   * Consultar `crt.sh` (o consumir su API/endpoint público) para extraer posibles subdominios.
4. Escritura de resultados en `outputs/output_vuln/` con archivos de salida por objetivo, por ejemplo:

   * `subdominios_<target>_<timestamp>.jsonl`
   * `Vuln_reporte_<target>_<timestamp>.jsonl`
     
5. Manejo básico de logs para poder ejecutar el script desde distinto contexto (p. ej. desde `main` o ejecutándolo directamente).

## Formato de salida

Los archivos JSONL contienen estructuras similares a:

__subdominios_<target>_<timestamp>.jsonl__ :
```json
{"target": "ejemplo.com", "time": "2025-11-09_04-47-54", "subdomains": ["www.ejemplo.com","mail.ejemplo.com"]}
```

__Vuln_reporte_<target>_<timestamp>.jsonl__ :
```json
{"metadata":{"target":"ejemplo.com","run_time":"2025-11-09_04-47-54"},"dns":{"A":["blablabla"],"AAAA":["blablablablablablablablabla"],"MX":["blablablablablabla"],"NS":["blablablablablabla"],"TXT":["blablabla",]},"whois":{"register": "Ejemplo, blablabla","creation_date": "1997-03-29 05:00:00+00:00","expiration_date": "2034-03-30 04:00:00+00:00","name_servers":["EJEMPLO.COM"],"emails":["ejemplo@example.com"]},"subdomains":{"count": 554,"subdomains":["*_ejemplo1.com","*_ejemplo3.com","*_ejemplo2.com"]}}
```

## Ejecución de la tarea de manera controlada
Para ejecutar esta segunda tarea de manera controlada solo basta con ejecutar el comando __python vuln_test.py__ y la funcionalidad va a ser la misma, las salidas se colocarán en una carpeta superior a la carpeta donde se ejecute el script vuln_test.py

## Buenas prácticas y consideraciones éticas

* Esta herramienta **realiza footprinting pasivo**: sólo recopila información públicamente disponible, sin escaneo activo ni explotación.
* Antes de usarla contra dominios que no controlas, obtén autorización explícita.
* Respeta términos de uso de APIs y servicios (crt.sh, whois providers, etc.).


