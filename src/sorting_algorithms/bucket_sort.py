def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def bucket_sort(arr):
    if not arr:
        return []

    n = len(arr)
    buckets = [[] for _ in range(n)]

    for num in arr:
        index = int(num * n)
        buckets[index].append(num)

    for i in range(n):
        buckets[i] = insertion_sort(buckets[i])

    result = []
    for bucket in buckets:
        result.extend(bucket)
    return result

entrada = input("Digite os numeros separados por espaço: ")

numeros = list(map(float, entrada.split()))

ordenado = bucket_sort(numeros)

print("Array ordenado:", ordenado)
