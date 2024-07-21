from fun_auxiliares import *
from importar_datos import *

def registro_usuario():
    """
    Permite al usuario registrarse ingresando los datos solicitados, se crea un nuevo usuario.
    """
    nuevo_usuario = {}
    limpiar_pantalla()
    print("\nEmpezá por resgistrarte. Es súper fácil y rápido!")
    nombre = input("\nIngresa tu nombre: ").capitalize().strip()
    nuevo_usuario['Nombre'] = nombre
    apellido = input("\nIngresa tu apellido: ").capitalize().strip()
    nuevo_usuario['Apellido'] = apellido
    nombre_usuario = input("\nIngresa tu nombre de usuario: ")
    nuevo_usuario['Nombre de usuario'] = nombre_usuario
    contrasenia_usuario = input("\nIngresa una contraseña: ") 
    nuevo_usuario['Contrasenia'] = contrasenia_usuario
    nuevo_usuario['Puntos'] = []

    guardar_usuario(nuevo_usuario)
    limpiar_pantalla()
    print("\nListo! Ahora iniciá sesión y ya podes empezar a reciclar!")
    esperar_usuario()
    limpiar_pantalla()
    return
 
def inicio_sesion():
    """
    Permite al usuario iniciar sesión siempre y cuando esté registrado, para la verificación se utiliza la funcion buscar_usuario. El usuario tiene 3 intentos disponibles para iniciar sesión, en caso de que los datos estén incorrectos se le mostrará en un mensaje.
    """
    limpiar_pantalla()
    print("\nPor favor, ingresa tus datos para acceder a tu cuenta: ")
    intento = 3
    while intento > 0 and intento < 4:
        usuario = input("\nUsuario: ")
        contrasenia = input ("\nContraseña: ")
        datos_usuario = buscar_usuario(usuario)

        if not datos_usuario is None:
            if  datos_usuario['Contrasenia'] == contrasenia:
                print("\nIngreso exitoso. A reciclar!")
                esperar_usuario()
                return datos_usuario
        
        print("\nEl usuario o la contraseña ingresados son incorrectos.\nPor favor vuelva a intentar.")
        intento -= 1
        #limpiar_pantalla()
        print(f"\nTe quedan {intento} intentos disponibles")
    
        if intento == 0 :
            print("\nSe agotaron los intentos. Vuelva a intentar en 5 minutos \n")
            # esperar 5 minutos
            # intento +=3 
            return {}
                     
def ver_mi_perfil(usuario_actual):
    """
    Muestra por consola el perfil del usuario, tomando como parametro la variable 'usuario_actual' para obtener los datos del mismo.
    """
    print("\nMIS DATOS".center(60, " "),"\n")
    for clave, valor in usuario_actual.items():
        if clave == "Puntos":
            continue
        print(f"{clave}".ljust(20, " "), end=" ")
        print(f"{valor}".rjust(20, " "))

    esperar_usuario()
        
def modificar_dato_usuario(usuario_actual):
    """
    Permite al usuario modificar los datos de su perfil, al finalizar se utiliza la funcion ver_mi_perfil para mostarle su perfil actualizado. Toma como parametro la variable 'usuario_actual' para obtener los datos del mismo. Retorna usuario_actual.
    """
    limpiar_pantalla()
    print("\nPresione Enter si no quiere modificar el dato. Para modificarlo ingrese el nuevo valor y luego Enter\n")
    for clave, _ in usuario_actual.items():
        if clave == "Puntos" or clave == "Nombre de usuario":
            continue
        nuevo_valor = input(f"{clave}: ").capitalize()
        if nuevo_valor:
            usuario_actual[clave] = nuevo_valor
    limpiar_pantalla()
    print("\nSe han modificado los datos, así luce tu nuevo perfil:\n ")
    ver_mi_perfil(usuario_actual)
    return usuario_actual


def buscar_usuario(nombre_usuario):
    """
    Busca en el archivo datos.json los 'Usuarios' por 'Nombre de usuario', y así verifica la existencia del usuario. Toma como parametro la variable 'usuario_actual' para obtener los datos del mismo.
    """
    for usuario in datos_usuarios:
        if usuario['Nombre de usuario'] == nombre_usuario:
            return usuario
    return None


