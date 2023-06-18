# Objetivo do exercício é simular uma jogada da moeda

# Remember to use the random module
# Hint: Remember to import the random module here at the top of the file. 🎲

# 🚨 Don't change the code below 👇
import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# 🚨 Don't change the code above 👆 It's only for testing your code.
jogada = random.randint(0,1)
if jogada == 0:
    print('Cara.')
else:
    print('Coroa.')