class DataAccessLayer:
    def __init__(self):
        self.database = {}

    def get_user(self, user_id):
        return self.database.get(user_id, None)

    def save_user(self, user_id, user_data):
        self.database[user_id] = user_data


# Logikschicht (Business Logic Layer)
class BusinessLogicLayer:
    def __init__(self, data_access_layer):
        self.data_access_layer = data_access_layer

    def create_user(self, user_id, user_name):
        if self.data_access_layer.get_user(user_id) is None:
            user_data = {'id': user_id, 'name': user_name}
            self.data_access_layer.save_user(user_id, user_data)
            return True
        else:
            return False

    def get_user_name(self, user_id):
        user = self.data_access_layer.get_user(user_id)
        if user:
            return user['name']
        else:
            return None


# Präsentationsschicht (Presentation Layer)
class PresentationLayer:
    def __init__(self, business_logic_layer):
        self.business_logic_layer = business_logic_layer

    def create_user_interface(self):
        user_id = input("Enter User ID: ")
        user_name = input("Enter User Name: ")
        if self.business_logic_layer.create_user(user_id, user_name):
            print(f"User '{user_name}' created successfully.")
        else:
            print(f"User ID '{user_id}' already exists.")

    def display_user_interface(self):
        user_id = input("Enter User ID to fetch: ")
        user_name = self.business_logic_layer.get_user_name(user_id)
        if user_name:
            print(f"User Name: {user_name}")
        else:
            print(f"No user found with ID '{user_id}'.")


# Hauptprogramm
if __name__ == "__main__":
    # Initialisierung der Schichten
    dal = DataAccessLayer()
    bll = BusinessLogicLayer(dal)
    pl = PresentationLayer(bll)

    # Benutzeroberfläche starten
    while True:
        print("\n1. Create User")
        print("2. Get User Name")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            pl.create_user_interface()
        elif choice == "2":
            pl.display_user_interface()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
