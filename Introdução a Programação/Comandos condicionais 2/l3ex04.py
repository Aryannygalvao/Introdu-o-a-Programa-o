participante = str.upper(input("Informe se é EX-aluno ou convidado: "))
if(participante == "EX-ALUNO"):
    taxaexaluno = 60
    print(f"O valor a ser pago: R${taxaexaluno:.2f}")
else: 
    if(participante == "CONVIDADO"):
        idade = int(input("Informe a sua idade: "))
        if (idade < 3):
            taxa = 0
            print(f"O valor a ser pago: {taxa:.2f}")
        elif(idade >= 3) and (idade <= 11):
            taxa = 25
            print(f"O valor a ser pago: R${taxa:.2f}")
        elif(idade >= 12):
            taxa = 50 
            print(f"O valor a ser pago: R${taxa:.2f}")