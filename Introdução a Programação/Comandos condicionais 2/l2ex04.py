#Regra de negocio 
multa1hora = 30 
multa2até3 = 80
multa4 = 40
#Entrada
ValorDiaria = float(input("Informe o valor da diária: "))
Dias = int(input("Informe quantos dias foi o aluguel: "))
atraso =int(input("Informe os dias de atraso: ")) 
totaldiaria = ValorDiaria * Dias
if (atraso == 0):
    print(f"O valor a ser pago é de {totaldiaria:.2f}")
elif (atraso == 1): 
    total = multa1hora + totaldiaria
    print(f"O valor a ser pago é de {total:.2f}")
elif(atraso == 2) or (atraso == 3):
    if (atraso == 2):
        total = multa2até3 + totaldiaria
        print(f"O valor a ser pago é de {total:.2f}")
    else:
        total = multa2até3 + totaldiaria
        print(f"O valor a ser pago é de {total:.2f}")
else: 
    total = multa4 * atraso + totaldiaria
    print(f"O valor a ser pago é de {total:.2f} ")
