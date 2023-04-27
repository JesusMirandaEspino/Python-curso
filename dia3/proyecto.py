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

