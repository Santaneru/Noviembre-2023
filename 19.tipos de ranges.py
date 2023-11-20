

#uso con list()para crear una lista de numeros

my_list = list(range(6))[3]
print(my_list)


#obtnecion de un elemnto especifico de la secuencia
value = range(1, 6)[2]
print(value)


new_list = [10,20,30,40,50]

for i in range(len(new_list)):
    print(new_list[i])

#uso de expresiones generadoras

square_generator = (x**2 for x in range(5))
for square in square_generator:
    print(square)


# In python ,the 'else' statemet in a 'for' loop is no alwawys necesary or obligatoary. 
# The basic estructure of a 'for' loop in Python is as allows:

# for element in iterable:
# codigo a ejecutr en cada iteracion
# else:
#codigo a iterar despues de que el bucle a terminado de iterar sobre todos los elementos del iterable

#Sin embargo si el bucle se interumpe prematuramente mediante la declaracion 'breake', entonces el bucle 'else' nos se ejecutara
    
for i in range(5):
    print(i)
    if i == 2:
        break
else:
    print("El bucle ha terminado")


for i in range(5):
    print(i)
else:
    print("El bucle ha terminado")
