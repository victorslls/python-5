patinhos = [5,4,3,2,1]
texto = ''

for patinho in patinhos:
    sobra = patinho - 1
    if patinho == 1:
        texto = 'um'
        sobra = 'nenhum'
    elif patinho == 2:
        texto = 'dois'
        sobra = 'um'
    elif patinho == 3:
        texto = 'tres'
        sobra = 'dois'
    elif patinho == 4:
        texto = 'quatro'
        sobra = 'tres'
    elif patinho == 5:
        texto = 'cinco'
        sobra = 'quatro'
    print(f'''
    {texto} patinhos foram passear
    Alem das montanhas
    Para brincar
    A mamae gritou: Qua, qua, qua, qua
    Mas {sobra} voltaram de la.
    ''')

print('''
    A mae patinha foi procurar
    Alem das montanhas
    Na beira do mar
    A mamae gritou: Qua, qua, qua, qua
    E os cinco patinhos voltaram de la.
''')