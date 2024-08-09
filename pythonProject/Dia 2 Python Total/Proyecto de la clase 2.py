print( "Hola, vamos a calcular tus ventas por favor ingresa tus datos")
nombre = input("dime tu nombre: ")
ventas = int(input("Dime el valor de tus ventas: "))
# aca puedes convertir a variable a int con :ventas = int(ventas) o agregarlo a la propia variable antes de input
comision = round(ventas * 13 / 100)
#del mismo modo puedes ahoorar lineas redondeando directamente en la variable en ves de usar comision = round(comision, 2)
print(f"Hola {nombre} tus ventas de este mes fueron ${ventas} dandote una comisión de ${comision} \nFelicidades!")
