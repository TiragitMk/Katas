class CalculadoraPocket():

    def __init__(self):
        self.OPERACIONES = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y,
            "salir": None
            }
        self.POSSIBILITIES = set(self.OPERACIONES.keys())
        self.num1 = None
        self.operation = None
        self.num2 = None
        self.result = None
    def __repr__(self):
        return f"{self.num1} {self.operation} {self.num2} = {self.result}"
    
    def set_numbers(self):
        """
        Toma el input del usuario y asigna a atributos num. Return None.
        """
        while True:
            try:
                self.num1 = float(input("Dame un número: "))
                self.num2 = float(input("\nDame el otro número: "))
            except ValueError:
                print("\n", "Número inválido. Volvemos a empezar...".center(50), "\n")
                continue
            break
    
    def set_operator(self):
        """
        Toma el input del usuario y asigna a atributo operation.
        operation se usa como clave en un diccionario, valor siendo la función
        que se aplica a ambos num.
        """
        while True:
            self.operation = input("\nElige un operador válido (+ - * /) o escribe 'salir': ").lower()
            if self.operation not in self.POSSIBILITIES:
                continue
            break
    
    def perform_operation(self, operator, n1, n2):
        """
        Aplica operation sobre num1 y num2. Devuelve el resultado.
        Mira en un diccionario de dispatch, es un aplicador básico con opciones limitadas.
        """
        if self.OPERACIONES[operator]:
            self.result = self.OPERACIONES[operator](n1, n2)
        else:
            self.result = self.OPERACIONES[operator]
        
        return self.result
    
    def calc_loop(self):
        """
        1 iteración de cálculo + resultados. Consigue los números, el operador, calcula e imprime.
        """
        while True:
            self.set_numbers()
            self.set_operator()
            try:
                self.perform_operation(self.operation, self.num1, self.num2)
            except ZeroDivisionError:
                print("\n¡Me has dado una división entre cero! Volvamos a empezar...\n")
                continue
            break

        if self.result:
            print("\n", self, "\t ¡Qué divertido, otra vez!", "\n"*2)
    
    def whole_loop(self):
        """
        Realiza un bucle de calc_loop hasta que se salga manualmente.
        """
        print("\n", "¡Bienvenido a la calculadorita súper chulita!".center(70), "\n")
        while True:
            self.calc_loop()
            if not self.result:
                print("\n", "Entendido maestro :p".center(30))
                break

if __name__ == "__main__":
    calculadorita = CalculadoraPocket()
    calculadorita.whole_loop()