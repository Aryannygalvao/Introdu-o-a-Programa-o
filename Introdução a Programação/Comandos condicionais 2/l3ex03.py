#regra de negocio
plateiaVip = 350
cadeira = 200
arquibancada = 100
#entrada 
setor = str.lower(input("Informe o setor: "))
ingresso = str.lower(input("Informe o tipo de ingresso: "))
#condições 
if(setor == "plateia vip"):
    if(ingresso == "inteira"):
        taxa = plateiaVip * 5 / 100
        plateia = plateiaVip + taxa
        print(f"o valor a ser pago: R${plateia:.2f}")
    else: 
        print("Tipo de ingresso inválido")
elif(setor == "cadeira"): 
    if(ingresso == "inteira"): 
        taxa = cadeira * 5 / 100
        cadei = cadeira + taxa
        print(f"O valor a ser pago: R${cadei:.2f}")
    else: 
        desconto = cadeira * 50 / 100
        taxa =  cadeira * 5 /100
        cade = taxa + desconto
        print(f"O valor a ser pago: R${cade:.2f}")
elif(setor == "arquibancada"):
    if(ingresso == "inteira"):
        taxa = arquibancada * 5 / 100
        arqui = arquibancada + taxa
        print(f"O valor a ser pago: R${arqui:.2f}")
    else: 
        desconto = arquibancada * 50 / 100
        taxa = arquibancada * 5 /100
        arqui = taxa + desconto
        print(f"O valor a ser pago: {arqui:.2f}")
else: 
    if (setor == "camarote"):
        print("setor inválido")