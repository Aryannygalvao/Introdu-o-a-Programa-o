veiculos = int(input("Infome quantos carros estão estacionados no momento: "))
vagas = 42 - veiculos
ganhos  = veiculos * 3.75
possiveis = vagas * 3.75
print(f"O total ganho até o momento foi de {ganhos:.2f} as vagas livres são {vagas} e se essas vagas livres foresm ocupadas ao longo do dia ela vai receber R${possiveis:.2f}")