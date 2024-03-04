menor_num = int(input("Menor Valor? "))
maior_num = int(input("Maior Valor? "))

if maior_num < menor_num:
    troca = maior_num
    maior_num = menor_num
    menor_num = troca

while menor_num <= maior_num:
    if menor_num % 2 == 1:
        print (f"IMPAR -> {menor_num}")

    print(f"{menor_num}")
    menor_num = menor_num + 1    
