from pathlib import Path
import dns.resolver
import whois
import json
import requests
import sys

# Configurar las salidas
ruta = Path.cwd()

if ruta.name == "scripts":
    OUTDIR = Path("../outputs/output_vuln")   
    OUTDIR.mkdir(parents=True, exist_ok=True)
else:
    OUTDIR = Path("outputs/output_vuln")
    OUTDIR.mkdir(parents=True, exist_ok=True)

# Configuramos la ruta
module_path = Path(__file__).parent
if str(module_path) not in sys.path:
    sys.path.append(str(module_path))

# Importamos helpers despues de acomodar la ruta inicial
import helpers

# Configuracion de logs
logs = helpers.logging.getLogger("Vuln")

# Obtener dominio y más información de la tarea 1
def obtener_dominio():
    """
    Lee el archivorecon.json de la Tarea 1
    y devuelve el dominio si existe.
    """
    logs.info("Proceso de obtención del dominio anteriormente reconocido")
    recon_dir = Path("outputs/output_recon")

    json_path = recon_dir / "recon.json"

    # Obtener datos del json
    if json_path.exists():
        with json_path.open("r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                return data.get("dominio")
            except Exception:
                pass

    return None

# Scan DNS
def query_dns(domain):
    resolver = dns.resolver.Resolver()
    out = {}
    for q in ("A", "AAAA", "MX", "NS", "TXT"):
        try:
            answers = resolver.resolve(domain, q, lifetime=5)
            out[q] = [r.to_text().strip() for r in answers]
            logs.debug(f"Se consultó correctamente {q}")
        except Exception as e:
            out[q] = {"error": str(e)}
            logs.error(f"Hubo un error consultando {q}")
    return out

# Scan WHOIS
def query_whois(domain):
    try:
        w = whois.whois(domain)
        def safe(v):
            try:
                json.dumps(v)
                return v
            except Exception:
                try:
                    return str(v)
                except Exception:
                    return None
        logs.debug(f"Se consultó correctamente WHOIS")
        return {k: safe(v) for k, v in dict(w).items()}
    except Exception as e:
        logs.error("Hubo un error consultando WHOIS")
        return {"error": str(e)}

# Obtener subdominios con crt.sh
def subdomains_from_crtsh(domain):

    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        r = requests.get(url, timeout=15)
        if r.status_code != 200:
            logs.error("No se pudo conectar con el subdominio")
            return {"error": f"crt.sh regresó {r.status_code}"}
        data = r.json()
        subs = set()
        for entry in data:
            name = entry.get("name_value", "")
            for n in name.split("\n"):
                n = n.strip()
                if n and n.endswith(domain):
                    subs.add(n)
        subs_list = sorted(subs)
        logs.debug(f"Se terminó de consultar los subdominios de {domain} con CRT.SH")
        return {"count": len(subs_list), "subdomains": subs_list}
    except Exception as e:
        logs.error("Hubo un error al obtener informacion del subdominio")
        return {"error": str(e)}

def main():

    target = obtener_dominio()

    if target:
        print(f"Dominio obtenido automáticamente desde recon.json: {target}")
        logs.info("Dominio obtenido automáticamente desde recon.json")
    else:
        # Si no existe recon.json o está vacío, se pide al usuario
        target = input("Ingrese el nombre del dominio" + helpers.bold + " (ejemplo: ejemplo.com): " + helpers.default).strip()

    target = target.strip()

    target = target.strip()
    logs.info(f" Iniciando footprint pasivo para: {target}")

    # DNS
    logs.debug(f"Se comenzó a consultar {target} con el scan DNS")
    dns_res = query_dns(target)

    # WHOIS
    logs.debug(f"Se comenzó a consultar {target} con WHOIS")
    whois_res = query_whois(target)
    whois_clean = {k: whois_res.get(k) for k in ("registrar", "creation_date", "expiration_date", "name_servers", "emails")}

    # Subdominios (crt.sh)
    logs.debug(f"Se comenzó a consultar los subdominios de {target} con CRT.SH")
    crtsh_res = subdomains_from_crtsh(target)

    # Guardar subdominios por separado si vinieron bien
    subs_json_path = OUTDIR / f"subdominios_{target.replace('.','_')}_{helpers.horaact}.jsonl"
    
    if isinstance(crtsh_res, dict) and "subdomains" in crtsh_res:
        with subs_json_path.open("w", encoding="utf-8") as fh:
            for sub in crtsh_res["subdomains"]:
                obj = {"target": target, "time": helpers.horaact, "subdomain": sub}
                fh.write(json.dumps(obj, ensure_ascii=False) + "\n")
    else:
        with subs_json_path.open("w", encoding="utf-8") as fh:
            fh.write(json.dumps({"target": target, "time": helpers.horaact, "result": crtsh_res}, ensure_ascii=False) + "\n")
        logs.error(f"Subdominios: no listados o error. Resultado guardado en {subs_json_path}")

    # Reporte json total
    report = {
        "metadata": {"target": target, "run_time": helpers.horaact},
        "dns": dns_res,
        "whois": whois_clean,
        "subdomains": crtsh_res
    }

    out_path = OUTDIR / f"Vuln_reporte_{target.replace('.', '_')}_{helpers.horaact}.jsonl"
    # Guardar en JSONL (una línea por objeto)
    with out_path.open("w", encoding="utf-8") as fh:
        fh.write(json.dumps(report, ensure_ascii=False) + "\n")

    logs.debug(f"Reporte finalizado y guardado en {out_path}")
    print(f"Reporte finalizado y guardado en {out_path}")

if __name__ == "__main__": 
    main()
