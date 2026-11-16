"""
ENTREGA 4 - Reconocimiento de victoria
======================================
Historia de usuario:
    "Como jugador quiero que el juego detecte cuándo alguien hizo
     tres en línea y lo anuncie como ganador."

Qué se implementó:
    - COMBINACIONES_GANADORAS: las 8 líneas posibles (3 filas, 3 columnas,
      2 diagonales).
    - comprobar_ganador(): compara las tres casillas de cada línea.
    - Al ganar se redibuja el tablero, se anuncia al ganador y se corta el bucle.

Prácticas XP aplicadas:
    - Pruebas automatizadas: /pruebas/test_entrega_04_victoria.py se escribió
      ANTES que esta función y cubre filas, columnas, diagonales y falsos positivos.
    - Simplicidad: la victoria se calcula con una lista de tuplas, sin clases
      ni estructuras extra.

Limitación conocida (bug detectado en la revisión de pareja):
    - Si el tablero se llena sin ganador, el bucle se queda pidiendo casillas
      para siempre ("está ocupada"). Se corrige en la entrega 5 (empate + reinicio).
"""

TABLERO_INICIAL = [str(numero) for numero in range(1, 10)]
FICHAS = ("X", "O")
JUGADORES = FICHAS
COMBINACIONES_GANADORAS = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),   # filas
    (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columnas
    (0, 4, 8), (2, 4, 6),              # diagonales
)


def mostrar_tablero(tablero):
    """Imprime el tablero en formato 3x3."""
    print()
    for inicio in range(0, 9, 3):
        print(" | ".join(tablero[inicio:inicio + 3]))
        if inicio < 6:
            print("---------")
    print()


def comprobar_ganador(tablero, jugador):
    """True si 'jugador' tiene tres en línea."""
    for a, b, c in COMBINACIONES_GANADORAS:
        if tablero[a] == tablero[b] == tablero[c] == jugador:
            return True
    return False


def leer_posicion():
    """Pide una casilla hasta que sea un número entre 1 y 9. Devuelve el índice 0-8."""
    while True:
        entrada = input("Elige una casilla (1-9): ").strip()
        if not entrada.isdigit():
            print("Ingresa un número válido (1-9).")
            continue
        posicion = int(entrada) - 1
        if not 0 <= posicion <= 8:
            print("Esa casilla no existe.")
            continue
        return posicion


def casilla_ocupada(tablero, posicion):
    """True si la casilla ya tiene una ficha."""
    return tablero[posicion] in FICHAS


def colocar_ficha(tablero, posicion, jugador):
    """Marca la casilla con la ficha del jugador."""
    tablero[posicion] = jugador


def siguiente_jugador(jugador):
    """Devuelve el otro jugador: X -> O y O -> X."""
    return JUGADORES[1] if jugador == JUGADORES[0] else JUGADORES[0]


if __name__ == "__main__":
    tablero = TABLERO_INICIAL.copy()
    jugador = JUGADORES[0]
    print("=== TIC TAC TOE - Entrega 4: reconocer la victoria ===")

    while True:
        mostrar_tablero(tablero)
        print("Turno del jugador", jugador)

        posicion = leer_posicion()
        if casilla_ocupada(tablero, posicion):
            print("Esa casilla está ocupada.")
            continue

        colocar_ficha(tablero, posicion, jugador)

        if comprobar_ganador(tablero, jugador):
            mostrar_tablero(tablero)
            print("¡Ganó el jugador", jugador, "!")
            break

        jugador = siguiente_jugador(jugador)
