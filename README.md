# Backup_system
Sistema de creación y recuperación de backups de carpetas locales

La idea de este programa es que tu puedes trabajar sobre un archivo o carpeta, con el programa corriendo de fondo. En caso de que en algun momento ocurra algun problema con ese archivo, el programa te permite recuperarlo al final de cada ciclo (3 backups). 

CUIDADO!! el programa realiza copias y elimina carpetas de verdad, NO introduzca carpetas con informacion importante sin estar seguro de que funciona, ni carpetas importantes del sistema operativo.

Se pueden colocar todos los directorios para realizar backup que desee, la informacion se guarda en un archivo CSV de donde el programa extraera el directorio y cual fue el ultimo backup o directorio introducido, para agilizar el siguiente. (El archivo CSV se crea con el primer inicio del programa)

Este programa te permite introducir un directorio, nombrarlo para identificarlo mas facil, y luego hacer copias de seguridad del mismo.
Por defecto crea 3 copias en carpetas separadas, luego te pregunta si quieres seguir, en caso de respuesta afirmativa, el programa elimina las carpetas y las rehace una por una.

Cuenta con un archivo config.txt donde se le debe introducir el directorio donde hara las copias de seguridad, la metodologia es la siguiente:
colocas el directorio de una carpeta, y dentro de esa se creara una carpeta "Backups", dentro de esta se crearan carpetas con el nombre que le diste al momento de correr el programa, dentro de esta, se crearan las 3 carpetas de nombres "Backup1" "Backup2" y "Backup3". Y por ultimo, para que el programa funcione correctamente, dentro de estas se ubicara la copia de la carpeta que se le introdujo.
Al finalizar cada ciclo, el programa hace una pausa y pregunta si desea recuperar alguna de las carpetas o seguir, asi que hay que estar atento al mensaje. Si le dice que quiere recuperar, se interrumpen los ciclos y le pregunta cual de los 3 backups quiere de vuelta, y se eliminara la carpeta original y se reemplazara por la copia.

El programa es funcional, pero aun puede mejorarse, asi que espero cualquier sugerencia, critica y/o correccion.
