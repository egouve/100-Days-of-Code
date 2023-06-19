# Jogo do mapa do tesouro. Digite dois números de 1 a 3 para decidir onde será printado o X

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆
#Write your code below this row 👇

coluna = int(position[0])
linha = int(position[1])

map[linha - 1][coluna - 1] = 'X'


# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")