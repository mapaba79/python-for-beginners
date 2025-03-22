sum = 0
n = int(input("Enter a positive integer: "))

for i in range(2, n + 1, 2):
    sum += i

print(f"Sum of even numbers from 2 to {n} is {sum}")