import random

def jogar():
    def mensagem_inicio():
        print("*********************************")
        print("Bem vindo no jogo de Adivinhação!")
        print("*********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000



    mensagem_inicio()

    print("Qual nível de dificuldade?")
    print("(1)Fácil  (2)Médio  (3)Difícil")

    nivel = int(input("Define o nível: "))
    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range(1,total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        chute = int(chute_str)
        print("Você digitou", chute)

        if (chute < 1 or chute > 100):
            print("Digite um número válido!!")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou, parabéns :D")
            print("Sua pontuação total foi:", pontos)
            break
        else:
            if(maior):
                print("Você errou, o seu chute foi maior do que o número :(")
            elif(menor):
                print("Você errou, o seu chute foi menor do que o número :(")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        rodada = rodada + 1

    print("Fim do jogo!!")
    print("*************************************")
    print("Jogo feito por Diego Rodrigues - 2022")
    print("*************************************")

if (__name__ == "__main__"):
    jogar()

