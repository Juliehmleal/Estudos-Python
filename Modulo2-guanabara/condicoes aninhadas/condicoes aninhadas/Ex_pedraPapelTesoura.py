from random import randint

jogadas = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0, 2)

print('''Escolha uma opção
[1] para Pedra
[2] para Papel
[3] para Tesoura''')
opcao = int(input("Opcao: "))
opcao -= 1

print("-="*11)
print('jogador jogou {}'.format(jogadas[opcao]))
print('Computador jogou {}'.format(jogadas[computador]))
print("-="*11)

if computador == 0:
    if opcao == 0:
        print("Empate")
    elif opcao == 1:
        print("Jogador ganhou")
    else:
        print("Jogador perdeu")
elif computador == 1:
    if opcao == 0:
        print("Jogador perdeu")
    elif opcao == 1:
        print("Empate")
    else:
        print("Jogador ganhou")
elif computador == 2:
    if opcao == 0:
        print("Jogador ganhou")
    elif opcao == 1:
        print("Jogador perdeu")
    else:
        print("Empate")
else:
    print("ERRO")
