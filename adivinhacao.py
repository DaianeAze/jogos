import random
def jogar():
    print("***************************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("***************************************")

    numero_secreto = random.randrange(1, 101)
    maximo_tentativas = 3
    rodada = 1

    for rodada in range(1, maximo_tentativas + 1 ):
        print("Tentativa {} de {}".format(rodada, maximo_tentativas))
        chute = int(input("Digite o seu numero entre 1 e 100:"))
        print("Você digitou o número", chute)
        acertou = numero_secreto == chute
        maior   = numero_secreto < chute
        menor   = numero_secreto > chute

        if (acertou):
            print("Você acertou!")
            break
        else:
            print("Você errou.")
            if(maior):
                print("Seu chute foi maior que o número.")
            elif(menor):
                print("Seu chute foi menor que o número.")
    print("Fim de jogo.")