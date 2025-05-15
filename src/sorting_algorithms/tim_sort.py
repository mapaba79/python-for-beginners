entrada = input("Digite os numeros separados por espaço: ")

numeros = list(map(int, entrada.split()))

numeros.sort()

print("Array ordenado:", numeros)
