"""
ENTREGA 1 - Tablero 3x3
=======================
Historia de usuario:
    "Como jugador quiero ver un tablero 3x3 numerado para saber
     qué casilla puedo elegir."

Qué se implementó:
    - Función mostrar_tablero() que dibuja el tablero con las casillas 1-9.

Prácticas XP aplicadas:
    - Diseño simple: solo el código que la historia pide, nada de más.
    - Entrega pequeña (small release): la primera versión ya se puede ver.

Limitación conocida (queda pendiente para la próxima iteración):
    - El tablero es una imagen fija: todavía no se puede jugar.
"""

TABLERO_INICIAL = [str(numero) for numero in range(1, 10)]


def mostrar_tablero(tablero):
    """Imprime el tablero en formato 3x3."""
    print()
    for inicio in range(0, 9, 3):
        print(" | ".join(tablero[inicio:inicio + 3]))
        if inicio < 6:
            print("---------")
    print()


if __name__ == "__main__":
    print("=== TIC TAC TOE - Entrega 1: tablero 3x3 ===")
    mostrar_tablero(TABLERO_INICIAL)
