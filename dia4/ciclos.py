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
    
    
combinacion = [ [1,2], [3,4], [5,6] ]
for a,b in combinacion:
    print(a)
    print(b)
    
    
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
for alumno in alumnos_clase:
    print(f'Hola {alumno}')
    
    
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0
for numero in lista_numeros:
    suma_numeros  = suma_numeros + numero