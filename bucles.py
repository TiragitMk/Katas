#while se repite el bloque de codigo mientras la condicion sea verdadera True
"""
seguir = True

while seguir:
    print("esto es el while")

    fin = input("Deseas seguir con este while ? s/n")
    if fin =='n':
        seguir = False
        #break
        print("Esto se acabo")
"""

#while con else
"""
nombre="Juana"
while nombre =="Maria":
    print("Hola ",nombre)
else:
    print("No es Maria")
"""
x=0
while x < 100:
    x = x + 1   
    print(x) 

# se repite mientras se cumpla en numero de iteraciones definidas
# dentro del propio for variable range(inicio,final(el numero dado menos uno),salto(opcional))    

for iteracion in range(1,21):
    print(iteracion)


#realizar un programa muestre segun la opcion +(suma), -(resta), *(Multiplicacion), /(Division)
#de dos numeros ingresados por teclado, nos pedira ingrese el primer numero, ingrese el segundo,
#ingrese la operacion, el programa debe para solo si al final de la operacion escribo la palabra ,
#usar funciones