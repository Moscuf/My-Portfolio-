import json
from fun_usuario import *

leer_json = open('datos.json', 'r')
data = json.load(leer_json)
puntos_objetos = data['Puntos']
datos_usuarios = data['Usuarios']
centros_reciclaje = data['Centros de Reciclaje']
leer_json.close()

def guardar_usuario(usuario_actual):
  """
  Guarda los datos del usuario si es existente, si no crea uno nuevo. Toma como parametro la variable usuario_actual para para obtener los d atos del mismo. 
  """
  indice_usuario_actual = -1

  for indice, usuario in enumerate(datos_usuarios):
    if usuario['Nombre de usuario'] == usuario_actual['Nombre de usuario']:
      indice_usuario_actual = indice
  
  if indice_usuario_actual > 0:
    datos_usuarios[indice_usuario_actual] = usuario_actual
  else:
    datos_usuarios.append(usuario_actual)

  
  datos_actualizados = {"Puntos": puntos_objetos,"Usuarios": datos_usuarios,"Centros de Reciclaje":centros_reciclaje}
  escribir_json = open('datos.json', 'w')
  json.dump(datos_actualizados,escribir_json)
  escribir_json.close()