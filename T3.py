import math
import random


def leer_numero(mensaje, tipo=float):
    """Pide un número positivo al usuario hasta que sea válido."""
    while True:
        try:
            valor = tipo(input(mensaje))
            if valor > 0:
                return valor
            print("  -> El valor debe ser mayor que cero.")
        except ValueError:
            nombre = "entero" if tipo is int else "decimal"
            print(f"  -> Entrada inválida, escriba un número {nombre}.")


def en_elipse(x, y, a, b):
    return (x ** 2) / (a ** 2) + (y ** 2) / (b ** 2) <= 1


def en_hiperbola(x, y, c, d):
    return (x ** 2) / (c ** 2) - (y ** 2) / (d ** 2) >= 1


def simular(a, b, c, d, cantidad):
    """Lanza 'cantidad' puntos aleatorios y devuelve los conteos."""
    dentro_elipse = 0
    dentro_ambas = 0

    for _ in range(cantidad):
        x = random.uniform(-a, a)
        y = random.uniform(-b, b)

        if en_elipse(x, y, a, b):
            dentro_elipse += 1
            if en_hiperbola(x, y, c, d):
                dentro_ambas += 1

    return dentro_elipse, dentro_ambas


def main():
    print("--- Área de intersección elipse/hipérbola (Monte Carlo) ---")

    a = leer_numero("Ingrese a (elipse, eje x): ")
    b = leer_numero("Ingrese b (elipse, eje y): ")
    c = leer_numero("Ingrese c (hipérbola, eje x): ")
    d = leer_numero("Ingrese d (hipérbola, eje y): ")
    n = leer_numero("Ingrese la cantidad de puntos: ", int)

    dentro_elipse, dentro_ambas = simular(a, b, c, d, n)

    area_elipse = math.pi * a * b
    proporcion = dentro_ambas / dentro_elipse if dentro_elipse > 0 else 0
    area_interseccion = proporcion * area_elipse

    print("\n--- Resultados ---")
    print(f"Puntos generados:                     {n}")
    print(f"Puntos dentro de la elipse:           {dentro_elipse}")
    print(f"Puntos en la intersección:            {dentro_ambas}")
    print(f"Área de la elipse (pi*a*b):           {area_elipse:.4f}")
    print(f"Proporción intersección/elipse:       {proporcion:.4f}")
    print(f"Área aproximada de la intersección:   {area_interseccion:.4f}")


if __name__ == "__main__":
    main()
