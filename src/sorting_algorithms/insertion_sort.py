def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

entrada = input("Digite os números separados por espaço: ")

numeros = list(map(int, entrada.split()))

ordenado = insertion_sort(numeros)

print("Array ordenado:", ordenado)
