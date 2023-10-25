print("**********************************")
print("Bem-vindo ao jogo de Adivinhação!!")
print("**********************************")

numero_secreto = 42
chute = int(input("Digite um numero: "))

print("Você digitou ", chute)
if (numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você errou!")
 