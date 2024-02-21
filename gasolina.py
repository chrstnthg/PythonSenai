print ("**********************")
print ("*    Chega Rapido    *")
print ("**********************")

#variaveis
modelo_do_veiculo = ""
autonomia_do_veiculo = 0.0
distancia_da_viagem = 0.0
preco_do_combusivel = 0.0
quantidade_de_combustivel_gasta = 0.0
total_gasto_na_viagem= 0.0

#entrada

modelo_do_veiculo = input("Qual é o seu veiculo?")
autonomia_do_veiculo = int(input("Qual é a autonomia do veiculo?"))
distancia_da_viagem = int(input("Qual é a distancia da viagem ?"))
preco_do_combusivel = float(input("Qual é o preço da gasolina?"))

#saida

quantidade_de_combustivel_gasta = (distancia_da_viagem/autonomia_do_veiculo)
total_gasto_na_viagem = (quantidade_de_combustivel_gasta * preco_do_combusivel)

#resultado

print ("**********************************")
print (f"Modelo do Veículo {modelo_do_veiculo}")
print (f"Autonomia do Veículo {autonomia_do_veiculo} Km\l")
print (f"Distancia percorrida {distancia_da_viagem} km")
print (f"Valor do Combustivel R$ {preco_do_combusivel}")
print ()
print ("**********************************")
print (f"Quantidade de Combustivel gasta foi de {quantidade_de_combustivel_gasta:.2f} L")
print (f"Total gasto com a viagem foi de R$ {total_gasto_na_viagem:.2f}")
print ("**********************************")
