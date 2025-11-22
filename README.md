# Baseline-Cybersecurity-Module

# Equipo
BCM
- Bruno Alberto Gonzalez Cuellar
- Cristian Adan Bravo Guerra
- Mikel Eduardo Jonguitud Hernandez

# Descripción general del proyecto
El proyecto tiene como propósito desarrollar un conjunto de scripts y procedimientos enfocados en fortalecer la seguridad de sistemas informáticos mediante la detección, análisis y protección de datos. A través de cuatro tareas complementarias, se busca implementar soluciones prácticas que permitan identificar vulnerabilidades, detectar eventos críticos, asegurar la integridad de los elementos del sistema y proteger información sensible mediante cifrado. El enfoque será principalmente defensivo, con la aplicación de herramientas y técnicas propias de un Blue Team, priorizando la ética, el uso de entornos controlados y datos sintéticos.

# Tareas 
## Tarea 1: Reconocimiento del dominio
Esta tarea tiene como misión conocer datos como la IP con el comando de ping (-n 1 en Windows ó -c 1 en Linux/macOS) mediante expresiones regulares, también realiza un nslookup para tener más información como las ip asociadas al dominio, servidores dns que corresponden a la consulta 

## Tarea 2: Footprinting pasivo
Esta tarea realiza actividades de footprinting pasivo como consulta del DNS para obtener (A,AAAA,MX,NS,TXT), consulta WHOIS para obtener información como la fecha de creación, fecha de expiración, correos electrónicos de contacto, etc; tambien se realiza la búsqueda de subdominios que están asociados a un dominio

## Tarea 3: Verificación de reputación
Esta tarea realiza una consulta a la API de AbuseIPDB para conocer la reputación de las ips asociadas a un dominio, como puede ser el total de reportes, si es considerada maliciosa, etc.

# Estado del proyecto
Se integraron las 3 tareas al flujo principal, se están puliendo los ultimos detalles para la entrega final
