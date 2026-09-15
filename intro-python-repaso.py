#comentarios en una sola linea

"""
comentarios en varias lineas
esto si mola
"""
'''
otra forma de comentar
en varias lineas
'''

#salida de informacion
print("Salida de información")

#entrada de información
#nombre = input("Ingrese su 'nombre': ")
# un input capura el dato ingresado por terminal y siempre lo devuelve en formato str
#print("Su nombre es "+nombre+ " es un alumno")

#tipos de variables en python
#str "@dflkdjflkdjflkd54545454)?"
#int 100
#float 1000.5
#bool True False
variable=100.5
print(type(variable))

#Variables sensible a mayusculas y minusculas
variable1="Carlos"
vARIable1="Ivan"
Variable1="Jose"
print(variable1)
print(vARIable1)
print(Variable1)

nombre=None

def nombrar(nom:str)->float:
    return

#las variables de python son flexibles
nombre = "Rolando"
print(nombre)
nombre = True
print(nombre)
nombre = 100
print(nombre)

#reglas de nombres de variables
#nombres de variables y funciones van en minusculas
#nombres de clases con la primera letra en mayuscula
#nombre de variables de tipo constante VALOR_PI=3.1434554
#DECLARACION DE VARIABLES

#NO SE PUEDE
#Numero entes de una letra en nombre de variable
#10valor="Ana"
#espacios entre nombre de variable
#cuenta bancaria = 54654654654

#SE PUEDE
nombre10="MAria"
#snake case o camel case
cuenta_bancaria_conjunta = 54654654
cuentaCorrienteCerrado = 4545748787

#casting o casteo,
numero1 = "100"
numero2 = 50
suma = int(numero1) +numero2
print("la suma es ",suma) 
#se puede hacer el casting o conversion de tipos de todas las variables
#str(aqui el valor), bool(aqui el valor),float(aqui va el valor),