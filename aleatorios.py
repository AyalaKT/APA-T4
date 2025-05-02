"""
    Cuarta tarea de APA - Generación de números aleatorios

    Nombre y apellidos: Eric Ayala

    Pruebas

    >>> rng = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rng))
    ...
    16
    29
    18
    15

    >>> rng(29)
    >>> for _ in range(4):
    ...     print(next(rng))
    ...
    18
    15
    20
    1

    >>> rng = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rng))
    ...
    34
    24
    38
    44

    >>> rng.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rng))
    ...
    44
    10
    32
    14
"""

class Aleat:
    """
    Clase para generar números pseudoaleatorios usando el método congruencial lineal.
    """

    def __init__(self, m=2**48, a=25214903917, c=11, x0=1212121):
        """
        Inicializa la clase con los parámetros m, a, c y la semilla inicial x0.
        """
        self.m = m
        self.a = a
        self.c = c
        self.x = x0

    def __next__(self):
        """
        Genera el siguiente número pseudoaleatorio.
        """
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def __call__(self, nueva_semilla):
        """
        Reinicia la secuencia con una nueva semilla.
        """
        self.x = nueva_semilla

    def send(self, nueva_semilla):
        """
        Cambia la semilla actual y devuelve el siguiente valor.
        """
        self.x = nueva_semilla
        return next(self)

def aleat(m=2**48, a=25214903917, c=11, x0=1212121):
    """
    Generador tipo corrutina para generar números aleatorios.
    """
    x = x0
    while True:
        x = (a * x + c) % m
        entrada = yield x
        if entrada is not None:
            x = entrada

# --- Pruebas automáticas ---
import doctest

if __name__ == "__main__":
    doctest.testmod(verbose=True)
