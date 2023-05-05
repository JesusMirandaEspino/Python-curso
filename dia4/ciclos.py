lista = ['a', 'b', 'c', 'd', 'e', 'f']

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print('letra: ', numero_letra, '.- ', letra)
    
    
nombres = [ 'Pablo', 'Luis', 'Pedro', 'Raul', 'Jose' ]

for nombre in nombres:
    if nombre.startswith('L'):
        print(nombre)