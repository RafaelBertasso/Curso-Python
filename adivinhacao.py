import random

print("Bem vindo ao jogo de adivinhacao!")

n_aleatorio = random.randint(1,5)
n_usuario = int(input("Digite um numero de 1 a 5: "))
print(f"Seu chute foi {n_usuario}")
if n_aleatorio == n_usuario:
    print("-----Você acertou!-----")
elif n_usuario > 5:
    print("Numero nao disponivel")
else:
    print("-----Voce errou!-----")
    print(f"O numero era {n_aleatorio}")