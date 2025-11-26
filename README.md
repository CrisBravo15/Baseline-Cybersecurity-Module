# Baseline-Cybersecurity-Module

# Integrales y Roles
BCM
| Integrante | Rol en el Proyecto |
| :--- | :--- |
| **Bruno Alberto Gonzalez Cuellar** | Desarrollo de analizador_de_dominios.py, reporte_ia.py y encargado de realizar las pruebas necesarias |
| **Cristian Adan Bravo Guerra** | Desarrollo de recon.py, vuln_test.py, reporte_ia.py, encargado de mantener avances y de la investigación de nuevas funciones  |
| **Mikel Eduardo Jonguitud Hernandez** | Desarrollo de helpers.py, reporte_ia.py y también encargado de controlar las validaciones |

# Descripción general del proyecto
El proyecto tiene como propósito desarrollar un conjunto de scripts y procedimientos enfocados en fortalecer la seguridad de sistemas informáticos mediante la detección, análisis y protección de datos. A través de cuatro tareas complementarias, se busca implementar soluciones prácticas que permitan identificar vulnerabilidades, detectar eventos críticos, asegurar la integridad de los elementos del sistema y proteger información sensible mediante cifrado. El enfoque será principalmente defensivo, con la aplicación de herramientas y técnicas propias de un Blue Team, priorizando la ética, el uso de entornos controlados y datos sintéticos.

## 📁 Estructura del Repositorio
```md
Baseline-Cybersecurity-Module
├─ 📄 README.md  
├─ 📁 docs/                         
│   ├─ ai_plan.md
│   ├─ entregable_2.md
│   ├─ entregable_3.md
│   └─ entregable_4.md
├─ 📁 examples/                     
│   ├─ 📁 logs/                      
│   │   └─ bcm.log
│   ├─ 📁 outputs/                   
│   │   └─ github-com_2025-11-25_23-56-28/
│   │       ├─ 📄 reporte_ia.txt
│   │       ├─ 📁 output_add/        
│   │       │   └─ add_reporte.json
│   │       ├─ 📁 output_recon/      
│   │       │   └─ recon.json
│   │       └─ 📁 output_vuln/       
│   │           ├─ subdominios.json
│   │           └─ vuln_reporte.json
│   ├─ 📁 tarea1/                    
│   │   ├─ facebook/
│   │   │   └─ recon.json
│   │   └─ github/
│   │       └─ recon.json
│   ├─ 📁 tarea2/                    
│   │   ├─ facebook/
│   │   │   ├─ bcm.log
│   │   │   ├─ subdominios_facebook_com_2025-11-09_05-47-42.jsonl
│   │   │   └─ Vuln_reporte_facebook_com_2025-11-09_05-47-42.jsonl
│   │   └─ github/
│   │       ├─ bcm.log
│   │       ├─ subdominios_github_com_2025-11-09_05-55-31.jsonl
│   │       └─ Vuln_reporte_github_com_2025-11-09_05-55-31.jsonl
│   └─ 📁 tarea3/                    
│       ├─ Add_reporte_2025-11-21_20-12-15.jsonl
│       └─ Reporte_IA.txt
├─ 📁 prompts/                       
│   └─ prompt_v1.json
├─ 📁 proposals/                    
│   └─ propuesta.md
└─ 📁 src/                          
    ├─ main.py                       
    └─ 📁 scripts/                   
        ├─ analizador_de_dominios.py
        ├─ helpers.py
        ├─ recon.py
        ├─ reporte_ia.py
        └─ vuln_test.py
```
## Estado Final del Proyecto
**Estado Actual:** Las tres tareas de recolección de inteligencia y el **módulo de Reporte con IA** han sido **integrados con éxito**. El proyecto se encuentra en la fase de **pulido de detalles, pruebas finales** y **documentación** para la entrega definitiva.

### Tareas y Módulos Implementados

| Módulo | Archivo Principal | Tarea BCM | Funcionalidad Clave |
| :--- | :--- | :--- | :--- |
| **Módulo Recon** | `recon.py` | 1. Reconocimiento Básico | Obtención de **IP** con ping y extracción de IPs/servidores **DNS** con nslookup. |
| **Módulo Footprinting** | `vuln_test.py` | 2. Footprinting Pasivo | Consulta **DNS** (A, MX, NS, TXT), consulta **WHOIS**, y obtención de **subdominios** vía crt.sh. |
| **Módulo Reputación** | `analizador_de_dominios.py` | 3. Verificación de Reputación | Extracción de IPs y consulta de reputación con la **API de AbuseIPDB**. |
| **Módulo Reporte IA** | `reporte_ia.py` | **Módulo Final** | Combina todos los JSONs y usa **OpenAI** para generar un **análisis estructurado** (Resumen, Riesgos, Recomendaciones). |

## 📜 Declaración Ética

El equipo de **Baseline-Cybersecurity-Module (BCM)** declara su compromiso con la **ciberseguridad ética y responsable**.

* Todo el desarrollo se ha realizado con un **enfoque defensivo (Blue Team)**, orientado a la identificación de amenazas.
* Las herramientas de reconocimiento (`ping`, `nslookup`, `WHOIS`, `crt.sh`) se utilizan de forma **pasiva** y no generan tráfico intrusivo sobre el dominio objetivo.
* El módulo está diseñado únicamente con fines de **fortalecimiento de la seguridad** de sistemas propios o bajo consentimiento explícito, y no para fines maliciosos.

## 🔗 Enlaces Internos a Entregables
Los resultados y entregables clave se generan dinámicamente en la carpeta `outputs/` después de cada ejecución.
- [Plan de IA](docs/ai_plan.md)
- [Entregable 2](docs/entregable_2.md)
- [Entregable 3](docs/entregable_3.md)
- [Entregable 4](docs/entregable_4.md)
- [Entregable Final](docs/entregable_final.md)


