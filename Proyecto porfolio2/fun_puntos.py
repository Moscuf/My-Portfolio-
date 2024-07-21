from fun_auxiliares import *


def ver_puntos(usuario_actual):
    """
    Muestra por consola los puntos totales del usuario. Toma como parametro la variable 'usuario_actual' para obtener los puntos del usuario.
    """
    limpiar_pantalla()
    print(f"\nUsted tiene un total de {int(sum(usuario_actual['Puntos']))} puntos.")
    esperar_usuario()

# Función para calcular los puntos, calcula si los puntos son suficientes para realizar el canje
def calcular_puntaje(usuario_actual, puntos):
    """
    Verifica si los puntos del usuario son suficientes para realizar el canje. Toma como parametro la variable 'usuario_actual' para obtener los puntos del usuario. Retorna usuario_actual.
    """
    total_puntos = sum(usuario_actual['Puntos'])
    total_puntos -= puntos

    if total_puntos < 0: 
        print("\nLo sentimos, no tienes puntos suficientes para realizar el canje.")
    else:
        usuario_actual['Puntos'].clear()
        usuario_actual['Puntos'].append(total_puntos)
        print(f"\n¡Canje realizado con éxito!\nTe quedan {int(total_puntos)} puntos.")

    return usuario_actual

def mostrar_menu_canjear():
    """
    Muestra por consola el menú con las opciones de canje disponibles.
    """
    limpiar_pantalla()
    print("""
    _____________________________________
    --------- Opciones de canje ---------
    [1] 2500 puntos: Maceta geotextil
    [2] 1000 puntos: Descuento en tienda
    [3] 500 puntos: Bolsa ecológica
    [0] Salir
    -------------------------------------
    """)

def canjear_puntos(usuario_actual):
   """
   Permite al usuario realizar un canje de puntos por premios disponibles, verificandolo con la funcion calcular_puntaje. Toma como parametro la variable 'usuario_actual' para obtener los puntos del usuario. Retorna usuario_actual.
   """
   mostrar_menu_canjear()
   opcion = int(input("\nSeleccione una opción: "))
   limpiar_pantalla()
   match opcion:
        case 1: 
            print("\nEsta maceta ecologica es la opción perfecta para reemplazar el plástico ya que es 100% reciclable.")
            usuario_actual = calcular_puntaje(usuario_actual, 2500)
        case 2: 
            print("\nTienes un 10% de descuento en cualquier producto sustentable en la tienda oficial de ReciApp ®")
            usuario_actual = calcular_puntaje(usuario_actual, 1000)
        case 3:
            print("\nEsta bolsa soporta hasta 8Kg! y podes elegir el diseño que más te guste de la tienda.")
            usuario_actual = calcular_puntaje(usuario_actual, 500)
        case 0: 
            mensaje_volviendo()
        case _: 
            mensaje_error()        

   esperar_usuario()
   return usuario_actual


