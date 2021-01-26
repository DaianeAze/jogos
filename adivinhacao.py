print("***************************************")
print("Bem vindo ao jogo de Adivinhação!")
print("***************************************")

numero_secreto = 20
maximo_tentativas = 3
rodada = 1

while(rodada <= maximo_tentativas):
    print("Tentativa {} de {}".format(rodada, maximo_tentativas))
    chute = int(input("Digite o seu numero:"))
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
    rodada = rodada + 1
print("Fim de jogo.")