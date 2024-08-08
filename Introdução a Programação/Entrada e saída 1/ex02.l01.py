#Exercício 2 python 
#se o usuário atrasar terá que pagar uma multa de 2,50 por dia de atraso
#ele quer que a entrada seja a quantidades de dias em atraso do empréstimo de um livro, e exiba o valor da multa
atraso = int(input("Digite a quantidade de dias que seu livro está atrasado na biblioteca: "))
multa  = atraso * 2.50
print(f"O valor da sua multa na biblioteca é de R${multa:.2f}")
#deu certo os dados de teste 