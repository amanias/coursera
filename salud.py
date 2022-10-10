#!C:\Users\micro\AppData\Local\Programs\Python\Python310\python.exe
import os
import psutil
import shutil
import sys

def chequear_disco_lleno(disk):
    """Devuelve True caso de quedar menos de un 20% de espacio libre; False en caso contrario."""
    espacioEnDisco = shutil.disk_usage(disk)
    libre = espacioEnDisco.free/espacioEnDisco.used * 100
    print("Espacio libre en disco: {:f}".format(libre))
    return libre < 20

def chequear_disco_raiz_lleno():
    """Devuelve True si la partición root está llena; False en caso contrario."""
    return chequear_disco_lleno("C:/")

def chequear_reinicio_necesario():
    """Devuelve True si es necesario reiniciar el ordenador; False en caso contrario."""
    return os.path.exists("/run/reboot-requiered")

def chequear_uso_cpu_excesivo():
    """Verificar que la carga de procesos de la CPU es excesiva; False en caso contrario."""
    uso = psutil.cpu_percent(1)
    print("Uso del procesador: {:f} %".format(uso))
    return uso > 75

def main():
    """Realización de los chequeos"""

    """"Lista de duplas con las funciones de chequeo y sus mensajes de error a mostrar en caso de fallo"""
    chequeos = [        
        (chequear_uso_cpu_excesivo, "Uso Excesivo de la CPU!"),
        (chequear_disco_raiz_lleno, "Partición Raiz Llena!"),
        (chequear_reinicio_necesario, "Reinicio Pendiente!"),        
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
