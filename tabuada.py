multiplicador = int(input("Escolha a tabuada ?"))
minimo_multiplicador = int(input("Por onde quer começar ?"))
maximo_multiplicador = int(input("Até onde quer ir ?"))
print (f"Tabuada Do {multiplicador}")
print ("---------------------------")
while minimo_multiplicador <= maximo_multiplicador:
    total = multiplicador * minimo_multiplicador
    print (f"{multiplicador} X {minimo_multiplicador}= {total}")
    minimo_multiplicador = minimo_multiplicador + 1

print ("---------------------------")
print ("-------------Fim-----------")
print ("---------------------------")
