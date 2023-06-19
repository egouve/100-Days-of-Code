# Desafio fizzbuzz. Prinar números de 1 a 100
# Se o número for divisível por 3, printar fizz
# Se for divisível por 5, printar buzz
# Se for divisível por 3 e 5, printar fizzbuzz

for numero in range(1,101):
    if numero % 3 == 0 and numero % 5 != 0:
        print('Fizz')
    elif numero % 5 == 0 and numero % 3 != 0:
        print('Buzz')
    elif numero % 3 == 0 and numero % 5 == 0:
        print('FizzBuzz')
    else:
        print(numero)