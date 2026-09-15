a=500
b=50

print(a < b)#False mayor que
print(a > b)#True menor que
print(a != b)#True distinto que
print(a == b)#Falso igual que
#condicional, es una estructura la
#cual ingresa al bloque de codigo miestra su condicion sea verdadera
#if a > b:
#    print("'a' es mayor a 'b'")
#sino else ingresa si no es verdadera la primera condicion if
"""
if a > b:
    print("a mayor a b")
else:
    print("a es menor o igual a b")        
 """
"""
dia = "viernes"

if dia == "martes":
    print("es martes")
elif dia == "miercoles":
    print("es miercoles")
elif dia == "jueves":
    print("es jueves")
elif dia =="viernes":
    print("es viernes")    
else:
    print("no se sabe que dia")
"""

usuario=None
password=None

usuario = input("Ingrese su usuario: ")
password = input("Ingrese su password: ")

# rolando@gmail.com y rolando12345 credenciales correctas

#operadores de union and or not

if usuario == "rolando@gmail.com" and password=="rolando12345":
    print("Bienvenido al sistema")
else:
    print("Credenciales no validas")    