def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

entrada = input("Digite os numeros separados por espaços: ")

numeros = list(map(int, entrada.split()))

ordenado = selection_sort(numeros)

print("Array ordenado:", ordenado)
