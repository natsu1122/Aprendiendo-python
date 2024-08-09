#conversiones implicitas, python las realiza de forma automatica
num1 = 20 #int
num2 = 30.5 #float
#aqui python cambia su valor a tipo float de num1
num1 = num1 + num2

print(type(num1))
print(type(num2))
#aqui veremos la conversion explicitas
print("aqui sigue la segunda parte")
num3 = 5.8
print(num3)
print(type(num3))

num4 = int(num3)
print(num4)
print(type(num4))
#parte 3 con los input convirtiendo un string (texto) a un int (numero) recuerda que cuando pides con input al usuario ingresar un dato
#este dato se vuelve un string(texto) aunque sea un numero

edad = input("Dime tu edad")
print(type(edad))

edad = int(edad)
print(type(edad))

nueva_edad = 12 + edad

print(nueva_edad)

#pruebas de udemi
#Convierte el valor de num1 en un int e imprime el tipo de dato que resulta:
num1 = 7.5
num2 = int(num1)
print(type(num2))
#Convierte el valor de num2 en un float e imprime el tipo de dato que resulta:
num2 = 10
num3 = float(num2)
print(type(num3))
#No modifiques el valor de las variables ya declaradas, sino aplica las conversiones necesarias dentro de la funcion print
num1 = "7.5"
num2 = "10"

resultado = float(num1) + float(num2)
print(resultado)