print("**********************************")
print("Bem-vindo ao jogo de Adivinhação!!")
print("**********************************")

numero_secreto = 42
chute = int(input("Digite um numero: "))
acertou = numero_secreto == chute
nunSecretoMaior = numero_secreto > chute
nunSecretoMenor = numero_secreto < chute

print("Você digitou ", chute)
if (acertou):
    print("Você acertou!")
else:
    print("Você errou!")
    if(nunSecretoMaior):
        print("número informado é menor que o número secreto")
    if(nunSecretoMenor):
        print("número informado é maior que o número secreto")

print("Fim do jogo.")