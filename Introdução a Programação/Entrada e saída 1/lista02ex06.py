pessoas = int(input("Informe quantas pessoas vão para o churrasco: "))
consumocarne = pessoas * 400 /1000
totalcarne = consumocarne * 41
consumocerveja = pessoas * 6 
totalcerveja = consumocerveja * 5.20
print(f"O gasto com carne é de R$ {totalcarne:.2f} e o de cerveja é de R${totalcerveja:.2f}")