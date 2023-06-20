#Criar um gerador de senha. Tem o nível fácil e o difpicil

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

letras_aleatorias = random.choices(letters, k=nr_letters)
chave = []

for letra in range(nr_letters):
    letra_aleatoria = random.choice(letters)
    chave.append(letra_aleatoria)

for simbolo in range(nr_symbols):
    simbolo_aleatorio = random.choice(symbols)
    chave.append(simbolo_aleatorio)

for numero in range(nr_numbers):
    numero_aleatorio = random.choice(numbers) # Dessa forma, ele é tratado como string, não como int
    chave.append(numero_aleatorio)


nova_senha = ''.join(chave)
print(nova_senha)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random.shuffle(chave)
nova_senha_aleatoria = ''.join(chave)
print(nova_senha_aleatoria)

