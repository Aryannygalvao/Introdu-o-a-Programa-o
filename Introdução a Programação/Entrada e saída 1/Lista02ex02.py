#ipva, se pagar com antecedência tem 5% de desconto 
ipva = float(input("Informe o valor do IPVA: "))
taxa_transito = float(input("Informe o valor da taxa Trânsito: "))
desconto = ipva * 5 /100
totaldesconto = ipva + taxa_transito - desconto
print(f"O total a ser pago é de R${totaldesconto:.2f} ")

