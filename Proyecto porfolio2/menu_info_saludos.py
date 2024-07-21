from fun_auxiliares import *

# Menú inicial
def mostrar_menu_inicial():
   """ Muestra por consola el menú inical del programa.
    """
   print("""
        __________________
        ------ MENÚ ------
        [1] Iniciar Sesión
        [2] Registrarse   
        [0] Cerrar
        ------------------
        """)
 
# Menú principal
def mostrar_menu_principal():
    """ Muestra por consola el menú principal del programa.
    """
    print("""
________________________________
------------- MENÚ -------------
--------------------------------
[1] ¿CÓMO PUEDO RECICLAR? 
[2] INGRESAR OBJETO A RECICLAR
[3] VER MIS PUNTOS
[4] CANJEAR PUNTOS
[5] CENTROS DE RECICLAJE 📍        
[6] VER MI PERFIL 
[7] EDITAR MI PERFIL
[0] SALIR
--------------------------------
""")

#saludo bienvenida
def saludo_bienvenida():
    """ Muestra por consola un saludo de bienvenida.
    """
    print("\n¡Bienvenid@ a ReciApp!\nLa App que te hace más fácil poder reciclar.")
    esperar_usuario()

#saludo de despedida
def saludo_despedida(usuario_actual):
    """ Muestra por consola un saludo de despedida personalizado tomando como parametro la variable 'usuario_actual' para obtener el nombre del usuario.
    """
    limpiar_pantalla()
    print(f"\nHasta luego {usuario_actual['Nombre']}, esperamos que vuelvas pronto.")

# Función para mostrar cómo reciclar
def como_reciclar():
    """ Muestra por consola una serie de pasos que le permiten ver al usuario como reciclar.
    """
    limpiar_pantalla()
    print("""
 Para poder reciclar correctamente, sigue estos pasos:\n
 1. Limpia y seca los objetos antes de reciclarlos.
 2. Separa los materiales según su tipo (papel, plástico, vidrio, metal).
 3. Coloca cada tipo de material en su contenedor correspondiente.
    """)
    esperar_usuario()
