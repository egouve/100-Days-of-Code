# Iniciando a criação de uma calculadora

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

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

print('Escolha um operador')

for sinal in operacao:
    print(sinal)

operador = input('')

funcao_operador = operacao[operador]
resultado = funcao_operador(n1,n2)

print(f'{n1} {operador} {n2} = {resultado}')