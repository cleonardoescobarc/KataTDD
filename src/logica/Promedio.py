def calcular_promedio(conjunto):
    if not conjunto:
        return 0
    suma = sum(conjunto)
    promedio = suma / len(conjunto)
    return promedio

if __name__ == "__main__":
    conjuntos = [
        [],
        [5],
        [1, 2, 3, 4, 5],
        [-1, -2, -3, -4, -5],
        [-1, 2, -3, 4, -5],
        [5, 5, 5, 5]
    ]

    for conjunto in conjuntos:
        print(f"Conjunto: {conjunto} -> Promedio: {calcular_promedio(conjunto)}")
