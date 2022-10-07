#!C:\Users\micro\AppData\Local\Programs\Python\Python310\python.exe
import requests
import socket

def chequear_localhost():
    """Verifica si el localhost está correctamente configurado"""
    localhost = socket.gethostbyname("localhost")
    #print("El localhost se encuentra en la dirección: {:s}".format(localhost))
    return localhost == "127.0.0.1"

def chequear_conectividad():
    """Verifica si el ordenador se puede conectar satisfactoriamente a Internet"""
    conexion = requests.get("http://www.google.com")
    #print("El código de conexión a Internet es: {:d}".format(conexion.status_code))
    return conexion.status_code == 200

#Realización de las comprobaciones
#if not chequear_localhost() or not chequear_conectividad():
    #print("ERROR de Conexión!!!")
#else:
    #print("Todo correcto!!!")
