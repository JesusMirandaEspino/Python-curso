diccionario = { 'c1': 'valor1', 'c2': 'valor2'}
diccionario['c3'] = 'valor3'
cliente = { 'nombre': 'Jesus', 'apellido': 'Miranda', 'peso': 80, 'altura':1.76 }
lista = { 'c1': 55, 'c2': [10,20,30], 'c3': { 's1': 100, 's2': 200 } }
nueva_lista = { 'c1': 55, 'c2': [10,20,30], 'c3': { 's1': 'a', 's2': 'c' } }
#nombre: Karen
#apellido: Jurgens
#edad: 35
#ocupacion: Periodista
mi_dic = { 'nombre': 'Karen', 'apellido': 'Jurgens', 'edad': 35, 'ocupacion': 'Periodista' }
consulta = (cliente['apellido'])
print(diccionario)
print(diccionario['c1'])
print(consulta)
print(lista['c2'][1])
print(lista['c3']['s2'])
print(nueva_lista['c3']['s2'].upper())
print(lista.keys())