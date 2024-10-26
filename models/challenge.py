from models.model import Model

class Challenge(Model):
    def __init__(self, attrs):
        super().__init__(table_name='challenge_', attrs=attrs)