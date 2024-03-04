# Programa para saber o tipo de triangulo
# Desenvolvido por Christian

print("****************************************")
print("*        Tipo de Triangulos            *")
print("****************************************")
print()

# ENTRADA DOS DADOS
lado_a = int(input("Digite a quanto mede o lado A: "))
lado_b = int(input("Digite quanto mede lado B: "))
lado_c = int(input("Digite quanto mede o lado C: "))

# PROCESSAR OS VALORES PARA OBTER OS TTIPO DE TRIANGULO

if (lado_a < lado_b + lado_c) and (lado_b < lado_a + lado_c) and (lado_c < lado_a + lado_b):
    print("É um triangulo!")
    
    if (lado_a == lado_b) and (lado_b == lado_c):
        print("É um Equilátero!")

    elif (lado_a == lado_b) or (lado_a == lado_c ) or (lado_b == lado_c):
        print("É um Isósceles!")

    else: 
        print("É um Escaleno!")

else:
    print("Não é um triangulo!")
print()
print("****************************************")
print("*                Fim                   *")
print("****************************************")
