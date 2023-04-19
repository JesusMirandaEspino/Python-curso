texto = 'Este es un texto'
a = 'aprender'
b = 'phyton'
c = ' '.join([a,b])
resultado = texto.upper()
print(resultado)

resultado = texto.split()
print(resultado)

resultado = texto.lower()
print(resultado)

resultado = texto.find('s')
print(resultado)

resultado = texto.replace('texto', 'escrito')
print(resultado)

print(c)

frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
r = frase.upper()
print(r)

lista_palabras = ["La","legibilidad","cuenta."]
lista = ' '.join(lista_palabras)
print(lista)

texto = 'Si la implementación es difícil de explicar, puede que sea una mala idea.'
parte1 = texto.replace('difícil', 'fácil')
parte2 = parte1.replace('mala', 'buena')
print(parte2)

saludo1 = 'Ho'
saludo2 = 'la'
print(saludo1 * 10)
poema = """Este es un texto de ejmplo
que sirve para hacer pruebas con phyton"""

print('texto' in poema)
print(len(poema))

print("Repetición" * 15)


poema = """Tierra mojada
mis recuerdos de viaje,
entre las lluvias"""

print('agua' in poema)