# Reporte Final – Cambios Importantes en la Planeación

# Cambios en Tareas Técnicas
Originalmente, la planeación se enfocó en cuatro tareas complementarias (Detección, Análisis, Integridad y Cifrado de datos) con un enfoque en la implementación de soluciones defensivas de Blue Team. Se simplificó el alcance para enfocarse únicamente en las primeras tres tareas (Reconocimiento, Footprinting y Verificación de Reputación) para asegurar un entregable sólido y funcional dentro del tiempo establecido.
- Tarea Afectada: Las tareas de "Asegurar la integridad de los elementos del sistema" y "Proteger información sensible mediante cifrado" fueron eliminadas.
- Razón: El enfoque original era demasiado amplio para un módulo inicial. Se decidió concentrar los esfuerzos en construir un pipeline robusto de Threat Intelligence básico (recolección, análisis de IoCs e inteligencia de amenazas).
- Resultado: Se consolidó el proyecto en la ejecución secuencial de recon.py (Tarea 1), vuln_test.py (Tarea 2) y analizador_de_dominios.py (Tarea 3), culminando en un reporte de análisis.

# Cambios en el Uso de IA
El uso de la Inteligencia Artificial se modificó significativamente, pasando de ser una herramienta de apoyo potencial a convertirse en el eje central del entregable final y la capa de análisis profesional del proyecto.
- Propósito Modificado: El objetivo pasó de "generar un análisis básico" a "generar un análisis profesional y estructurado".
- Punto de Integración: Se creó el script reporte_ia.py específicamente para esta tarea. Este script se integra al final del flujo, unificando los resultados de los tres módulos anteriores (recon.json, vuln_reporte.json, add_reporte.json).
- Diseño de Prompts: El prompt se diseñó para que la IA actúe como un "analista de ciberseguridad experto", forzándola a generar apartados específicos de un informe profesional (Resumen Ejecutivo, Vulnerabilidades clasificadas por severidad, Análisis de IPs sospechosas, Correlación con MITRE ATT&CK, Impacto potencial y Recomendaciones priorizadas).

# Decisiones Técnicas Relevantes
1. Sistema de Logging (Módulo helpers.py)
- Decisión: Se implementó un sistema de logging centralizado usando la librería estándar de Python (logging) con un adaptador (ContextAdapter) y un formateador seguro (SafeFormatter).
-	Impacto: Permitió inyectar un EXECUTION_ID único por corrida (un UUID de 8 caracteres) en el log (bcm.log), facilitando la depuración y auditoría de cada análisis de forma independiente.
2. Estandarización de Salidas
-	Decisión: Se definió que todos los módulos de análisis generen archivos de salida en formato JSON (recon.json, vuln_reporte.json, add_reporte.json) y los almacenen en carpetas únicas basadas en el dominio y la marca de tiempo (outputs/{carpeta}/output_[...]).
-	Impacto: Esta estandarización fue crucial para el éxito del módulo reporte_ia.py, ya que permitió consumir y unificar fácilmente los resultados de las tres tareas en un solo prompt.
3. Encadenamiento de Flujo
-	Decisión: Se implementó una función (obtener_dominio() en vuln_test.py y analizador_de_dominios.py) para leer automáticamente el dominio objetivo y la carpeta de salida desde el reporte JSON de la tarea anterior.
-	Impacto: Permitió la ejecución secuencial y fluida del módulo, permitiendo la opción de usar el "dominio anterior" sin requerir la intervención del usuario, logrando la automatización del pipeline de análisis.

# Entregable Final
Logrado ✅
El resultado final del proyecto fue la construcción exitosa de un módulo de Threat Intelligence básico que es completamente funcional y automatizado. Este módulo es capaz de realizar tareas cruciales como:
1.	Reconocimiento pasivo del dominio objetivo.
2.	Footprinting para identificar subdominios y obtener información WHOIS.
3.	Verificación de reputación de los Indicadores de Compromiso (IPs) detectados.
La decisión de integrar la Inteligencia Artificial (IA) tuvo un impacto significativo, ya que elevó el entregable de ser una simple recolección de datos técnicos a un informe de ciberseguridad profesional. Esto permitió cumplir ampliamente el objetivo de análisis al proporcionar un resumen ejecutivo, clasificación de riesgos y recomendaciones estructuradas.

Aprendido
Las lecciones clave obtenidas durante el desarrollo fueron:
- Limitación del Alcance: Se confirmó la importancia de limitar el alcance en proyectos de ciberseguridad iniciales para asegurar la solidez y funcionalidad del producto principal.
- Estandarización de Datos: Se reconoció la necesidad crítica de estandarizar las salidas de datos en formato JSON. Esta decisión técnica fue fundamental para permitir la integración eficiente y fluida con herramientas avanzadas como los modelos de IA utilizados para la generación del reporte final.
