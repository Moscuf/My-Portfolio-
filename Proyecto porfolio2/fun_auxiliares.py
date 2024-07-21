
import os 

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def esperar_usuario():
    input("\nPresiona enter para continuar")

def mensaje_saliendo():
    print("\nSaliendo del programa...")

def mensaje_volviendo():
    print("\nVolviendo al menú principal...")

def mensaje_error():
    print("\nERROR: Ingrese una opción válida.")
  
