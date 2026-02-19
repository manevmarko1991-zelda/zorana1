class UserModel:
    def __init__(self):
        self.user_data = {"name": "Max", "age": 30}

    def get_user_data(self):
        return self.user_data

    def set_user_data(self, name, age):
        self.user_data["name"] = name
        self.user_data["age"] = age

class UserView:
    def show_user(self, user_data):
        print(f"Name: {user_data['name']}")
        print(f"Age: {user_data['age']}")

    def get_user_input(self):
        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        return name, age

class UserController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_user(self):
        name, age = self.view.get_user_input()
        self.model.set_user_data(name, age)
        self.view.show_user(self.model.get_user_data())

#Hauptprogramm
if __name__ == "__main__":
    model = UserModel()
    view = UserView()
    controller = UserController(model, view)

    # Initiale Anzeige der Benutzerdaten
    view.show_user(model.get_user_data())

    # Benutzerdaten aktualisieren
    controller.update_user()