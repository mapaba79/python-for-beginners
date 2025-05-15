def counting_sort(arr):
    if not arr:
        return []

    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    result = []
    for num, freq in enumerate(count):
        result.extend([num] * freq)

    return result

entrada = input("Digite os numeros separados por espaço: ")

numeros = list(map(int, entrada.split()))

ordenado = counting_sort(numeros)

print("Array ordenado:", ordenado)
