def jogar():
    print("***************************************")
    print("Bem vindo ao jogo de Forca!")
    print("***************************************")

    palavra_secreta = 'abacaxi'.upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):
        chute = input("Qual a letra?")
        chute = chute.strip().upper()

        index = 0
        if (chute in palavra_secreta):
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Trecho não existe na palavra.")

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (enforcou):
        print("SE ENFORCOU! Você excedeu o limite de tentativas.")
    if (acertou):
        print("PARABÉNS! Você acertou a palavra antes de se enforcar.")
    print("Fim de jogo")


if (__name__ == "__main__"):
    jogar()
