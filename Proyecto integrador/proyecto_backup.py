# Python Inicial [Python]
# Proyecto integrador
# Sistema de Copias de Seguridad Locales

# Autor: Julian Sarlingo
# Version: 2.0 beta

'''Este es un sistema donde tu le ingresas exactamente
que carpeta o archivo quieres salvar.
NO recupera archivos perdidos previamente,
los guarda al momento de ejecutar el codigo, y puedes
recuperar una de esas versiones, pero no hace milagros'''


import csv
from os import system 
from os.path import exists
from time import sleep
import datetime
import shutil

system('cls')

# Funcion para establecer la fecha y hora del backup
def hora():
    fecha = datetime.datetime.now()
    fecha = fecha.strftime('%Y/%m/%d %H:%M:%S')
    return fecha

# Funcion que verifica cual fue el ultimo backup realizado
def ultimo_backup():
    with open('directorios.csv') as csvfile:
        data = list(csv.DictReader(csvfile))
    
    for backup in data:
        if backup.get('Ultimo') == '1':
            return data.index(backup)


# Funcion que genera el indice del backup
def generar_id():
    '''
    Funcion de ayuda, nos obtiene el ID para que insertemos una nueva prenda, el ID que devuelve
    es el último ID registrado + 1

    Ejemplo de funcionamiento
    CSV de entrada
        |----|-----------------|-----------------|------------|
        | id | nombre          | categoria       | color      |
        |----|-----------------|-----------------|------------|
        |  1 | saco viejo      | prenda superior | negro      |
        |----|-----------------|-----------------|------------|
        |  2 | camisa moderna  | prenda superior | multicolor |
        |----|-----------------|-----------------|------------|
        |  3 | remera basica   | prenda superior | blanco     |
        |----|-----------------|-----------------|------------|

    Valor de retorno → 3 + 1 → 4
    '''
    try:
        with open('directorios.csv', 'r') as csvfile:
            # Leer archivo CSV y almacenar los resultados en data
            data = list(csv.DictReader(csvfile))

        # Obtener ultima fila del CSV leído
        ultima_fila = data[-1]

        # Obtener el ID de la última fila
        ultimo_id = int(ultima_fila.get('ID'))

        # Aumentar en 1 el ID encontrado, y retornarlo
        return ultimo_id + 1
    except:
        return 1

# Funcion que comprueba la existencia del archivo y lo crea en caso de ser falso
def comprobacion_inicio():
    file_exists = exists('directorios.csv')
    if file_exists == False:

        print('Bienvenid@ a su primer backup!\n')
        print('Para comenzar se le pedirá un nombre con el que usted reconocerá el archivo, y a continuación,')
        print('se le pedirá el directorio que quiera respaldar\n')
        csvfile = open('directorios.csv', 'w', newline='')

        # Especificar cuales serán las columnas del CSV
        header = ['ID', 'Nombre', 'Directorio', 'Fecha creacion', 'Fecha Ultimo Backup', 'Cantidad backups total', 'Ultimo']

        # Construir el objeto writer, que se encargará de escribir el csv
        writer = csv.DictWriter(csvfile, fieldnames=header)

        # Escribir los nombres de las columnas
        writer.writeheader()

        csvfile.close()
        
    return file_exists

# Funcion que pregunta al usuario si quiere realizar backup del ultimo directorio
# ingresar datos nuevos
# o seleccionar un directorio ya cargado en el archivo
def preguntar_si_comienza():
    print('Desea comenzar una copia de seguridad del ultimo directorio?')
    print('O desea ingresar un directorio nuevo?')
    print('Seleccione su opcion:')
    print('1. Realizar copia de seguridad')
    print('2. Ingresar nuevo directorio')
    print('3. Seleccionar un directorio existente')
    print('0. Terminar el programa\n')

    while True:

        try:
            opcion = input()
            if opcion == '1' or opcion == '':
                return('Crear Backup')

            elif opcion == '2':
                return('Ingresar Datos')

            elif opcion == '3':
                return('Seleccionar')

            elif opcion == '0':
                return('Terminar')

            else:
                print('Ingrese una de las opciones')

        except:
            print('Ingrese una de las opciones')

# Funcion que pregunta si se quiere seguir ingresando datos o continuar
def preguntar_si_guarda():
    print('Desea comenzar una copia de seguridad de este directorio?')
    print('O desea ingresar un directorio nuevo?')
    print('Seleccione su opcion:')
    print('1. Realizar copia de seguridad')
    print('2. Ingresar nuevo directorio\n')
    while True:
        try:
            opcion = input()
            if opcion == '1' or opcion == '':
                indice = ultimo_backup()
                comenzar_backup(indice)
                break
            elif opcion == '2':
                return('sigue')
            elif opcion == '0':
                return('Terminar')
            else:
                print('Ingrese una de las opciones')
        except:
            print('Ingrese una de las opciones')

# Funcion que solicita ingresar datos al usuario
def ingreso_datos():
    # Solicitar datos al usuario
    ingreso = 'Se le solicitarán uno por uno los datos necesarios para realizar un backup'
    print(ingreso)
    nombre = input('Ingrese el nombre con el que quiere reconocer su backup:\n')
    print('\nCopie y pegue aqui el directorio tal cual como sale en la barra superior del explorador de archivos')
    directorio = input('y agregue al final el nombre de un archivo si no quiere copiar una carpeta completa:\n')

    if directorio == '':
        return False

    # Cambio la barra que se pone por defecto por una compatible
    directorio = directorio.replace("\\", '/') 

    # Crear ID
    id = generar_id()

    # Creacion fecha inicial
    fecha_creacion = hora().replace("\\", '/')
    fecha_ult_back = 0

    # Resetear el 'Ultimo' Backup
    csvfile = open('directorios.csv')
    data = list(csv.DictReader(csvfile))

    for line in data:
        line['Ultimo'] = 0

    csvfile.close()
    
    csvfile = open('directorios.csv', 'w', newline='')
    header = ['ID', 'Nombre', 'Directorio', 'Fecha creacion',
              'Fecha Ultimo Backup', 'Cantidad backups total', 'Ultimo']

    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)
    csvfile.close()

    # Construir objeto a respaldar
    backup = {
        'ID': id,
        'Nombre': nombre,
        'Directorio': directorio,
        'Fecha creacion': fecha_creacion,
        'Fecha Ultimo Backup': fecha_ult_back,
        'Cantidad backups total': 0,
        'Ultimo': 1
    }

    # Construir el objeto writer, que se encargará de escribir el csv
    csvfile = open('directorios.csv', 'a', newline='')
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writerow(backup)

    csvfile.close()

    return True


# Funcion que realiza los backups
def comenzar_backup(indice):
    # Abrir el archivo CSV en modo lectura
    with open('directorios.csv', 'r') as csvfile:
        data = list(csv.DictReader(csvfile))
    
    nombre = data[indice]['Directorio'].split('/')[-1]
    ruta_origen = data[indice]['Directorio']

    with open('config.txt') as config:
        texto = config.read().split(' = ')[-1].rstrip()
    # Pegar aqui debajo la ruta donde hará las copias de seguridad
    # La carpeta "Backups" 
    ruta_destino = texto + data[indice]['Nombre'] + '/Backup'


    existe = exists(ruta_origen.replace("/", '\\'))

    if existe == True:
        # exists(ruta_origen.replace("/", '\\'))
        print('Existe')
        
    else:
        print('Al parecer la el directorio de su archivo ya no existe o se movio, revise su carpeta')
        print(ruta_origen)
        return


    # minutos = 0
    # horas = 0
    print('Introduzca la cantidad de minutos que va a estar trabajando en esta carpeta')
    print('Numeros decimales son validos')
    tiempo = float(input())
    # tiempo = float(input('Si el numero es mayor a 10, se supondrá que se refiere a minutos: '))

    # if tiempo > 10:
    #     minutos = tiempo
    # elif tiempo <= 10:
    #     horas = tiempo

    segundos = tiempo * 60

    intervalo = float(input('Introduzca cada cuanto tiempo (en minutos) se realizará el backup:\n'))
    intervalo *= 60

    while segundos > 0:
        for i in range(1,4):
            sleep(intervalo)
            existes = exists(ruta_destino + str(i))
            segundos -= intervalo
            if existes == True:
                siExiste = ruta_destino + str(i) + " Existe\n"
                print(siExiste)
                
                # Si existe la carpeta, se elimina para dar espacio a hacerla otra vez
                # No queremos infinitos backups de la misma carpeta o archivo
                shutil.rmtree(ruta_destino + str(i))
                
                
            else:
                noExiste = ruta_destino + str(i) + " NO Existe\n"
                print(noExiste)
                
            # Aqui la operacion para copiar la carpeta
            shutil.copytree(ruta_origen, ruta_destino +
                            str(i) + '/' + nombre)

            # Resetear la fecha ultimo backup Backup
            csvfile = open('directorios.csv')
            data = list(csv.DictReader(csvfile))

            for line in data:
                line['Ultimo'] = 0

            data[indice]['Fecha Ultimo Backup'] = hora()
            cant_backup = int(data[indice].get('Cantidad backups total'))
            cant_backup = str(cant_backup + 1)
            data[indice]['Ultimo'] = 1
            data[indice]['Cantidad backups total'] = cant_backup

            csvfile.close()

            csvfile = open('directorios.csv', 'w', newline='')
            header = ['ID', 'Nombre', 'Directorio', 'Fecha creacion',
                    'Fecha Ultimo Backup', 'Cantidad backups total', 'Ultimo']

            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writeheader()
            writer.writerows(data)
            csvfile.close()


            print('Backup')
            print(hora())
        print('''Prosigue o recupera?
        1. Prosigue
        2. Recupera''')

        sigue = int(input())
        if sigue == 1:
            continue
        else:
            print('Surgió un problema y necesita recuperarlo')
            print('Por favor, indique el numero del backup que necesita')
            numero = int(input('Indique un numero del 1 al 3\n'))
            recuperar_carpeta(nombre, numero, ruta_destino, ruta_origen)
        
    
    

# Funcion que permite seleccionar la carpeta a respaldar
def seleccion_carpeta():
    # Resetear el 'Ultimo' Backup
    system('cls')
    csvfile = open('directorios.csv')
    data = list(csv.DictReader(csvfile))

    for line in data:
        line['Ultimo'] = 0

    csvfile.close()

    csvfile = open('directorios.csv', 'w', newline='')
    header = ['ID', 'Nombre', 'Directorio', 'Fecha creacion',
              'Fecha Ultimo Backup', 'Cantidad backups total', 'Ultimo']

    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)
    csvfile.close()

    print('Tiene a disposicion estas carpetas:')
    for i in range(len(data)):
        print(str(i+1) + '.' + data[i]['Nombre'])
    indice = int(input('De cual desea hacer Backups?'))
    comenzar_backup(indice - 1)

# Funcion que recupera el archivo desde el backup si surgio algun problema
# Se invierten las rutas de origen y destino ya que ahora
# se copiara la carpeta con direcciones contrarias
def recuperar_carpeta(nombre, backup, ruta_origen, ruta_destino):
    print('Deshaciendo cambios')

    shutil.rmtree(ruta_destino)
    ruta_destino = ruta_destino.removesuffix('Backups/')
    shutil.copytree(ruta_origen + str(backup) + '/' + nombre,
                    ruta_destino)


# Main
if __name__ == '__main__':
    # Compruebo si existe el directorio con los datos
    existe = comprobacion_inicio()

    termina = '' # Variable que, si seleccionamos para salir, adquiere un valor que rompe el siguiente bucle
    # Si no toma ese valor, el programa inicia en su modo normal
    if existe == True:
        while True:
            opcion = preguntar_si_comienza()
            if opcion == 'Crear Backup':
                indice = ultimo_backup()
                comenzar_backup(indice)
                break
            elif opcion == 'Ingresar Datos':
                ingreso_datos()
                print('Por favor, ingrese un directorio')
                break
            elif opcion == 'Seleccionar':
                seleccion_carpeta()
                break  
            elif opcion == 'Terminar':
                termina = opcion
                break      

    # Si no existe, el programa creará el archivo y solicitará el primer elemento
    else:
        continua = ingreso_datos()
        if continua == False:
            print('Por favor, ingrese un directorio')

    # Aqui el programa entrará en bucle para ingresar todos los directorios que el usuario desee
    while True:
        if termina == 'Terminar':
            break
        guarda = preguntar_si_guarda()
        if guarda == 'sigue': # Si retorna 'sigue' se seguira ingresando datos
            continua = ingreso_datos()
            if continua == True:
                continue
            else:
                print('Por favor, ingrese un directorio')
                break
        
        elif guarda == 'Terminar':
            break
