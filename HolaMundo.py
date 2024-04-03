#!/usr/bin/env python3
import random

print("Hola Mundo!\n") 

# Modificación del código
x = int(input("Introduce un numero del 1 al 6:\n"))
if x == random.randint(1,6):
    print("¡Tu ganas!")
else:
    print("Mala suerte.")
    