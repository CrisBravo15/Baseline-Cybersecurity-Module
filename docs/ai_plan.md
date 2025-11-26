# Propósito del Uso de IA en el Proyecto
En el módulo BCM se emplea inteligencia artificial para transformar múltiples reportes técnicos generados por las distintas pruebas de ciberseguridad en un análisis consolidado, claro y accionable. Cada una de las herramientas del sistema produce resultados en formato JSON (por ejemplo, escaneos de vulnerabilidades, consultas DNS, WHOIS, revisión de certificados, análisis de reputación de IPs, entre otros). La IA se utiliza para interpretar, correlacionar y resumir esta información dispersa, generando un reporte final integral que incluya conclusiones, riesgos detectados, explicación no técnica y recomendaciones priorizadas. Esto permite obtener un diagnóstico más completo y profesional sin depender únicamente del análisis manual.

# Punto del Flujo donde se Integrará
La IA se integra al final del flujo de ejecución del BCM.
Después de que todas las pruebas hayan sido realizadas y que el sistema haya generado sus respectivos reportes en JSON, el archivo orquestador junta estos archivos en un solo objeto de datos. En ese punto, antes de generar el informe final, BCM envía la información recopilada a la API del modelo de OpenAI junto con un prompt base.
El modelo procesa esos datos y devuelve un análisis profundo, el cual se convierte en el informe final entregado al usuario en un archivo txt.

# Tipo de Modelo/API a Utilizar
El proyecto utiliza el modelo gpt-3.5-turbo mediante la API de Chat Completions de OpenAI.
Este modelo permite procesar prompts extensos que incluyen resultados de pruebas técnicas y generar reportes estructurados con buena coherencia, alta velocidad y bajo costo, lo cual lo hace ideal para un flujo automatizado de análisis de ciberseguridad como el de BCM.


# Ejemplo de Prompt Inicial
"Eres un analista experto en ciberseguridad. 
A continuación recibirás resultados de diferentes pruebas realizadas a un dominio y a sus servicios asociados. 
La información proviene de herramientas como DNS Resolver, WHOIS, escáneres de vulnerabilidades, CRT.SH y consultas a AbuseIPDB.

Tu tarea es generar un análisis profesional con la siguiente estructura:
1. Resumen ejecutivo (explicación breve para un lector no técnico)
2. Vulnerabilidades detectadas (clasificadas por criticidad)
3. Riesgos asociados y su posible impacto
4. Correlación entre los diferentes reportes
5. Hallazgos informativos relevantes
6. Recomendaciones y acciones prioritarias
7. Conclusión general del estado de seguridad

A continuación se te envían los datos de todas las pruebas juntas:
{datos_recopilados}"
