# Escolher um nome aleatório dentro da lista de nomes passadas no input

import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇

numero_pessoas = len(names)
numero_escolhido = random.randint(0, numero_pessoas - 1)
print(f'{names[numero_escolhido]} vai pagar a conta')