#Aqui con el index [] se puede ver que letra esta en el indice 0
mi_texto = "Esta es una prueba"
resultado = mi_texto[1]
print(resultado)
#para ver en que indice se encuentra una letra es de la siguiente forma, si buscaas una letra repetida eln sistema busca de izuierda a derecha y muestra la primer letra
prueba2 = "Esta es una prueba"
resultado2 = prueba2.index("prueba")
print(resultado2)
#si se agrega una coma luego de el indice el sistema busca a partir de el indice que pongas y si colocas otra coma seguida de la primer abuscara en un rango de dos indices que pongas
#si agregas r a el indes "rindex" buscara de derecha a izquierda
prueba2 = "Esta es una prueba"
resultado2 = prueba2.index("a", 4, 12)
print(resultado2)