"""
ENTREGA 3 - Cambio de turno
===========================
Historia de usuario:
    "Como jugador quiero que después de mi jugada sea el turno del otro
     jugador, alternando entre X y O."

Qué se implementó:
    - JUGADORES: la lista de fichas posibles ("X", "O").
    - siguiente_jugador(): alterna X -> O -> X.
    - El bucle muestra siempre de quién es el turno.

Prácticas XP aplicadas:
    - Propiedad colectiva: la alternancia vive en una sola función pequeña,
      fácil de leer y de probar por cualquier miembro de la pareja.

Limitación conocida:
    - La partida nunca termina: todavía no se reconoce la victoria (entrega 4).
"""

TABLERO_INICIAL = [str(numero) for numero in range(1, 10)]
FICHAS = ("X", "O")
JUGADORES = FICHAS


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


def siguiente_jugador(jugador):
    """Devuelve el otro jugador: X -> O y O -> X."""
    return JUGADORES[1] if jugador == JUGADORES[0] else JUGADORES[0]


if __name__ == "__main__":
    tablero = TABLERO_INICIAL.copy()
    jugador = JUGADORES[0]
    print("=== TIC TAC TOE - Entrega 3: cambio de turno ===")

    while True:
        mostrar_tablero(tablero)
        print("Turno del jugador", jugador)

        posicion = leer_posicion()
        if casilla_ocupada(tablero, posicion):
            print("Esa casilla está ocupada.")
            continue

        colocar_ficha(tablero, posicion, jugador)
        jugador = siguiente_jugador(jugador)
