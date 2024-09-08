import json
from funciones import *

def main():
    archivo_medicamentos = "medicamentos.json"
    archivo_laboratorios = "laboratorios.json"

    cargar_crear_archivos(archivo_medicamentos, archivo_laboratorios)

    while True:
        mostrar_menu()
        opcion = input("Ingrese una de las opciones: ")

        if opcion == "1":
            agregar_medicamento(archivo_medicamentos)
        elif opcion == "2":
            agregar_laboratorio(archivo_laboratorios)
        elif opcion == "3":
            mostrar_informacion(archivo_medicamentos, archivo_laboratorios)
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor ingresar un número del 1 al 4.")

if __name__ == "__main__":
    main()


