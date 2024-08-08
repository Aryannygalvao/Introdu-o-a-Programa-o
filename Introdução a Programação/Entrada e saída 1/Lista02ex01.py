convenio = int(input("quantas consultar por convênio o médico atendeu nessa semana? "))
particular = int(input("Quantas consultas pelo particular o médico atendeu nessa semana? "))
cadaconvenio = convenio * 170
cadaparticular = particular * 310
totaldasconsultas = cadaconvenio + cadaparticular
print(f"Pelo convênio foram {convenio}, as consultas particular foram {particular}. O valor total recebido pelo médico por consulta foi de R$ {totaldasconsultas:.2f} nessa semana." )