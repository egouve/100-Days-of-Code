#Criar um sistema de leilão onde cada pessoa dará um valor, e o sistema dirá quem deu o maior valor
# Esse comando clear só funciona no replit, portanto, precisa ser rodado por lá

from replit import clear

# HINT: You can call clear() to clear the output in the console.

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
lances = {}
new_bidder = True

while new_bidder == True:

    nome = input('Qual o seu nome?\n')
    lance = int(input('Qual o lance?\nR$'))
    bidder = input('Há outros lances? S ou N\n').upper()
    lances[nome] = lance
    print(lances)

    if bidder == 'N':
        new_bidder = False
    elif bidder == 'S':
        clear()

maior_lance = 0
nome_vencedor = ''
for jogador in lances:
    lance_atual = lances[jogador]
    if lance_atual > maior_lance:
        maior_lance = lance_atual
        nome_vencedor = jogador
    else:
        maior_lance = maior_lance

print(f'Maior lance: {maior_lance}, por {nome_vencedor}')
