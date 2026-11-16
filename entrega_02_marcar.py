"""
ENTREGA 2 - Marcar X en el tablero
==================================
Historia de usuario:
    "Como jugador quiero elegir una casilla y que quede marcada con una X."

Qué se implementó:
    - leer_posicion(): valida que la entrada sea un número del 1 al 9.
    - casilla_ocupada(): evita sobrescribir una ficha ya puesta.
    - colocar_ficha(): escribe el jugador en el tablero.
    - Bucle de juego que redibuja el tablero después de cada jugada.

Prácticas XP aplicadas:
    - Prueba primero (TDD): se definió qué entrada es válida antes de escribir.
    - Refactorización: la lectura de datos se sacó del bucle a su propia función.

Limitación conocida:
    - Siempre coloca "X": el cambio de turno es la historia de la entrega 3.
"""

TABLERO_INICIAL = [str(numero) for numero in range(1, 10)]
FICHAS = ("X", "O")


def mostrar_tablero(tablero):
    """Imprime el tablero en formato 3x3."""
    print()
    for inicio in range(0, 9, 3):
        print(" | ".join(tablero[inicio:inicio + 3]))
        if inicio < 6:
            print("---------")
    print()


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


if __name__ == "__main__":
    tablero = TABLERO_INICIAL.copy()
    print("=== TIC TAC TOE - Entrega 2: marcar X ===")

    while True:
        mostrar_tablero(tablero)
        posicion = leer_posicion()

        if casilla_ocupada(tablero, posicion):
            print("Esa casilla está ocupada.")
            continue

        colocar_ficha(tablero, posicion, "X")
