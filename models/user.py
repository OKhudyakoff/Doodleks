from models.model import Model

class User(Model):
    def __init__(self, attrs):
        super().__init__(table_name='user_', attrs=attrs)
