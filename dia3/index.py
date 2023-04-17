mi_texto = 'hola'
mi_nuevo_texto = 'esta es una prueba'
l = mi_texto.index('o')
resultado = mi_nuevo_texto.index('prueba')
res_a = mi_nuevo_texto.index('a')
res_ar = mi_nuevo_texto.rindex('a')
res_a2 = mi_nuevo_texto.index('a',5)
# res_a3 = mi_nuevo_texto.index('a',5, 10)
print(mi_nuevo_texto[9])
print(l)
print(resultado)
print(res_a)
print(res_a2)
# print(res_a3)
print(res_ar)

palabra = "ordenador"
print(palabra[4])

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.index('práctica'))

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.rindex('práctica'))

otroTexto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
fragmento = otroTexto[2:5]
print(fragmento)

fragmento = otroTexto[:5]
print(fragmento)

fragmento = otroTexto[2:]
print(fragmento)

fragmento = otroTexto[2:5:2]
print(fragmento)

fragmento = otroTexto[::2]
print(fragmento)

frase = "Controlar la complejidad es la esencia de la programación"
fragmento = frase[:9]
print(fragmento)


frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
fragmento = frase[8::3]
print(fragmento)


frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
fragmento = frase[::-1]
print(fragmento)