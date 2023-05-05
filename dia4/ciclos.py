lista = ['a', 'b', 'c', 'd', 'e', 'f']

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print('letra: ', numero_letra, '.- ', letra)
    
    
nombres = [ 'Pablo', 'Luis', 'Pedro', 'Raul', 'Jose' ]

for nombre in nombres:
    if nombre.startswith('L'):
        print(nombre)
        
        
numeros = [ 1,2,3,4,5,6,7,8,9 ]
valor = 0
for numero in numeros:
    valor = valor + numero
    print(valor)
    
    
palabra = 'phyton'
for letra in palabra:
    print(letra)
    
    
combinacion = [ [1,2], [[3,4]], [[5,6]] ]
for a, b in combinacion:
    print(a)
    print(b)