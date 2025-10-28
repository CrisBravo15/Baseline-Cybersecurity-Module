# 🧩 Propuesta técnica del proyecto PIA
## 🛡️ Título del proyecto
Baseline Cybersecurity Module

## 📌 Descripción general del proyecto
El proyecto tiene como propósito desarrollar un conjunto de scripts y procedimientos enfocados en fortalecer la seguridad de sistemas informáticos mediante la detección, análisis y protección de datos.
A través de cuatro tareas complementarias, se busca implementar soluciones prácticas que permitan identificar vulnerabilidades, detectar eventos críticos, asegurar la integridad de los elementos del sistema y proteger información sensible mediante cifrado.
El enfoque será principalmente defensivo, con la aplicación de herramientas y técnicas propias de un Blue Team, priorizando la ética, el uso de entornos controlados y datos sintéticos.

## 🧪 Tareas propuestas
-	Detección de eventos y logs del sistema
-	Detección de vulnerabilidades de un sistema o un sitio web 
-	Verificación de integridad de los datos

### 🔐 Tarea 1
**Título**: 
Detección de eventos y logs del sistema

**Propósito**: 
Analizar los registros del sistema para detectar eventos críticos o actividades sospechosas que puedan indicar incidentes de seguridad.
Generar reportes claros y estructurados que permitan al equipo de seguridad monitorear y reaccionar ante posibles amenazas.

**Rol o área relacionada**: 
SOC, DFIR, IT Security Officer

**Entradas esperadas**: 
Cantidad de eventos a recopilar, especificar si solo se desea ver eventos de aplicaciones, seguridad o sistema, o todos juntos, o varios como el usuario guste y también la opción de nombrar el archivo donde se realice el reporte de eventos en formato json
Ejemplos: 
Donde “-n” representa la cantidad de eventos a mostrar. Por default n=100
Donde “-nombre” representa el nombre del archivo donde se genera el reporte en formato json
-	python system_events.py -n -all -nombre (Muestra las 3 categorías de los eventos)
-	python system_events.py -n -sec -nombre (Muestra eventos de seguridad)
-	python system_events.py -n -sys -nombre (Muestra eventos de sistema)
-	python system_events.py -n -app -nombre (Muestra eventos de aplicaciones)
-	python system_events.py -n -asec -nombre (Muestra eventos de aplicaciones y seguridad)
-	python system_events.py -n -asys -nombre (Muestra eventos de aplicaciones y sistemas)
-	python system_events.py -n -ss -nombre (Muestra eventos de seguridad y de sistema)

**Salidas esperadas**: 
Registro de logs del sistema, eventos ocurridos en el transcurso del escaneo que pudieran ser maliciosos o estén marcados con una etiqueta de advertencia o una etiqueta crítica (error).
Ejemplos:
La cantidad de eventos depende de la opción ingresada por el usuario
Tabla de eventos del sistema. 
| ID |	LogName |	LevelDisplayName |	ProviderName |	TimeCreated |
|----|---------|------------------|--------------|-------------|
| 10013 |	System |	Advertencia |	Tcpip	| 10/09/2025 16:05 |
| 10041	| System	| Advertencia	| Netwtw10	| 20/10/2025 12:46 |

Tabla de eventos del sistema. 
| ID |	LogName |	LevelDisplayName |	ProviderName |	TimeCreated |
|----|---------|------------------|--------------|-------------|
| 10013 |	Security |	Advertencia |	Tcpip	| 10/09/2025 16:05 |
| 10041	| Security | Advertencia	| Netwtw10	| 20/10/2025 12:46 |

Tabla de eventos del sistema. 
| ID |	LogName |	LevelDisplayName |	ProviderName |	TimeCreated |
|----|---------|------------------|--------------|-------------|
| 10013 |	Applications |	Advertencia |	Tcpip	| 10/09/2025 16:05 |
| 10041	| Applications	| Advertencia	| Netwtw10	| 20/10/2025 12:46 |

**Descripción del procedimiento**: 
El usuario ejecutará este script usando las opciones programadas por el equipo para poder recibir un reporte sobre los eventos que tengan algún error o advertencia en su sistema, en el reporte se mostrará el ID del evento, su LogName al igual que el ProviderName que ayudaran al usuario a definir su curso de acción con este proceso

**Complejidad técnica**: 
Parsing (análisis de logs):Leer y extraer información relevante de archivos de registro con formatos variados (texto plano, CSV, XML o binario como .evtx).
Uso de expresiones regulares y librerías para interpretar y filtrar los datos correctamente.
Correlación de eventos: Relacionar eventos distintos para identificar patrones sospechosos o incidentes potenciales.
Automatización: Crear scripts que realicen recolección, filtrado y reporte de manera automática. Permitir que el análisis se ejecute periódicamente sin intervención manual.

**Controles éticos**:
 Vamos a realizar pruebas en entornos controlados propios para no filtrar ningún tipo de información sensible que pueda afectar a terceros, no se compartirán en los entregables datos sensibles que puedan afectar a alguno de los integrantes donde realicemos las pruebas del script

**Dependencias**:
 Librerías: subprocess, json, os, tkinter, PyQt / PySide. Comandos: Get-WinEvent, Where-Object. Entorno: Visual Studio Code. Variables de entorno: $env:USERPROFILE, $env:PATH, $env:SYSTEMROOT

### 🧭 Tarea 2
**Título**: 
Detección de vulnerabilidades de un sistema o sitio web

**Propósito**:  
Realizar un análisis pasivo y activo controlado para identificar configuraciones inseguras, servicios expuestos y vulnerabilidades conocidas en un dominio o IP objetivo, y generar un reporte estructurado que facilite la priorización de remediaciones. Se busca automatizar la recolección de información inicial (DNS/WHOIS/certificados/subdominios) y enlazarla con escaneos de vulnerabilidades para producir evidencia reproducible.

**Rol o área relacionada**: 
Red Team: prueba ofensiva controlada (encuentra fallas reales). Auditoría: revisión formal y documentada de seguridad. Vulnerability Management: proceso continuo de parcheo/priorización. SOC/DFIR: SOC detecta en tiempo real; DFIR investiga incidentes. Todos colaboran para priorizar, validar y remediar hallazgos.

**Entradas esperadas**: 
Se espera que el usuario ejecute el script con una ip o con el nombre del dominio que desea evaluar y generar un reporte de técnicas pasivas en formato json
Ejemplos: 
-	python web_eval.py --target ejemplo.com
-	python web_eval.py --target 191.01.01.01
  
**Salidas esperadas**: 
Ejemplos:
Dos archivos json, uno llamado reporte_<dominio o ip>_<fecha>.json que contiene todo lo recopilado del comando DNS (pasivo), otro archivo llamado subdominios_<dominio o ip>_<fecha>.json que contiene los subdominios registrados a esa ip o dominio, otro archivo .pem que es el certificado tls (en caso de que la página cuente con uno) y un archivo .log que registra las pruebas realizadas con fecha y con etiqueta de información

**Descripción del procedimiento**:
 El usuario ejecuta el comando utilizando la opción --target y espera unos minutos a que se termine de realizar todo el procedimiento, después se crearán los archivos, una carpeta llamada outputs que esté contenida en donde se ejecuta el programa y dentro de esta carpeta los reportes de dns y subdominios en formato.json y el archivo tls en caso de contar con uno, y en la carpeta principal se creara el archivo logs.log que mostrará todos los pasos realizados mediante con una marca de tiempo 

**Complejidad técnica**: 
Parsing: interpretar diversos formatos (salida de nmap XML/grepable, JSON de trivy, texto de nikto) y normalizarlos.
Correlación: unir datos de recon (DNS/WHOIS/subdominios/TLS) con resultados de escaneo para entender contexto (p. ej. qué subdominio sirve una app vulnerable).

**Controles éticos**: 
Ejecutar únicamente en entornos propios o con autorización expresa por escrito, no publicar ni compartir datos sensibles ni credenciales; en reportes, mostrar solo evidencia mínima necesaria (hashes, fingerprints) y recomendaciones sin exponer secretos y aplicar límites de tasa y ventanas de mantenimiento para evitar impacto en servicios en producción.

**Dependencias**: 
Librería: dnspython (dns.resolver), requests, python-whois (whois), ssl, socket, pathlib.
Comandos / herramientas externas (recomendadas): dns, whois, crt.sh, ssl
Variables de entorno y configuración: TARGET (dominio/IP), OUTDIR (directorio de salida; ejemplo outputs/), SCAN_PROFILE (p. ej. quick, full)

### 🧠 Tarea 3 (opcional)
**Título**: 
Verificación de integridad de los datos

**Propósito**:  
Verificar mediante hashes la integridad de los archivos para prevenir que se modifiquen cosas como los logs o los reportes realizados por las tareas anteriores, esto con el fin de evitar que un agente malicioso modifique los datos a su favor

**Rol o área relacionada**: 
DFIR, SOC, Threat Hunting, Blue team, Auditoría

**Entradas esperadas**: 
Se espera que el usuario ejecute el script #1 para que se genere un archivo .pickle y que este archivo funcione como base para verificar los próximos cambios, después de haber ejecutado por primera vez el script #1 el usuario ejecutara solo el archivo #2 para saber si los datos han sido manipulados
Ejemplos: 
-	python gen_hash.py (Script #1)
-	python check_hash.py (Script #2)

**Salidas esperadas**: 
Al ejecutar el script #1 Deben de aparecer la lista de documentos a los cuales se realizó el hasheo al igual que con el archivo .pickle donde se guardaron los hashes de todos los archivos
Al ejecutar el script #2 Aparece si no existen archivos modificados. En caso de que existan aparece una lista de cuales son y en caso de que se hayan agregado más archivos aparece una lista de cuales son
Ejemplos:
#Al ejecutar el script #1
Hasheado: info1.py
Hasheado: info2.txt
Hasheado: logs.log
Hasheado: json.json
Registro guardado en hashes.pickle
#Al ejecutar el script #2
Archivos modificados:
-	info1.py
-	logs.log
Archivos nuevos:
-	hashes.pickle

**Descripción del procedimiento**: 
El usuario ejecuta primero el script #1 en la carpeta donde desea resguardar la integridad de los datos para que se genere un archivo llamado hashes.pickle que funcionará como una clave para detectar algún cambio en los archivos. Este archivo llamado hashes.pickle lo usará el script #2 que al ejecutarlo el usuario tendrá una recopilación de archivos modificados o archivos nuevos en caso de que existan

**Complejidad técnica**: 
Parsing: interpretar diversos formatos (salida de nmap XML/grepable, JSON de trivy, texto de nikto) y normalizarlos.
Correlación: unir datos de recon (DNS/WHOIS/subdominios/TLS) con resultados de escaneo para entender contexto (p. ej. qué subdominio sirve una app vulnerable).

**Controles éticos**: 
Propósito Defensivo: La herramienta está diseñada únicamente para seguridad defensiva, privacidad: Solo lee el contenido de los archivos para generar hashes, 

**Dependencias**: 
Librería: hashlib, os, pickle.
Comandos: Ejecución de scipts
Variables de entorno y configuración: No se requieren variables de entorno específicas

---

## 👥 Asignación de roles del equipo
| Integrante | Rol o responsabilidad |
|------------|------------------------|
| Cristian| Desarrollar la primera tarea y realizar la interfaz |
| Mikel | Desarrollar la segunda tarea y realizar la interfaz |
| Bruno | Desarrollar la tercera tarea y trabajar en la documentación del proyecto |

---

## 🔐 Declaración ética y legal
Nosotros, los integrantes del equipo conformado por:
•	Cristian Adán Bravo Guerra
•	Mikel Eduardo Jonguitud Hernández
•	Bruno Alberto González Cuéllar
estudiantes del programa Seguridad en Tecnologías de la Información en la Universidad Autónoma de Nuevo León, declaramos que el presente Producto Integrador de Aprendizaje (PIA) se desarrolló cumpliendo con los principios éticos, legales y académicos establecidos por la institución y las normas aplicables en materia de tecnología y protección de datos.
1. Uso Ético y Responsable de la Información
Afirmamos que todas las actividades realizadas durante el desarrollo del proyecto se llevaron a cabo de forma ética, priorizando el respeto a la privacidad, la integridad y los derechos de las personas e instituciones.
No se ha hecho uso de información confidencial ni de bases de datos pertenecientes a entidades reales sin autorización expresa.
2. Protección de Datos y Seguridad
No se han empleado datos personales reales, credenciales, claves privadas, tokens, contraseñas ni información sensible de sistemas o usuarios reales.
Los datos utilizados para pruebas, simulaciones o demostraciones son sintéticos, anónimos o generados en entornos controlados y autorizados.
Se han aplicado medidas básicas de seguridad informática para evitar la exposición o mal uso de la información procesada.
3. Cumplimiento Legal y de Propiedad Intelectual
Se respeta la propiedad intelectual y licencias de los recursos, bibliotecas y herramientas empleadas durante el desarrollo del PIA.
4. Compromiso Ético y Profesional
Nos comprometemos a fomentar el uso ético, seguro y responsable de los conocimientos adquiridos en el ámbito de la seguridad informática.
Este proyecto tiene fines exclusivamente académicos y formativos, y no será utilizado con propósitos que puedan vulnerar la privacidad, integridad o disponibilidad de sistemas informáticos.

Lugar y fecha: Monterrey, N. L. 26 de octubre de 2025.

