def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

entrada = input("Digite os numeros separados por espaços: ")

numeros = list(map(int, entrada.split()))

ordenado = merge_sort(numeros)

print("Array ordenado:", ordenado)
