elefantes = [1,2,3,4,5,6,7,8,9,10]
incomodam ='incomodam, '

for numero_de_elefantes in elefantes:
    repeticao = incomodam * numero_de_elefantes
    if numero_de_elefantes % 2 == 0:
        print(f'{numero_de_elefantes} elefantes {repeticao[0:len(repeticao) - 2]} muito mais!')
    else:
        print(f'{numero_de_elefantes} elefante incomoda muita gente')

elefantes = elefantes[::-1]

for numero_de_elefantes in elefantes:
    repeticao = incomodam * numero_de_elefantes
    if numero_de_elefantes % 2 != 0:
        print(f'{numero_de_elefantes} elefantes {repeticao[0:len(repeticao) - 2]} muito mais!')
    else:
        print(f'{numero_de_elefantes} elefante incomoda muita gente')