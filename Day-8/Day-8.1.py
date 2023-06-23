#Criar uma função que calcule a quantidade de tinta usada para pintar uma área

#Write your code below this line 👇

def calcular_quantidade(test_h, test_w, coverage):
    total_tinta = round((test_h * test_w) / coverage)
    print(f'Será usado um total de {total_tinta} latas de tinta.')



#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
calcular_quantidade(test_h, test_w, coverage)