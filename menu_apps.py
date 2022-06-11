import os
from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME, "es_ES")                                               # Set locale to Spanish (Spain)

opcion = 0                                                                              # Variable para controlar el menu

while opcion < 3:
    os.system('cls')
    print('+---------------------------------+')
    print('|         Hola ' + os.environ['USERNAME'])                                   # Muestra el nombre de usuario
    print('|                                 |')
    print('|         Menú Principal:         |')
    print('|                                 |')
    print('|   1. Mostrar Día/Hora actual    |')
    print('|   2. Menú Apagar                |')
    print('|   3. Buscador                   |')
    print('|   4. Exit                       |')
    print("|                  By Valite#3644 |")
    print('|                                 |')
    print('+---------------------------------+')
    opcion=int(input('Introduce Opción: '))
    if opcion==1:                                                             # Opción 1: Muestra la fecha y hora actual
        now = datetime.now()                                                            # Muestra la fecha y hora actual
        os.system('cls')
        print(now.strftime("%A %d %B %Y %H:%M:%S Día %j de 365 días"))                  # Formatea la fecha y hora actual
        input("Pulsa Enter para continuar...")
    elif opcion==2:                                                           # Opción 2: Apaga el equipo
        os.system('cls')
        opcionshutdown = 0                                                              # Variable para controlar el menu
        while opcionshutdown < 6:
            os.system("cls")
            print("+-----------------------------+")
            print("|                             |")
            print("|       Menú Principal:       |")
            print("|                             |")
            print("|    1. Apagar Ordenador      |")
            print("|    2. Reiniciar Ordenador   |")
            print("|    3. Hibernar Ordenador    |")
            print("|    4. Cerrar Sesión         |")
            print("|    5. Anular Apagado        |")
            print("|    6. Exit                  |")
            print("|              By Valite#3644 |")
            print("|                             |")
            print("+-----------------------------+")
            opcionshutdown=int(input("Introduce Opción: "))
            if opcionshutdown==1:
                os.system("cls")
                h = int(input(f"Dentro de x horas\n"))                                  # Hora de apagado
                os.system("cls")
                m = int(input(f"Dentro de {h} horas y x minutos\n"))                    # Minutos de apagado
                os.system("cls")
                s = int(input(f"Dentro de {h} horas y {m} minutos y x segundos\n"))     # Segundos de apagado
                os.system("cls")
                hh = h*3600                                                             # Horas a segundos
                mm = m*60                                                               # Minutos a segundos
                t = str(hh+mm+s)                                                        # Tiempo de apagado
                apagar = "shutdown /s /t "                                              # Comando de apagado
                opc = apagar+t                                                          # Comando de apagado con tiempo
                os.system(opc) # Apagar
                print(f"Apagando Ordenador en {h} horas, {m} minutos y {s} segundos")   # Mensaje de apagado
                input("Pulsa Enter para volver al menú o cancelar el apagado...")
            elif opcionshutdown==2:
                os.system("shutdown /r")                                                # Comando de reiniciar
            elif opcionshutdown==3:
                os.system("shutdown /h")                                                # Comando de hibernar
            elif opcionshutdown==4:
                os.system("shutdown /l")                                                # Comando de cerrar sesión
            elif opcionshutdown==5:
                os.system("shutdown /a")                                                # Comando de anular apagado
            elif opcionshutdown==6:
                os.system("exit")                                                       # Comando de cerrar programa y volver al menú principal
            else:
                print("Opcion no existente")
    elif opcion==3:                                                         # Opción 3: Buscador de archivos
        ruta = input("Introduce ruta: ")
        if len(ruta) == 0:
            ruta = "."                                  # Si no se introduce nada se pone la ruta actual
        items = os.listdir(ruta)
        archivo = input('Introduce nombre del archivo: ')

        if len(archivo) == 0:                           # Si no se introduce ningún nombre se busca por extensión
            extension = input("Extension para buscar: ")
            if len(extension) == 0:                     # Si no se introduce ninguna extensión se busca en todo el directorio
                if len(items) == 0:                     # Si no hay ningún archivo en el directorio se muestra un mensaje
                    print("No se ha encontrado ningún archivo")
                for item in items:
                    print(item)                         # Se muestran todos los archivos del directorio ordenados
                input("Pulsa Enter para continuar...")
                opcion=0                                # Se cierra el programa y se vuelve al menú principal
            else:
                newlist = []
                for names in items:                     # Se busca por extensión
                    if names.endswith(extension):       # Si el nombre del archivo termina con la extensión se añade a la lista
                        newlist.append(names)           # Se añade el nombre del archivo a la lista
                if len(newlist) == 0:                   # Si no se encuentran archivos con la extensión se muestra un mensaje
                    print("No se ha encontrado ningún archivo con la extensión " + extension)
                for list in newlist:
                    print(list)                         # Se muestran los archivos con la extensión
                input("Pulsa Enter para continuar...")
                opcion=0                                # Se cierra el programa y se vuelve al menú principal
        else:
            newlist = []
            for names in items:                         # Se busca por nombre
                if names.startswith(archivo):           # Si el nombre del archivo empieza con el nombre se añade a la lista
                    newlist.append(names)               # Se añade el nombre del archivo a la lista
            if len(newlist) == 0:                       # Si no se encuentran archivos con el nombre se muestra un mensaje
                print("No se ha encontrado ningún archivo con el nombre " + archivo)
            for list in newlist:
                print(list)                             # Se muestran los archivos con el nombre
            input("Pulsa Enter para continuar...")
            opcion=0                                    # Se cierra el programa y se vuelve al menú principal
    elif opcion==4:                                                         # Opción 4:Exit
        os.system('cls')
        print("Saliendo...")
        input("Pulsa Enter para continuar...")
    else:
        print("Opcion no existente")