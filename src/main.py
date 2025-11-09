import scripts.helpers as helpers
import pyfiglet
import scripts.vuln_test as vuln

# Limpiar a la consola
helpers.clear_console()

# Configuracion de logs
logs = helpers.logging.getLogger("menu")

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
        print("1 - Escaneo de puertos")
        print("2 - Footprinting pasivo")
        print("3 - Verificación de integridad de los datos")
        print("4 - Salir")

        op = int(input("\nIngrese el número de la tarea que desea realizar: "))

        if op == 1:
            logs.info(" El usuario escogió la opcion 1")
            print("Ejecución del escaneo de puertos...")
            # Aquí va tu código futuro

        elif op == 2:
            logs.info(" El usuario escogió la opcion 2")
            print(helpers.bold + helpers.azul + "Analisis de vulnerabilidades" + helpers.default)
            vuln.main()

        elif op == 3:
            logs.info(" El usuario escogió la opcion 3")
            print("Analizando la integridad de los elementos...")
            # codigo de checkhash o algo

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
