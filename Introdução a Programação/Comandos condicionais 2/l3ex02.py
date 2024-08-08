#regra de negocio 
motorola = 879.18
samsungcelular = 921.40
multilaser = 339.50
tabletsamsung = 417.72
#entrada 
tipo = str.lower(input("Informe o tipo de aparelho: "))
modelo = str.lower(input("Informe o modelo: "))
quantidade = int(input("Informe a quantidade de clientes: "))
#condições 
if(tipo == "tablet"):
    if(modelo == "multilaser"):
        total = multilaser * quantidade
        print(f"{total:.2f}")
    else:
        total = tabletsamsung * quantidade
        print(f"{total:.2f}")
else: 
    if(modelo == "samsung"):
        total = samsungcelular * quantidade
        print(f"{total:.2f}")
    else: 
        total = motorola * quantidade
        print(f"{total:.2f}")
