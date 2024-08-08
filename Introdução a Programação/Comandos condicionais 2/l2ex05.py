#regra de negocio 
filme2D = 8.50
filme3D = 14.50
pipocamaisrefri = 10
pipocarefriechocolate = 12
#entrada
filme = str.upper(input("Informe se vai querer ver o filme em 2D ou 3D: "))
combo = str.upper(input("Informe se vai querer combo. Temos o simples (pipoca e refrigerante) e o completo (pipoca, refrigerante e chocolate): "))
#condições
if (filme == "3D"):
    if(combo == "SIMPLES"):
        total = pipocamaisrefri + filme3D
        print(f"{total:.2f}")
    elif(combo == "COMPLETO"):
        total =pipocarefriechocolate + filme3D
        print(f"{total:.2f}")
    else:
        print(f"{filme3D:.2f} ")

elif(filme == "2D"):
    if(combo == "SIMPLES"):
        total = pipocamaisrefri + filme2D
        print(f"{total:.2f}")
    elif(combo == "COMPLETO"):
        total = pipocarefriechocolate + filme2D
        print(f"{total:.2f}")
    else:
        print(f"{filme2D:.2f}")
    