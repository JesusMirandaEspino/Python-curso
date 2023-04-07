mi_texto = 'hola'
mi_nuevo_texto = 'esta es una prueba'
l = mi_texto.index('o')
resultado = mi_nuevo_texto.index('prueba')
res_a = mi_nuevo_texto.index('a')
res_ar = mi_nuevo_texto.rindex('a')
res_a2 = mi_nuevo_texto.index('a',5)
res_a3 = mi_nuevo_texto.index('a',5, 10)
print(mi_nuevo_texto[9])
print(l)
print(resultado)
print(res_a)
print(res_a2)
print(res_a3)
print(res_ar)

palabra = "ordenador"
print(palabra[4])

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.index('práctica'))

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.rindex('práctica'))