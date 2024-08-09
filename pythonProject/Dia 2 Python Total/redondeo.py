print(90/7)
#ahora redondeando
print(round(90/7))
#ahora con variable
resultado = 90/7
redondeo = round(resultado)
print(redondeo)
#ahora pidiendo que se muestren decimales solo se vuelve un
valor = round(94.2345234)
print(valor)
#al redondear con round se vuelve un integer ej (solo se vuelve integer si se redondea dentro de la varaible)
print(type(valor))
#se puede pedir a round mostrar decimales round(operacion o numero, cantidad de decimales a mostrart)
print(round(90/7, 3))
#ejercicios de udemi
#Redondea el resultado de la división 10/3 a un número con 2 decimales, y muestra en pantalla el valor redondeado.
print(round(10/3, 2))
#tambien se podria
x = 10/3
redondeo = round(x, 2)
print(redondeo)
#Redondea el número 10.676767 al entero más próximo, y muestra en pantalla el resultado.
valor = 10.676767
redondeo = round(valor)
print(redondeo)
#o tambien
valor = 10.676767
print(round(valor))
#Calcula la raíz cuadrada de 5, y muestra en pantalla el resultado redondeado con 4 posiciones decimales.
valor = 5**0.5
print(round(valor, 4))
