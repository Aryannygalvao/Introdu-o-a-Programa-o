tempo = float(input("Informe quantos minutos leva para analisar cada processo: "))
hora = 60 / tempo
trabalhos = 8 * hora
print(f"o total de processos revisados em um dia é de {trabalhos:.0f}")