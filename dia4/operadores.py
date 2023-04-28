comparacion = 24 == 45
print(comparacion)

comparacion = 5 + 3 == 4 * 6
print(comparacion)

comparacion = 'blanco' == 'Blanco'
print(comparacion)

comparacion = 'blanco' != 'Blanco'
print(comparacion)

num1 = 36
num2 = 17
mi_bool = num1 >= num2

num1 = 25**0.5
num2 = 5
mi_bool = num1 == num2

num1 = 64*3
num2 = 24*8
mi_bool = num1 != num2

bool1 = 4 > 5 > 6
print(bool1)

bool2 = 4 < 5 and 5 > 6
print(bool2)

bool2 = (4 < 5) and (5 > 2 + 3)
print(bool2)

bool2 = (55 == 55) and ('perro' == 'perro')
print(bool2)

bool2 = (10 == 10) or (3 == 3)
print(bool2)

bool2 = not 10 == 10
print(bool2)

num1 = 36
num2 = 72/2
num3 = 48
mi_bool = num3 >  num1 > num2


num1 = 36
num2 = 72/2
num3 = 48
mi_bool =   num1 > num2 or num3 > num1

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"

mi_bool = not palabra1 in frase and not palabra2 in frase