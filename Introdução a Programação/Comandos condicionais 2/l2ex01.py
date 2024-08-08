#Regra de negocio 
Bolsa_couro = 180 
Bolsa_tecido = 100
Relogio_couro = 150
Relogio_metal = 215
brinde = "Você ganhou um chaveiro de brinde"

#Entrada-> informações da compra
tipo = str.lower(input("Informe sua escolha, bolsa ou relógio? "))
if (tipo == "bolsa"):
    escolha = str.lower(input("Informe a sua escolha de material, couro ou tecido? "))
    if (escolha == "couro"):
        print(f"O valor da bolsa é de R${Bolsa_couro:.2f}")
    else: 
        print(f"O valor da bolsa é de R${Bolsa_tecido:.2f}")
if (tipo == "relógio"):
    escolha2 = str.lower(input("Informe a sua escolha do material, couro ou metal? "))
    if (escolha2 == "couro"):
        print(f"O valor do relógio é de R${Relogio_couro:.2f} é {brinde}")
    else: 
        print(f"O valor do relógio é de R${Relogio_metal:.2f} é {brinde}")