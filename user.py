class User:
    def __init__(self, login, name, password):
        self.login = login
        self.name = name
        self.password = password
        self.is_login = True

current_user = User('admin', 'admin', 'admin')

def get_current_user():
    global current_user