from importar_datos import centros_reciclaje
from fun_auxiliares import *

def buscar_por_provincia():
  """Permite a el usuario buscar un centro de reciclaje ingresando una provincia. 
  Busca en el archivo datos.json los 'Centros de Reciclaje' por 'Provincia'.  
  """
  limpiar_pantalla()
  provincia = input("\nIngrese una provincia: ").title()
  respuesta = [] 
  for centro in centros_reciclaje:
    if provincia == centro['Provincia']:
      respuesta.append(centro)
  
  return respuesta


def mostrar_centros():
  """
  Muestra por consola una lista con los centros de reciclaje disponibles en la provincia buscada por el usuario, en caso de no haber ninguno le muestra un mensaje que lo indica.
  Utiliza la función buscar_por_provincia. 
  """
  centros = buscar_por_provincia()
  if not centros: 
    print('No encontramos centros en esa provincia')
  else:
    print("\nCentros de Reciclaje: \n")
    for centro in centros:
      for clave, valor in centro.items() :
        print(f"{clave}".ljust(20, " "), end=" ")
        print(f"{valor}".rjust(20, " "))
      print("\n")
  esperar_usuario()
