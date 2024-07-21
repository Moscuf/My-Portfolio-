
from fun_auxiliares import *
from importar_datos import puntos_objetos

   
def menu_ingresar_objetos():
  """
  Muestra por consola el menú para ingresar objetos.
  Retorna 'opcion'.
  """
  limpiar_pantalla()
  print("\nTe recordamos que cualquier objeto que vayas a ingresar debe estar limpio y seco! 😀")
  print("\nPor favor, seleccione una opción del siguiente menú: \n")
  for objeto in puntos_objetos:
    print(f"[{objeto['id']}] {objeto['nombre']}")

  
  opcion = int(input("\n"))
  return opcion

def ingresar_objeto(usuario_actual):
  """
  El usuario debe indicar el material y su cantidad en Kgs, a cambio se le otorgan una cantidad de puntos correspondientes, que son guardados en los datos del mismo. Toma como parametro la variable 'usuario_actual' para obtener los puntos del usuario. Retorna 'usuario_actual'.
  """
  
  while True:
    opcion = menu_ingresar_objetos()
    
    if opcion == 0: 
      break

    if opcion >= 1 and opcion < len(puntos_objetos):
      cantidad = float(input("\n¿Cuántos kilos ingresó?: "))
      resultado = puntos_objetos[opcion-1]['puntos'] * cantidad
      usuario_actual['Puntos'].append(resultado)
      limpiar_pantalla()
      print(f"\n¡Felicidades, obtuvo {int(resultado)} puntos!")
      usuario_actual = eliminar_objeto(usuario_actual)
      
      break
    else:
      limpiar_pantalla()
      mensaje_error()
      esperar_usuario()

  limpiar_pantalla()
  return usuario_actual

def eliminar_objeto(usuario_actual):
  """
  Permite al usuario eliminar el último objeto ingresado, y se elimina la ultima cantidad de puntos obtenidos, en caso de no tener se le muestra un mensaje con dicha información.
  """
  opcion = input("\nSi desea eliminar el último objeto ingresado presione [E]\nSino, presione enter").upper()

  if opcion == "E":

    if len(usuario_actual['Puntos']) <= 0:
      print("\nERROR, No se registran objetos ingresados.") 
    else:    
      usuario_actual['Puntos'].pop()
      print("\nEl último objeto ingresado se ha eliminado con éxito!")
      
    esperar_usuario()
  return usuario_actual

