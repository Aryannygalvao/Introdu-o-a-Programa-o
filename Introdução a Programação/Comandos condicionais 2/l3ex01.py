#ENTRADATIME1
time1 = input("Informe o nome do time1: ")
pontostime1 = int(input("Informe os pontos da time1:  "))
saldogolstime1 = int(input("Informe o saldo de gols do time1: "))
golsfeitostime1 = int(input("Informe os gols feitos do time1: "))
#entradatime2
time2 = input("Informe o nome do time2: ")
pontostime2 = int(input("Informe os pontos do time2:  "))
saldogolstime2 = int(input("Informe o saldo de gols do time2: "))
golsfeitostime2 = int(input("Informe os gols feitos do time2: "))
#condições
if (pontostime1 > pontostime2): 
    print(f"{time1.lower()}")
elif (pontostime2 > pontostime1): 
    print(f"{time2.lower()}")
else: 
    if (saldogolstime1 > saldogolstime2): 
        print(f"{time1.lower()}")
    elif (saldogolstime2 > saldogolstime1):
        print(f"{time2.lower()}")
    else:
        if (golsfeitostime1 > golsfeitostime2):
            print(f"{time1.lower()}")
        elif(golsfeitostime2 > golsfeitostime1):
            print(f"{time2.lower}")
        else:
            print("EMPATE")