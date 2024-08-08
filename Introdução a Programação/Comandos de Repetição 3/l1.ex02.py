#regra de negocio 
numero = 0 
soma = 0
#entrada 
num = int(input("Digite um número: "))
#processamento 
while (num != 100):
    if (num % 2 == 0):
        numero += 1
    num = int(input("Digite um número: "))
#saída 
print(f"A média dos números pares é de {numero}")
