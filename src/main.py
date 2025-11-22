import pyfiglet
import scripts.helpers as helpers
import scripts.vuln_test as vuln
import scripts.recon as recon
import scripts.analizador_de_dominios as add

# Limpiar a la consola
helpers.clear_console()

# Inicializar el Logger
import uuid
EXECUTION_ID = str(uuid.uuid4())[:8]
logs = helpers.setup_logging(execution_id=EXECUTION_ID)

# Menu
def menu():
    logs.info(" -"*45)
    logs.info(" El usuario ingresó al programa")

    # Banner
    banner = pyfiglet.figlet_format(" " * 33 + "B C M")
    print(helpers.azul + helpers.bold + banner + helpers.default, end="")

    while True:
        print("-"*90)
        print(helpers.bold + helpers.verde + "Bienvenido al sistema Baseline Cybersecurity Module" + helpers.default)
        print("Seleccione una opción del menú:")
        print("1 - Recolección de Datos Básicos del Dominio")
        print("2 - Footprinting pasivo")
        print("3 - Verificación de reputación")
        print("4 - Salir")

        op = int(input("\nIngrese el número de la tarea que desea realizar: "))

        if op == 1:
            logs.info(" El usuario escogió la opcion 1")
            recon.main()

        elif op == 2:
            logs.info(" El usuario escogió la opcion 2")
            print(helpers.bold + helpers.azul + "Analisis de vulnerabilidades" + helpers.default)
            vuln.main()

        elif op == 3:
            logs.info(" El usuario escogió la opcion 3")
            print("Analizando la reputacion de las ips del dominio...")
            add.main()

        elif op == 4:
            logs.info(" El usuario salió del sistema ")
            print("\nSaliendo... Gracias por utilizar el sistema") 
            logs.info(" -"*45)
            break

        else:
            print(helpers.rojo + "Opción fuera del menú, seleccione nuevamente." + helpers.default)
            logs.error("El usuario ingresó una opción no válida")

if __name__ == "__main__": 
    menu()
