#Take both people's names and check for the number of times the letters in the word TRUE occurs.

#Then check for the number of times the letters in the word LOVE occurs.

#Then combine these numbers to make a 2 digit number.

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

nome_1 = name1.lower()
nome_2 = name2.lower()

nome_completo = name1 + name2

t = nome_completo.count('t')
r = nome_completo.count('r')
u = nome_completo.count('u')
e = nome_completo.count('e')
l = nome_completo.count('l')
o = nome_completo.count('o')
v = nome_completo.count('v')

pontuacao_true = t + r + u + e
pontuacao_love = l + o + v + e

pontuacao_total = str(pontuacao_true + pontuacao_love)

if pontuacao_total < 10 or pontuacao_total > 90:
    print(f"Your score is {pontuacao_total}, you go together like coke and mentos.")
elif final_score >= 40 and pontuacao_total <= 50:
    print(f"Your score is {pontuacao_total}, you are alright together.")
else:
    print(f"Your score is {pontuacao_total}.")