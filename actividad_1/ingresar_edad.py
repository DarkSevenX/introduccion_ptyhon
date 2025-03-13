
edad: int 

while True:
    edad = int(input('ingrese su edad >> '))

    if edad < 1:
        print('Ingrese un numero entero valido')
        continue
    break

if edad < 18:
    print('Eres menor de edad')
elif edad > 65:
    print('Eres una persona de la tercera edad')
elif edad > 18 and edad < 65:
    print('Eres mayor de edad')

