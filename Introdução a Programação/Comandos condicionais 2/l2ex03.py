#regra de negocio
gasolina = 2.53
etanol = 2.09
diesel = 1.92
etanol30 = "Você ganhou uma troca de óleo"
nãoganhou = "Você não ganhou a troca de óleo"
#entrada 
combustivelEscolhido = str.lower(input("Informe o combustível escolhido: "))
valorCombustivel = float(input("Informe o valor em dinheiro que deseja gastar: "))
if(combustivelEscolhido == "gasolina"):
    valor = valorCombustivel / gasolina
    print(f"O total de combustível abastecido {valor:.2f} litros é {nãoganhou}.")
elif (combustivelEscolhido == "etanol"):
    valor = valorCombustivel / etanol
    if (valor >= 30):
        print(f"O total do combustível abastecido {valor:.2f} litros é {etanol30}.")
    else: 
        print(f"O total de combustível abastecido {valor:.2f} litros é {nãoganhou}.")
else: 
    valor = valorCombustivel / diesel
    print(f"O total de combustível abastecido {valor:.2f} litros é {nãoganhou}.")