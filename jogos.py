import adivinhacao
import forca

def mensagem_inicio():
    print("*********************************")
    print("******ESCOLHA O SEU JOGO!!*******")
    print("*********************************")


mensagem_inicio()

print("(1)FORCA  (2)ADIVINHAÇÃO")

jogo = int(input("Qual jogo? "))

if (jogo == 1):
    print("Jogo forca")
    forca.jogar()
elif (jogo == 2):
    print("Jogo adivinhação")
    adivinhacao.jogar()