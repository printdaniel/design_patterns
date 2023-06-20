# Modelo
class UserModel:
    def __init__(self):
        self.users = []

    def add_user(self, name):
        self.users.append(name)

    def get_users(self):
        return self.users


# Vista
class UserView:
    def show_users(self, users):
        print("Lista de usuarios:")
        for user in users:
            print(user)


# Controlador
class UserController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_user(self, name):
        self.model.add_user(name)

    def update_view(self):
        users = self.model.get_users()
        self.view.show_users(users)


# Uso del patrón MVC
model = UserModel()
view = UserView()
controller = UserController(model, view)

# Agregar usuarios al modelo
controller.add_user("Alice")
controller.add_user("Bob")
controller.add_user("Charlie")

# Actualizar la vista para mostrar los usuarios
controller.update_view()
