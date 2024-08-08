#Regra de negocio
quantiletras = 0
#entrada 
letras = str.lower(input("Digite uma letra: "))
#processamento 
while (letras != "x"):
    if (letras == "y") or (letras == "k") or (letras == "w"):
        quantiletras += 1
    letras = str.lower(input("Digite uma letra: "))
#saída
print(f"Quantidade de letras especiais {quantiletras}")