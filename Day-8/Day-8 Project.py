# Corrigir bugs: permitir que sejam usados espaços, símbolos e letras;
# permitir números grandes no shift;
# permitir que o usuário seja redirecionado ao código caso ele deseje cifrar/decifrar novamente

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

continuar = True
while continuar == True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26 # Impede que o programa quebre se usar números muito grandes para o shift

    def caesar(text, shift, direction):
        palavra_nova = []
        for letter in text:
            if letter in alphabet:
                index_letra = alphabet.index(letter)
                if direction == 'encode':
                    nova_letra = alphabet[index_letra + shift]
                    palavra_nova.append(nova_letra)
                elif direction == 'decode':
                    nova_letra = nova_letra = alphabet[index_letra - shift]
                    palavra_nova.append(nova_letra)
                else:
                    print('Comando Inválido')
                    return
            else:
                palavra_nova.append(letter)

        palavra_nova = ''.join(palavra_nova)
        print(palavra_nova)

    caesar(text, shift, direction)

    novamente = input('Deseja Continuar? Sim ou Não\n')
    if novamente == 'Sim':
        continue
    elif novamente == 'Não':
        continuar = False
    else:
        print('Comando Inválido, finalizando.')

