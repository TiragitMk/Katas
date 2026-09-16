#funciones o metodos
#funcion sin retorno
def saludar():
    print("Hola como estas")

#invocar metodo o funcion
saludar()

#funcion con retorno
def ver_numero():
    return 150

a = 10
suma = a + ver_numero()
print('La suma es: ',suma)

#funcion con parametros
def saludoCustom(saludo):
    print(saludo)

saludoCustom("Hello ")    


def getDatosCliente(nombre,apellido,email,telefono):
    datos_cliente = f"Nombre: {nombre}, Apellido: {apellido}, Email: {email}, Telefono:{telefono}"
    print(datos_cliente)

datos_cliente=True

getDatosCliente("Jorge","Perez","jp@gmail.com","64787124")


#como buena practica
def calcular_sumatoria(num1:float,num2:float)->float:
    print(num1+num2)
    suma= num1+num2
    return suma

calcular_sumatoria(41,61)

def calcularCuadrado(num:int)->int:
    return num*num

try:
    print('Respuesta: ', calcularCuadrado("True") )
except Exception as ex:
    print('deberias ingresar un numero',ex)

print("Fin de las pruebas")

#realizar un programa muestre segun la opcion +(suma), -(resta), *(Multiplicacion), /(Division)
#de dos numeros ingresados por teclado, nos pedira ingrese el primer numero, ingrese el segundo,
#ingrese la operacion, el programa debe para solo si al final de la operacion escribo la palabra salir

def mini_calculadora():

    POSSIBLE_OPS = {"+", "-", "*", "/", "salir"}
    OPERACIONES = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y,
            "salir": None
        }

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segúndo número: "))

    while True:
        operation = input("Ingrese el signo de la operación a realizar (+, -, * o /), o salir: ").lower()
        if operation in POSSIBLE_OPS:
            break
        print("Signo incorrecto. Pruebe otra vez.")

    result = OPERACIONES[operation](num1, num2)
    print(result)
    return result

def bucle_calculadora():
    while True:
        resultado = mini_calculadora()
        if resultado == None:
            break