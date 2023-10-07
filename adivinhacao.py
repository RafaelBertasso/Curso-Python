import random

print("Bem vindo ao jogo de adivinhacao!")

n_aleatorio = random.randint(1,5)

tentativas = 3
for i in range(1,tentativas + 1):
    n_usuario = int(input("Digite um numero de 1 a 5: "))
    if n_aleatorio == n_usuario:
        print("-----Você acertou!-----")
        break
    elif n_usuario > 5:
        print("Numero nao disponivel")
    else:
        print("-----Voce errou!-----")
print(f"O numero era {n_aleatorio}")