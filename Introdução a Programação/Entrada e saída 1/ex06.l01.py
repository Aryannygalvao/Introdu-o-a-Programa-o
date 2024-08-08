
horasala = float(input("Digite a quantidade de Horas em sala de aula no mêS: "))
projetos  = int(input("Digite a quantidade de projetos participou durante esse mês: "))
cadaaula = horasala * 35
cadaprojeto = projetos * 80
salario = cadaaula + cadaprojeto
print(f"O salario do professor é de R$ {salario:.2f}")
 