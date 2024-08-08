jogos = int(input("Informe a quantidade de jogos vendidos: "))
valorjogo = 39.90 * jogos
bonus = 2.50 * jogos 
salario = valorjogo * 15 / 100
total = bonus + salario
print(f"o valor arrecadado {valorjogo:.2f}, o bônus é de {bonus:.2f} e o pagamento total é de {total:.2f}")