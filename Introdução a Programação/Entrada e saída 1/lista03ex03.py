mulheres = int(input("Informe a quantidade de funcionárias: "))
homens  = int(input("Informe a quantidade de funcionários: "))
vinho  = mulheres * 17
panetone = homens * 12.50
gastototal = vinho + panetone
gastomedia = (vinho + panetone) / (homens + mulheres)
print(f"O valor total gasto com presente foi de R${gastototal:.2f} o valor médio por funcionários foi de R${gastomedia:.1f}")
