#converter reais para dolar (valor atual) 
#valor da taxa de cabio e fixo
#entrada e a quantidade de reais a serem convertidas e a taxa de cambio atual  e o valor de cada dolar, dve exibir o valor convertido em dolares 
reais = float(input("Digite a quantidade de reais a serem convertidos: R$ "))
taxadecambio = float(input("Digite a taxa de Câmbio: "))
taxa = reais / taxadecambio
print(f'O valor convertido em dólares é de: US${taxa:.2f}')