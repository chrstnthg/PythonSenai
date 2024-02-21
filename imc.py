# Programa para calcular IMC
# Desenvolvido por Christian

print("****************************************")
print("*        CALCULADORA DE IMC            *")
print("****************************************")
print()

# CRIAÇÃO DAS VARIÁVEIS
nome = ""
peso = 0
altura = 0.0
imc = 0.0
situacao = ""

# ENTRADA DOS DADOS
nome = input("Digite o seu nome: ")
peso = int(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

# PROCESSAR OS VALORES PARA OBTER O IMC
imc = peso / altura ** 2

if imc < 18.5:
    situacao="abaixo do Peso"
elif imc > 18.5 and imc < 25:
    situacao="com o peso normal"
elif imc > 25 and imc < 30:
    situacao="com sobrepeso"
elif imc > 30 and imc < 35:
    situacao="com obesidade Grau 1 "
elif imc > 35 and imc < 40:
    situacao="com obesidade Grau 2 "
elif imc >= 40:
    situacao="com obesidade Grau 3 ou Morbida " 

# SAÍDA DO PROCESSAMENTO
print()
print("*******************************")
print("*          RESULTADO          *")
print("*******************************")
print("*                             *")
print("NOME: " + nome)
print("PESO: " + str(peso) + "Kg")
print("ALTURA: " + str(altura) + "m")
print("IMC: " + str(imc))
print(f"Você está {situacao}.")
