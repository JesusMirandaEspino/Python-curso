mi_set = set([1,2,3,4,5])
otro_set = { 1,2,3,4,5, (1,2,3) }
s1 = {1,2,3,4}
s2 = {2,3,4,5,6,7}
s3 = s1.union(s2)
s3.add(8)
sorteo = s3.pop()
s3.discard(1)
print(type(mi_set))
print(mi_set)
print(type(otro_set))
print(otro_set)

print(len(mi_set))
print(2 in mi_set)
print(s3)
print(sorteo)
s3.clear()


mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}
mi_set_3 = mi_set_1.union(mi_set_2)

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
azar = sorteo.pop()
sorteo.discard(azar)