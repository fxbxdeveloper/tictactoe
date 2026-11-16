"""
ENTREGA 5 - Empate y reinicio (versión final)
=============================================
Historias de usuario:
    "Como jugador quiero que se detecte el empate cuando el tablero se llena,
     para no quedarme pidiendo casillas para siempre."
    "Como jugador quiero poder jugar otra partida sin cerrar el programa."

Qué se implementó:
    - tablero_lleno() y el mensaje de empate.
    - jugar(): una partida completa; devuelve el ganador o None si es empate.
    - main(): repite la partida mientras el jugador responda "s".
    - pedir_posicion(tablero): valida rango y ocupación en un solo lugar.

Prácticas XP aplicadas:
    - Refactorización: la validación de la casilla se unificó en pedir_posicion(),
      sin cambiar el comportamiento visible del juego.
    - Integración: esta es la versión que se demuestra; las 5 entregas quedan
      cubiertas por las pruebas de /pruebas.
    - Valentía: se corrigió el bug detectado en la entrega 4 en vez de esconderlo.

Cómo ejecutar:  python entregas/entrega_05_reiniciar.py
"""

TABLERO_INICIAL = [str(numero) for numero in range(1, 10)]
JUGADORES = ("X", "O")
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


def tablero_lleno(tablero):
    """True si ya no quedan casillas libres."""
    return all(casilla in JUGADORES for casilla in tablero)


def siguiente_jugador(jugador):
    """Devuelve el otro jugador: X -> O y O -> X."""
    return JUGADORES[1] if jugador == JUGADORES[0] else JUGADORES[0]


def pedir_posicion(tablero):
    """Pide una casilla hasta que sea válida y esté libre. Devuelve el índice 0-8."""
    while True:
        entrada = input("Elige una casilla (1-9): ").strip()
        if not entrada.isdigit():
            print("Ingresa un número del 1 al 9.")
            continue
        posicion = int(entrada) - 1
        if not 0 <= posicion <= 8:
            print("Esa casilla no existe.")
            continue
        if tablero[posicion] in JUGADORES:
            print("Esa casilla está ocupada.")
            continue
        return posicion


def jugar():
    """Juega una partida completa. Devuelve el ganador o None si hay empate."""
    tablero = TABLERO_INICIAL.copy()
    jugador = JUGADORES[0]

    print("=== TIC TAC TOE ===")

    while True:
        mostrar_tablero(tablero)
        print("Turno del jugador", jugador)

        posicion = pedir_posicion(tablero)
        tablero[posicion] = jugador

        if comprobar_ganador(tablero, jugador):
            mostrar_tablero(tablero)
            print("¡Ganó el jugador", jugador, "!")
            return jugador

        if tablero_lleno(tablero):
            mostrar_tablero(tablero)
            print("¡Empate!")
            return None

        jugador = siguiente_jugador(jugador)


def main():
    """Pregunta al terminar cada partida si se quiere jugar otra."""
    while True:
        jugar()
        otra = input("¿Quieres jugar otra vez? (s/n): ").strip().lower()
        if otra != "s":
            print("¡Gracias por jugar!")
            return


if __name__ == "__main__":
    main()
