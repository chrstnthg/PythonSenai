print("********************")
print("*   MÉDIA FINAL    *")
print("********************")

# PROGRAMA PARA CALCULAR A MÉDIA FINAL

nome_do_aluno = ""
nota_bimestre1 = 0.0
nota_bimestre2 = 0.0
nota_bimestre3 = 0.0
nota_bimestre4 = 0.0
media_final = 0.0
situacao = ""
#ENTRADA DOS DADOS

nome_do_aluno = input("Qual o nome do aluno? : ")
nota_bimestre1 = float(input("Nota 1: "))
nota_bimestre2 = float(input("Nota 2: "))
nota_bimestre3 = float(input("Nota 3: "))
nota_bimestre4 = float(input("Nota 4: "))

#CALCULAR A NOTA FINAL
media_final = (nota_bimestre1 + nota_bimestre2 + nota_bimestre3 + nota_bimestre4)/4

if  media_final >=7:
    situacao= "Aprovado"
elif media_final <5:
    situacao = "Reprovado"
else:
    situacao= "Em recuperação"
    
# EXIBIR O RESULTADO
print()
print("**********************")
print("*   RESULTADO  FINAL *")
print("**********************")
print(f"{nome_do_aluno}, a sua media final é {media_final},e você está {situacao}")
print("**********************")
