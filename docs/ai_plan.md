# Propósito del Uso de IA en el Proyecto
El propósito principal de integrar la Inteligencia Artificial es automatizar y escalar el análisis de los datos de reconocimiento (reconnaissance) y vulnerabilidades. La IA permite procesar rápidamente grandes volúmenes de datos semiestructurados y no estructurados (como registros JSONL de subdominios, respuestas DNS crudas y outputs de ping/nslookup) para identificar patrones, anomalías y advertencias de ciberseguridad que podrían pasarse por alto en una revisión manual o que consumirían demasiado tiempo a un analista. Esto incluye la detección de entornos de desarrollo expuestos, errores de configuración de DNS críticos, y la cuantificación de la superficie de ataque.

# Punto del Flujo donde se Integrará
La IA se integrará en la fase de Post-Procesamiento y Reporte Automatizado.
- Ingesta de Datos: Se cargan los archivos de reporte (subdominios_github_com...jsonl, Vuln_reporte_github_com...jsonl, recon.json) generados por las herramientas de reconocimiento.
- Integración de IA: El contenido completo de los archivos se pasa a la API del modelo de lenguaje, sirviendo como el contexto fundamental para el análisis.
- Salida Estructurada: La IA genera un resumen estructurado y clasificado, resaltando vulnerabilidades, advertencias y observaciones clave, listo para ser entregado al equipo de seguridad.

# Tipo de Modelo/API a Utilizar
Se utilizará un Modelo de Lenguaje Grande (LLM) de la familia Gemini (Flash 2.5), accesible a través de su API.
Razón de la Elección: Este tipo de modelo es ideal por su avanzada capacidad de razonamiento y comprensión contextual para interpretar y sintetizar información técnica y compleja contenida en los reportes de texto y JSON. Además, tiene la capacidad de manejar archivos como entrada (visión multimodal sobre documentos) y generar una respuesta con el tono analítico y enfocado en ciberseguridad requerido.


#Ejemplo de Prompt Inicial
El prompt inicial debe ser detallado para guiar a la IA a realizar el análisis de seguridad deseado:
- "Eres un analista de ciberseguridad experto. Analiza el contenido completo de los archivos adjuntos (subdominios, DNS/WHOIS y recon) para el dominio 'github.com'. Identifica y cataloga todas las vulnerabilidades, advertencias y observaciones de seguridad."
- "Tu reporte debe incluir las siguientes secciones: 1. Advertencias críticas de DNS (e.g., fallas en AAAA/TXT). 2. Superficie de Ataque (menciona la cuenta de subdominios y resalta los entornos de desarrollo/staging o servicios sensibles como VPN/API/SMTP). 3. Hallazgos del WHOIS (puntos que un atacante podría usar). Proporciona una conclusión clara sobre la seguridad general del dominio basada en estos datos. Utiliza el formato Markdown para facilitar la lectura."