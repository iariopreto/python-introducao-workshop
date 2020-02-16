#!/bin/python3

def multiplicacao(a: int, b: int) -> int:
    """Multiplicação de 2 numeros
    
    Arguments:
        a {int} -- Primeiro numero
        b {int} -- Segundo numero
    
    Returns:
        int -- Returno da multiplicação
    """
    return a * b

print(__name__)
if __name__ == "__main__":
    print(multiplicacao(1, 2))