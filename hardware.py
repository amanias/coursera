#!C:\Users\micro\AppData\Local\Programs\Python\Python310\python.exe
import os
import psutil
import shutil
import sys

def chequear_disco(disk):
    """Verificar que hay suficiente espacio libre en disco"""
    espacioEnDisco = shutil.disk_usage(disk)
    libre = espacioEnDisco.free/espacioEnDisco.used * 100
    print("Espacio libre en disco: {:f}".format(libre))
    return libre < 20

def chequear_disco_raiz():
    """Verificar si la partición root está llena"""
    return chequear_disco("C:/")

def chequear_reinicio():
    """Devuelve verdad si es necesario reiniciar el ordenador."""
    return os.path.exists("/run/reboot-requiered")

def chequear_uso_cpu():
    """Verificar que la carga de procesos de la CPU es suficiente"""
    uso = psutil.cpu_percent(1)
    print("Uso del procesador: {:f} %".format(uso))
    return uso > 75

def main():
    """Realización de los chequeos"""

    """"Lista de duplas con las funciones de chequeo y sus mensajes de error a mostrar en caso de fallo"""
    chequeos = [        
        (chequear_uso_cpu, "Uso Excesivo de la CPU!"),
        (chequear_disco_raiz, "Partición Raiz Llena!"),
        (chequear_reinicio, "Reinicio Pendiente!"),        
    ]

    todo_ok = True
    
    for chequeo, mensaje in chequeos:
        if chequeo():
            print(mensaje)
            todo_ok = False
    
    if not todo_ok:
        sys.exit(1)

    print("Todo correcto!!!")
    sys.exit(0)

main()
