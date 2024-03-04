import random

print("****************************************")
print("*            Numero Secreto            *")
print("****************************************")
print()

numero_secreto = int(random.random() * 10)

tentativas = 3
rodada = 1
resposta = "s"

while resposta == "s":
    rodada = 1
    numero_secreto = int(random.random() * 10)
    while rodada <= tentativas:
        print (f"Tentativa {rodada}")
        
        numero = int(input("Digite o Numero Secreto: "))

        if numero == numero_secreto:
            print(f"{numero} é o numero correto")
            break

        if numero < numero_secreto:
            print ("Numero Secreto Maior")

        else:
            print ("Numero Secreto Menor")
        rodada = rodada + 1

        if rodada > tentativas:
            print (f"Tentativas Esgotadas, o numero secreto é {numero_secreto},você perdeu!")
    resposta = input("Jogar Novamente (s/n)")
print ("Fim")


# PROCESSAR
