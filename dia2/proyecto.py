print('Escribe tu nombre')
nombre = input()
print('Escribe tu ventas')
ventas = int(input())

comision = round(ventas * 13 / 100)

print(f'Hola {nombre}, tu comisiones de este mes son {comision}')