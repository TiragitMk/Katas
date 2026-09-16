class User():

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def menu():
        pass

class Admin(User):

    def menu():
        """
        Permite obtener datos de la base de datos y modificarlos.
        """


class Client(User):

    def menu():
        """
        Permite obtener datos propios.
        """

class DatabaseAccess():

    def __init__(self):
        self.users = {"Admin":"Admin123"}

    def login(self):
        pass
    def register(self):
        pass
    def login_register_choice_menu(self):
        print("----Sistema de Autenticación----")
        print("1. Registrar nuevo usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        
        

    def obtain_anon_choice(self):
        while True:
            anon_user_choice = int(input("Elija 1, 2 o 3: "))
            if anon_user_choice not in {1, 2, 3}:
                print("Opción fuera de las posibles.")
                continue
            break
        return anon_user_choice

    def add_entry(self):
        pass
    def remove_entry(self):
        pass
    def modify_entry(self):
        pass