import forca
import adivinhacao

def escolha_jogos():
    print("-"*40)
    print("Escolha o jogo que deseja:")
    print("1 - Forca \n2 - Adivinhação")
    print("-"*40)

    escolha = int(input("Sua opção: "))
    if escolha == 1:
        print("Jogo da forca")
        forca.jogo()
    elif escolha == 2:
        print("Jogo da adivinhação")
        adivinhacao.jogo()
        
if __name__ == "__main__":
    escolha_jogos()