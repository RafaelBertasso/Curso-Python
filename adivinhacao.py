import random
print("-"*40)
print("Bem vindo ao jogo de adivinhacao!")
print("-"*40)

n_aleatorio = random.randint(1,100)
tentativas = 0
pontuacao = 1000

print("Dificuldade do jogo:")
print("(1) - Fácil \n(2) - Médio \n(3) - Difícil")
nivel = int(input("Dificuldade = "))

if nivel == 1:
    tentativas = 20
elif nivel == 2:
    tentativas = 10
elif nivel == 3:
    tentativas = 3
else:
    print("Dificuldade invalida")

for i in range(1,tentativas + 1):
    n_usuario = int(input("Digite um numero de 1 a 100: "))
    print(f"Tentativa {i} de {tentativas}")
    if n_aleatorio == n_usuario:
        print("-----Você acertou!-----")
        print(f"Você fez {pontuacao} pontos")
        break
    elif n_usuario > 100:
        print("Numero nao disponivel")
    else:
        print("-----Voce errou!-----")
        pontos_perdidos = abs(n_aleatorio - n_usuario)
        pontuacao -= pontos_perdidos
        print(f"Você fez {pontuacao} pontos")
print(f"O numero era {n_aleatorio}")