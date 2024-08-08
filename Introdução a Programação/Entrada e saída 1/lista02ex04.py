refeicao = float(input("Informe o peso da sua refeição (em gramas):"))
pratovazio = refeicao - 230 
gramapquilo = pratovazio / 1000
valorpquilo = gramapquilo * 40
print(f"O preço cobrado é de R${valorpquilo:.2f}")