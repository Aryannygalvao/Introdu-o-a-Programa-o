#regra de negocio 
xérox_em_pb = 0.06
xérox_color = 0.29
encadernacao = 2.00
encadernacao100 = 4.00
#entrada 
tiposervico = str.lower(input("Informe qual será o serviço, xérox ou encadernação? "))
folhas = int(input("Informe a quantidade de folhas: "))
if (tiposervico == "xérox"):
    pb_ou_colorida = str.lower(input("Informe se será preto e branco ou colorida: "))
    if (pb_ou_colorida == "preto e branco"): 
        valor = folhas * xérox_em_pb
        print(f"O valor é de {valor:.2f}")
    else: 
        valor = folhas * xérox_color
        print(f"O valor é de R${valor:.2f}")
else:
    if (folhas <= 100): 
        print(f"O valor da encadernação é de {encadernacao:.2f}")
    else:
        print(f"O valor da encadernação é de {encadernacao100:.2f}")