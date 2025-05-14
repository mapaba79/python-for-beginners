def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

entrada = input("Digite os numeros separados por espaços: ")

numeros = list(map(int, entrada.split()))

ordenado = quick_sort(numeros)

print("Array ordenado:", ordenado)
