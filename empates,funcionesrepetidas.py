# -*- coding: utf-8 -*-
"""Empates,funcionesrepetidas.ipynb



Original file is located at
    https://colab.research.google.com/drive/1FUePE5hud9uUheCU8RX-3V7lURg8ieM0
"""

def crear_tablero():
    tablero = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
    return tablero

def imprimir_tablero(tablero):
        print(f"{tablero[0][0]}|{tablero[0][1]}|{tablero[0][2]}")
        print("-----")
        print(f"{tablero[1][0]}|{tablero[1][1]}|{tablero[1][2]}")
        print("-----")
        print(f"{tablero[2][0]}|{tablero[2][1]}|{tablero[2][2]}")



def movimiento_jugador(tablero, jugador):
    while True:
        fila = int(input("Elige fila (0, 1, 2): "))
        columna = int(input("Elige columna (0, 1, 2): "))
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador
            break
        else:
            print("¡Casilla ocupada!")


def hay_ganador(tablero):
    # Verificar filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
            return True

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return True

    return False


def tablero_lleno(tablero):
    for fila in tablero:
        if " " in fila:
            return False
    return True

import random

def movimiento_ia(tablero):
    casillas_vacias = [(i, j) for i in range(3) for j in range(3) if tablero[i][j] == " "]
    if casillas_vacias:
        fila, columna = random.choice(casillas_vacias)
        tablero[fila][columna] = "O"

def juego_completo():
    tablero = crear_tablero()
    jugador_actual = "X"

    while True:
        imprimir_tablero(tablero)
        print(f"Turno de {jugador_actual}")
        if jugador_actual == "X":
            movimiento_jugador(tablero, jugador_actual)
        else:
            movimiento_ia(tablero)


        if hay_ganador(tablero):
            print(f"¡{jugador_actual} ha ganado!")
            break

        if tablero_lleno(tablero):
            print("¡Empate!")
            break

        if(jugador_actual=="O"):
            jugador_actual="X"
        else:
            jugador_actual = "O"


juego_completo()
