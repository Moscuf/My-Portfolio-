
from fun_auxiliares import *
from fun_usuario import *
from fun_objetos import * 
from fun_puntos import *
from menu_info_saludos import *
from importar_datos import *
from centros_reciclaje import  *

usuario_actual = {}
saludo_bienvenida() 

while True:
    mostrar_menu_inicial()
    opcion = int(input())
    match opcion:
        case 1:
            usuario_actual = inicio_sesion()
            break
        case 2:
            registro_usuario()
        case 0:
            print("\nHasta luego, esperamos que vuelvas pronto.")
            break
        case _:
            mensaje_error()

if usuario_actual:
    while True:
        limpiar_pantalla()
        mostrar_menu_principal()
        
        try:
            opcion = int(input("Seleccione una opción: "))
            match opcion:
                case 1:
                    como_reciclar()
                case 2:
                    usuario_actual = ingresar_objeto(usuario_actual)
                case 3:
                    ver_puntos(usuario_actual)
                case 4:
                    usuario_actual = canjear_puntos(usuario_actual)
                case 5:
                    mostrar_centros()
                case 6:
                    limpiar_pantalla()
                    ver_mi_perfil(usuario_actual)  
                case 7:
                    usuario_actual = modificar_dato_usuario(usuario_actual)
                case 0:
                    break
                case _:
                    mensaje_error()
                    esperar_usuario()
        except ValueError:
            mensaje_error()
            esperar_usuario()
    guardar_usuario(usuario_actual)
    saludo_despedida(usuario_actual)