texto = input('Ingresa el texto')
letras = []
texto = texto.lower()

letras.append( input('Ingresa la primera letra').lower() )
letras.append( input('Ingresa la segunda letra').lower() )
letras.append( input('Ingresa la tercera letra').lower() )

print('')
print('Cantidad de letras')
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[0])
cantidad_letras3 = texto.count(letras[0])

print( f'Hemos encontrado la letra {letras[0]} repetiva {cantidad_letras1} veces' )
print( f'Hemos encontrado la letra {letras[1]} repetiva {cantidad_letras2} veces' )
print( f'Hemos encontrado la letra {letras[2]} repetiva {cantidad_letras3} veces' )

print('')
print('Cantidad de palabras')
palabras = texto.split()
print('Cantidad de las palabras es {len(palabras)}')

print('')
print('Letras de inicio y fin')
letra_ini = texto[0]
letra_f = texto[-1]
print(f'La letra de inicio del texto es {letra_ini} y la letra final es {letra_f}')

print('')
print('Texto invertido')
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f'El texto inverido es {texto_invertido}')


print('')
print('Buscando la palabra phyton')
buscar = 'phyton' in texto
dic = {True:'si', False:'no'}
print(f'La palabra phyton {dic[buscar]} se encuentra en el texto')



