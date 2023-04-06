print('Escribe tu nombre')
nombre = input()
print('Escribe tu ventas')
ventas = int(input())

comision = ventas * 13 / 100
r_comision = round(comision)

print(f'Hola {nombre}, tu comisiones de este mes son {comision}')