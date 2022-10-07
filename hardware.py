#!C:\Users\micro\AppData\Local\Programs\Python\Python310\python.exe
import shutil
import psutil

def chequear_disco(disk):
    """Verificar que hay suficiente espacio libre en disco"""
    espacioEnDisco = shutil.disk_usage(disk)
    libre = espacioEnDisco.free/espacioEnDisco.used * 100
    #print("Espacio en disco: {:f}".format(libre))
    return libre > 20

def chequear_uso_cpu():
    """Verificar que la carga de procesos de la CPU es suficiente"""
    uso = psutil.cpu_percent(1)
#    print("Uso del procesador: {:f} %".format(uso))
    return uso < 75

#Realización de las comprobaciones
#if not chequear_disco("C:/") or not chequear_uso_cpu():
    #print("ERROR de Hardware!!!")
#else:
    #print("Todo correcto!!!")
