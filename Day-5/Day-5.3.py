# O obetivo é criar um for loop usando range que some todos os números pares de 1 a 100

total = 0

for pares in range(2,101, 2):
    total += pares

print(total)