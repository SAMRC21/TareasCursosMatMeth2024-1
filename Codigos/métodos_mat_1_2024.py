# -*- coding: utf-8 -*-
"""Métodos Mat 1  2024.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11UB_2qhRSzCU2KVihxp4IJN69bWcwQDl

## ***BARICENTRO***
"""

def calcular_baricentro(x1, y1, x2, y2, x3, y3):
    # Calcular las coordenadas del baricentro
    baricentro_x = (x1 + x2 + x3) / 3
    baricentro_y = (y1 + y2 + y3) / 3

    return baricentro_x, baricentro_y

# Ejemplo de uso con vértices A(1, 2), B(3, 4), C(5, 1)
x1, y1 = 1, 2
x2, y2 = 3, 4
x3, y3 = 5, 1

baricentro = calcular_baricentro(x1, y1, x2, y2, x3, y3)

print(f"El baricentro del triángulo con vértices A({x1}, {y1}), B({x2}, {y2}), C({x3}, {y3}) es {baricentro}")

def calcular_baricentro(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    # Calcular las coordenadas del baricentro en tres dimensiones
    baricentro_x = (x1 + x2 + x3) / 3
    baricentro_y = (y1 + y2 + y3) / 3
    baricentro_z = (z1 + z2 + z3) / 3

    return baricentro_x, baricentro_y, baricentro_z

# Ejemplo de uso con vértices A(1, 2, 3), B(3, 4, 5), C(5, 1, 2)
x1, y1, z1 = 1, 2, 3
x2, y2, z2 = 5, 1, 2
x3, y3, z3 = 3, 9, 5

baricentro = calcular_baricentro(x1, y1, z1, x2, y2, z2, x3, y3, z3)

print(f"El baricentro del triángulo con vértices A({x1}, {y1}, {z1}), B({x2}, {y2}, {z2}), C({x3}, {y3}, {z3}) es {baricentro}")