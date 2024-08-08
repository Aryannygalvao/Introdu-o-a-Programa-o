#entrada 
sexo = str.lower (input("sexo: ")) 
peso = int(input("peso: "))
categoria = str.lower (input("categoria:"))
#processamento 
if(sexo == "feminino"): 
   if(peso <= 60) and (categoria == "peso pena"): 
      print("Pode competir") 
   elif(peso > 60) and (peso <= 72):
      if(categoria == "peso médio"):
        print("Pode competir")
      else:
        print("Não pode competir")
   else:
       print("Não pode competir")
else:
   if(peso <= 41) and (categoria == "peso pena"):
      print("pode competir")
   elif(peso > 41) and ( peso <= 55):
      if(categoria == "peso médio"):
        print("Pode competir")
      else: 
        print("não pode competir")
   elif(peso > 55) and (peso <= 62):
      if (categoria == "peso pesado"):
        print("Pode competir")
      else: 
        print("não pode competir")
   else:
      print("Não pode competir")
    