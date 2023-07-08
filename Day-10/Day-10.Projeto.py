# Finalizar a calculadora
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)
def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def dividir(n1, n2):
    return n1 / n2

def multiplicar(n1, n2):
    return n1 * n2

operacao = {
    '+': somar,
    '-': subtrair,
    '/': dividir,
    '*': multiplicar
}

def calculadora():
    finalizar = False
    n1 = float(input('Primeiro número: '))
    while finalizar == False:
        print('Escolha um operador')

        for sinal in operacao:
            print(sinal)

        operador = input('')
        n2 = float(input('Escolha outro número: '))

        funcao_operador = operacao[operador]
        resultado = funcao_operador(n1,n2)

        print(f'{n1} {operador} {n2} = {resultado}')

        continuar = input('Deseja continuar? S para continuar ou N para começar de novo\n').upper()
        if continuar == 'S':
            n1 = resultado

        elif continuar == 'N':
            finalizar = True
            calculadora()
        else:
            print('Comando Inválido, finalizando.')
            break

calculadora()