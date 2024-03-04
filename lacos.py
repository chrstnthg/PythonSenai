voltas = 0

while voltas < 5:
    print("teste_loop")
    voltas = voltas + 1

print("Fim")

resposta = "s"

voltas = 1
while resposta == "s":
    print(f"Volta {voltas}")
    voltas = voltas + 1
    resposta = input("Continuar (s/n)?")
