if 10 > 9: 
    print('Es correcto')
    
if 5 == 2:
    print('Es correcto')
else:
    print('Es Incorrecto')
    
    
mascota = 'Gato'

if mascota == 'Gato':
    print('Tienes un Gato')
elif mascota == 'Perro':
    print('Tienes un Perro')
elif mascota == 'Pez':
    print('Tienes un Pez')
else:
    print('No se que animal Tienes')
    

edad = 16
calificacion = 9
if edad < 18:
    print('Es menor de edad')
    if calificacion > 5:
        print('Aprobo la Materia')
    else:
        print('Reprobo la Materia')
else:
    print('Es mayor de edad')
    
    
    
num1 = input("Ingresa un número:")
num2 = input("Ingresa otro número:")

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")