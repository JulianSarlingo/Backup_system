import csv
from os import system
import shutil
from time import sleep
system('cls')

# prueba = input('ingrese espacio vacio: ')

# if prueba == '':
#     print('exito!!!!')
# else:
#     print('fracaso!')

# tiempo = 30

# for i in range(tiempo):
#     sleep(1)
#     print(i)

with open('directorios.csv', 'r') as csvfile:
    data = list(csv.DictReader(csvfile))

# archivo = data[2]

# nombre = data[0]['Directorio'].split('/')[-1]

# print(nombre)

ruta_destino = 'C:/Users/Julian/Desktop/Programacion/cursoInove/Python_Inicial/Proyecto integrador/Backups/'
ruta_destino = ruta_destino.removesuffix('Backups/')

print(ruta_destino)
