def radix_sort(arr):
    if not arr:
        return []

    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        arr = counting_sort_exp(arr, exp)
        exp *= 10
    return arr

def counting_sort_exp(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in reversed(range(n)):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    return output

entrada = input("Digite os numeros separados por espaço: ")
numeros = list(map(int, entrada.split()))
ordenado = radix_sort(numeros)
print("Array ordenado", ordenado)
