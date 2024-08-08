
pessoas = int(input("Informe a quantidade de pessoas: "))
preco = float(input("Informe o preço do rodízio: "))
valor = pessoas * preco
if (pessoas >= 10): 
    valor = valor - preco
    print(f"Total a pagra: R${valor:.2f}")
else: 
    print(f"O total a ser pago: R${valor:.2f}")