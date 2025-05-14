def heap_sort(arr):
    import heapq
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

entrada = input("Digite os numeros separados por espaço: ")

numeros = list(map(int, entrada.split()))

ordenado = heap_sort(numeros)

print("Array ordenado:", ordenado)
