#a copiadora de Rio Tinto cobra o,15 por cópia
# entrada a quantidade de folhas de um livro e exibir o valor total a ser pago
# entrada  
folhas = int(input("Digite a quantidade de folhas impresas: ")) 
#processamento
valor = folhas * 2 * 0.15
#saída
print(f"O valor total a ser pago é de R${valor:.2f}")
#deu certo com os teste 