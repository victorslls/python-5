numeros = ['1','2','3','4','5','6','7','8','9','10']
foiContado = []

for numero in numeros:
    foiContado.append(numero)
    resposta = ''
    if len(foiContado) == 1:
        resposta = foiContado[0]
    else:
        resposta = ', eh '.join(foiContado)
    print(f'''
    Mariana conta {numero}
    Mariana conta {resposta}
    Ana, viva a Mariana, viva a Mariana
    ''')