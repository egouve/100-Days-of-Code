#Exercício 3 pede para calcular se o ano é um ano bissexto.

#Regras:
#Em todos os anos divisíveis por quatro com resto zero

# Exceto caso o ano seja divisível por 100 com resto zero

# Nesse caso, o ano só é bissexto se também for divisível por 400 com resto zero

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Lear year.')
        else:
            print('Not leap year.')
    else:
        print('Lear year.')
else:
    print("Not leap year.")