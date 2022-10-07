#!/usr/bin/env python3
import hardware
import conectividad

# Realizacion de las comprobaiones.
if not hardware.chequear_disco("C:/") or not hardware.chequear_uso_cpu():
    print("Fallo de Hardware")
elif not conectividad.chequear_localhost() or not conectividad.chequear_conectividad():
    print("Fallo en la Red!!!")
else:
    print("Todo Correcto!!!")