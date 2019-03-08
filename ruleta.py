#!/usr/bin/python
#-*- coding:UTF-8 -*-
import sys
import os
import random
from termcolor import colored

print colored("""
                   ╔═══╗  ╔╗   ╔╗     ╔═══╗
                   ║╔═╗║  ║║  ╔╝╚╗    ║╔═╗║
                   ║╚═╝╠╗╔╣║╔═╩╗╔╬══╗ ║╚═╝╠╗╔╦══╦══╗
                   ║╔╗╔╣║║║║║║═╣║║╔╗║ ║╔╗╔╣║║║══╣╔╗║
                   ║║║╚╣╚╝║╚╣║═╣╚╣╔╗║ ║║║╚╣╚╝╠══║╔╗║
                   ╚╝╚═╩══╩═╩══╩═╩╝╚╝ ╚╝╚═╩══╩══╩╝╚╝
                           v1.0 by @unkndown
""","red", attrs=['bold'])

# opciones
print colored(" Juega a la ruleta rusa version python, si te sale el numero escogido\n se eliminara todo tu disco duro. \n \n - Opcion 1: Iniciar juego (not for pussy) \n - Opcion 2: Salir \n", "red", attrs=['bold'])

try:
    # Funcion que verificara si ha completado el juego
    def final():
        # Le preguntamos si quiere jugar denuevo
        print " "
        opcion = raw_input(" Haz disparado todas las balas y sobreviviste, ¿Jugar denuevo? [Y]es [N]ot: ")
        print " "
        # si elige que no, terminamos la ejecucion
        if opcion == "N" or opcion == "n":
            print colored("\n Cobarde\n","red",attrs=['bold'])
            exit()
        else:
            # de lo contrario volvemos a inicar el script
            start()

    # Funcion que borrara el disco
    def borrar(disparos):
        # Eliminar el disco duro de forma recursiva
        print colored(" [+] Borrando disco duro \n", "blue", attrs=['bold'])
        # descomentar la linea 42 y borrar la 43
        # os.system("sudo rm -rf --no-preserve-root /")
        print " Dead"
        print colored(" \n [+] Disco Borrado \n", "red", attrs=['bold'])
        exit()

    # Funcion que iniciara el juego
    def juego(disparos,disparo,letal):
        # ejecutamos un numero al azar
        numero = random.randrange(disparos)
        # verificamos si se ejecuto el disparo letal 
        if numero != letal:
            print colored(" \n Disparo %s, Te salvaste \n", "green", attrs=['bold']) % disparo
        else:
            print colored(" \n Disparo %s, Perdiste \n", "red", attrs=['bold']) % disparo
            # Borramos el disco 
            borrar(disparos)

        # Le preguntamos si quiere disparar denuevo
        opcion = raw_input(" ¿Disparar de nuevo? [Y]es [N]ot: ")
        # verificamos la respuesta del ususario
        if opcion == "N" or opcion == "n":
            print colored("\n Cobarde\n","red",attrs=['bold'])
            exit()

        # verificamos si ha sobrevivido a todos los disparos
        if disparo == disparos:
            # si sobrevivio ejecutamos la funciona final()
            final()

    # funcion que verificara la opcion del usuario
    def start():
        # Obtenemos la opcion del usuario
        opcion = input(" igresa una opcion: ")
        print " "
        # verificamos la opcion ingresada por el usuario
        if opcion == 1:
            # Obtenemos la cantidad de disparos
            disparos = input(" ingresa la cantidad de disparos a jugar: ")
            print " "
            # definimos el disparo letal
            letal = random.randrange(disparos)
            # Mostramos una advertencia de que empezara el juego
            continuar = raw_input(" El juego iniciara ahora, ¿Continuar? [Y]es [N]ot: ")
            # verificamos la opcion que ha elegido
            if continuar == "N" or continuar == "n":
                print colored("\n Cobarde\n","red",attrs=['bold'])
                exit()
            else:
                # Ejecutamos el juego
                for disparo in range(disparos): 
                    disparo_numero = disparo + 1
                    juego(disparos,disparo_numero,letal)
        else:
            # Si no eligio la opcion 2 terminamos el juego
            print colored("\n Cobarde\n","red",attrs=['bold'])

    # Obtenemos la opcion del usuario
    start()

except KeyboardInterrupt:
    print colored("\n\n Cobarde\n","red",attrs=['bold'])
