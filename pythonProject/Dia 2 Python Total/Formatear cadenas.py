#funcion format
x = 10
y = 5
print("Mis numeros son {} y {}".format(x, y))
#ahora veremos una suma con fortmat

print("La suma de {} y {} es igual a {}".format(x, y, x+y))
#aunque tambien puedes hacerlo con una variable
z = x + y
print("La suma de {} y {} es igual a {}".format(x, y, z))
#Ahora con la funcion con cadenas literales "f"
color = "rojo"
matricula = 4352
print(f"El auto es {color} y su matricula es {matricula}")
#Pruebas de udemy
#Necesitamos imprimir el nombre y número de asociado dentro de la siguiente frase:Estimado/a (nombre_asociado), su número de asociado es: (numero_asociado)
nombre_asociado = "Jesse Pinkman"
numero_asociado = 399058
print("Estimado/a {}, su número de asociado es: {}".format(nombre_asociado, numero_asociado))
#Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase: Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos con formatear (f)
puntos_nuevos = 350
puntos_totales = 1225
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")
#Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos En esta ocasión, la cantidad de puntos acumulados (totales) será igual a los puntos_anteriores más los puntos_nuevos.
puntos_anteriores = 875
puntos_nuevos = 350
nuevos_puntos = puntos_nuevos + puntos_anteriores
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {nuevos_puntos} puntos")