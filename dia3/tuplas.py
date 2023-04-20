mi_tupla = (1,2,3,4,5,6, (10, 20))
t = (1,2,3, 'a', 'b', 'c')
print(mi_tupla)
print(mi_tupla[2])
print(mi_tupla[6][0])
print(len(t))
print(t.count(2))
print(t.index(2))


mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)

mi_tupla = (1, 2, 3, 4)
a,b,c,d = mi_tupla