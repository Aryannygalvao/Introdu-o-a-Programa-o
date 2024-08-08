revista = int(input("Informe a quantidade de revista: "))
amigos = int(input("Informe a quantidade de amigos: "))
cada = revista // amigos 
resta = revista % amigos
print(f"Revista doada a cada amigo {cada} e as revistas restantes {resta}")