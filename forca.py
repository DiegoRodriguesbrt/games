import random

def mensagem_abertura():
    tentativas = 7
    print("*********************************")
    print("***Bem vindo no jogo de Forca!***")
    print("*********************************")

    print("Você tem {} tentativas para acertar, bora pro jogo!!".format(tentativas))

def sorteio_palavra():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def recebe_chute():
    chute = input("Qual letra?")
    chute = chute.strip().upper()
    return chute

def chute_correto(chute,letras_acertadas,palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
        index += 1

def desenha_forca(tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if(tentativas == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(tentativas == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativas == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("Você ganhou, parabéns :D")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Você perdeu :(")
    print("A palavra era {}".format(palavra_secreta))

def mensagem_copyright():
    print("*************************************")
    print("Jogo feito por Diego Rodrigues - 2022")
    print("*************************************")

def jogar():

    mensagem_abertura()

    palavra_secreta = sorteio_palavra()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativas = 0

    while (not enforcou and not acertou):

        chute = recebe_chute()

        if(chute in palavra_secreta):
            chute_correto(chute,letras_acertadas,palavra_secreta)
        else:
            tentativas += 1
            desenha_forca(tentativas)

        enforcou = tentativas == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()

    else:
        imprime_mensagem_perdedor(palavra_secreta)

    mensagem_copyright()






if (__name__ == "__main__"):
    jogar()




