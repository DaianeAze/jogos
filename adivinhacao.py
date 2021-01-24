print("***************************************")
print("Bem vindo ao jogo de Adivinhação!")
print("***************************************")
numero_secreto = 20
chute = int(input("Digite o seu numero:"))
print("Você digitou o número", chute)
if (numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você errou.")