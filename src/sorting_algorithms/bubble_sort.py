def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

entrada = input("Digite os números separados por espaço: ")

numeros = list(map(int, entrada.split()))

ordenado = bubble_sort(numeros)

print("Array ordenado:", ordenado)
