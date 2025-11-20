# Integración del Script `recon.py`: Reconocimiento Inicial

## Funcionalidades Integradas

El script `recon.py` se enfoca en obtener información de infraestructura básica del dominio ingresado por el usuario, utilizando herramientas nativas del sistema operativo.

### 1. Obtención de Dirección IP (Utilizando `ping`)

* **Función Clave:** `obtener_ip_con_ping(domain)`
* **Descripción:** Ejecuta el comando `ping` contra el dominio para obtener su **dirección IP pública** y verificar la conectividad.
* **Inteligencia OS:** El script es capaz de detectar si está corriendo en **Windows** (`-n 1`) o **Linux/Unix** (`-c 1`) y ajusta la sintaxis del comando automáticamente.
* **Registro:** Captura tanto la IP resuelta como la salida completa (`raw`) del comando `ping`.

### 2. Consulta de Registros DNS (Utilizando `nslookup`)

* **Función Clave:** `obtener_dns_nslookup(domain)`
* **Descripción:** Ejecuta el comando `nslookup` para realizar consultas de DNS y extraer metadatos cruciales del dominio.
* **Datos Recolectados:**
    * **IPs Adicionales:** Lista todas las direcciones IP (`Address`) detectadas.
    * **Servidores DNS:** Identifica y lista los servidores de nombres (`Server`) utilizados para la resolución del dominio.

---

## Salida y Reporte

Toda la información recolectada se junta y se almacena en un formato estructurado para facilitar el análisis:

* **Ruta de Salida:** `outputs/output_recon/recon.json`
* **Formato:** JSON (JavaScript Object Notation), con identación para una fácil lectura.
* **Contenido:** Incluye el dominio, la IP obtenida por `ping`, la salida cruda de `ping`, y los detalles completos del `nslookup` (IPs detectadas y servidores DNS).
