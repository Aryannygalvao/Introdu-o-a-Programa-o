#o bar cobra 12% de taxa de serviço, a entrada deve ser o valor da conta e deve exibir o que o garçom deve receber de taxa de serviço e o valor da conta 
conta = float(input("Digite o valor da conta:"))
taxadogarçom = conta * 12 / 100
valorconta = conta + taxadogarçom
print(f"A taxa do garçom é de R$ {taxadogarçom:.2f}, e o valor total da conta é de R$ {valorconta:.2f}")