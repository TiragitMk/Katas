class CalculadoraPocket():

    def __init__(self):
        self.POSSIBLE_OPS = {"+", "-", "*", "/", "salir"}
        self.OPERACIONES = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y,
            "salir": None
            }
        self.num1 = None
        self.operation = None
        self.num2 = None
        self.result = None
    def __repr__(self):
        return f"{self.num1} {self.operation} {self.num2} = {self.result}"
    
    def get_numbers(self):
        
        while True:
            try:
                self.num1 = float(input("Dame un número: "))
                self.num2 = float(input("\nDame el otro número: "))
            except ValueError:
                print("\n", "Número inválido. Volvemos a empezar...".center(50), "\n")
                continue
            break
    
    def get_operator(self):
        while True:
            self.operation = input("\nElige un operador válido (+ - * /) o escribe 'salir': ").lower()
            if self.operation not in self.POSSIBLE_OPS:
                continue
            break
    
    def perform_operation(self):
        if self.OPERACIONES[self.operation]:
            self.result = self.OPERACIONES[self.operation](self.num1, self.num2)
        else:
            self.result = self.OPERACIONES[self.operation]
        
        return self.result
    
    def calc_loop(self):
        while True:
            self.get_numbers()
            self.get_operator()
            try:
                self.perform_operation()
            except ZeroDivisionError:
                print("\n¡Me has dado una división entre cero! Volvamos a empezar...\n")
                continue
            break

        if self.result:
            print("\n", self, "\t ¡Qué divertido, otra vez!")
    
    def whole_loop(self):
        print("\n", "¡Bienvenido a la calculadorita súper chulita!".center(70), "\n")
        while True:
            self.calc_loop()
            if not self.result:
                print("\n", "Entendido maestro :p".center(30))
                break
    
calculadorita = CalculadoraPocket()
calculadorita.whole_loop()