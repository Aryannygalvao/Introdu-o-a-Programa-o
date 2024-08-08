qtdbrigadeiro = int(input("Informe quantos brigadeiros encomendou: "))
qtdbeijinhos = int(input("Informe a quantos beijinhos encomendou: "))
qtdcriancas = int(input("Informe quantas crianças convidou: "))
valorbrigadeiro = qtdbrigadeiro * 1.90
valorbeijinho = qtdbeijinhos * 1.70
totalgasto = valorbeijinho + valorbrigadeiro
cadacriancacome = (qtdbrigadeiro + qtdbeijinhos) // qtdcriancas
print(f"O total gasto foi de R${totalgasto:.2f} e cada criança vai comer {cadacriancacome} docinhos.")