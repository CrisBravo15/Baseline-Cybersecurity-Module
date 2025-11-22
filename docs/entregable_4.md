# Flujo técnico consolidado
El sistema Baseline Cybersecurity Module (BCM) opera mediante un flujo de tres etapas secuenciales, orquestado por el script principal main.py. La información fluye principalmente a través de archivos JSON/JSONL intermedios ubicados en el directorio /outputs.

## Módulos Conectados:

- Recolección Básica (recon.py): Obtiene la IP principal y los registros DNS de un dominio, guardando la información en /outputs/output_recon/recon.json.

- Footprinting Pasivo (vuln_test.py): Lee recon.json, realiza consultas DNS extendidas, WHOIS, y escaneo de subdominios (crt.sh), generando un reporte en /outputs/output_vuln/Vuln_reporte_*.jsonl.

- Análisis Adicional (analizador_de_dominios.py - ADD): Utiliza las IPs obtenidas en etapas anteriores para verificar su reputación en servicios de Threat Intelligence (como AbuseIPDB) y consolida los Indicadores de Compromiso (IoCs) en un archivo JSONL en /outputs/output_add/Add_reporte_*.jsonl.

- Generación de Reporte de IA (reporte_ia.py): Procesa el reporte de IoCs del Módulo 3.

- Flujo de Información: El script recon.py genera un JSON que es leído por vuln_test.py y analizador_de_dominios.py para obtener el dominio. El script analizador_de_dominios.py genera un JSONL (Add_reporte_.jsonl) con los Indicadores de Compromiso (IoCs) y su reputación. El script reporte_ia.py lee este archivo Add_reporte_.jsonl, procesa cada IoC con la IA y muestra el análisis final en la consola (STDOUT).

## Salidas Generadas
Salidas Generadas: /outputs/output_recon/recon.json (Recolección básica) /outputs/output_vuln/Vuln_reporte_.jsonl (Footprinting) /outputs/output_add/Add_reporte_.jsonl (Análisis de IoCs/Reputación) logs/bcm.log (Logs estructurados con ID de ejecución)

##  IA integrada funcionalmente
Modelo/API utilizado: GPT-3.5-Turbo (a través de la API de OpenAI).


## Punto de integración
Punto de integración: La integración ocurre en el script reporte_ia.py. Se invoca después de que el script carga los Indicadores de Compromiso (IoCs) del archivo de reputación. La IA actúa como un Analista SOC experto que clasifica el riesgo, el tipo detectado, la descripción, las técnicas MITRE y las recomendaciones por cada IP.

## Ejemplo

Entrada: (Prompt para la IA): Analiza esta IP con fines de ciberseguridad y devuelve:
- riesgo
- tipo_detectado
- descripcion
- tecnicas_mitre
- recomendaciones IP objetivo: [IP del reporte]

Salida (Respuesta de GPT-3.5-Turbo): Riesgo: Alto Tipo_detectado: Botnet C2 (Command and Control) Descripción: [Análisis detallado de la IP y su amenaza] Tecnicas_mitre: Command and Control (TA0011), External Remote Services (T1133) Recomendaciones: Bloquear inmediatamente el tráfico hacia y desde esta IP en el firewall perimetral.

## Evidencia
Evidencia reproducible
Archivos de salida: La evidencia reproducible se encuentra en el directorio /examples.

## Logs
Logs estructurados: El archivo /logs/bcm.log contiene la trazabilidad completa, utilizando un ContextAdapter para registrar un RUN_ID único por ejecución.


## Observaciones
Qué falta por pulir antes de la entrega final:

- Formalizar la salida final del módulo reporte_ia.py, guardando el análisis en un archivo de reporte estructurado (Ej. PDF o HTML) en lugar de solo imprimir a consola.
- Mejorar el manejo de errores y la validación de las claves de API.
- Decisiones Técnicas Tomadas: Se utilizó GPT-3.5-Turbo por su eficiencia en el análisis textual y su relación coste-rendimiento. Se optó por JSONL para los reportes intermedios por su facilidad de procesamiento secuencial.
- Qué se aprendió en esta etapa: Se comprendió la complejidad de asegurar la serialización y el flujo de datos entre scripts independientes y la necesidad de un logging robusto para el debugging.