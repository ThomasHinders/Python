import random
print("-" * 30)
print("Pedra, Papel e Tesoura".center(28))
print("-" * 30)
print("""Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA""")
opcoes = ('Pedra', 'Papel', 'Tesoura')
jogador = int(input("Escolha uma opção: "))
pc = random.randint(0,2)
print('-' * 30)
print(f'Jogador jogou {opcoes[jogador]}')
print(f'PC jogou {opcoes[pc]}')
print('-' * 30)
if pc == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador venceu')
    elif jogador == 2:
        print('PC venceu')

if pc == 1:
    if jogador == 0:
        print('PC venceu')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador venceu')

if pc == 2:
    if jogador == 0:
        print('Jogador venceu')
    elif jogador == 1:
        print('PC venceu')
    elif jogador == 2:
        print('Empate')
