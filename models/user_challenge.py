from models.model import Model

class UserChallenge(Model):
    attrs = {
        'id_user' : 'Null',
        'id_challenge' : 'Null'
    }
    def __init__(self, attrs):
        super().__init__(table_name='user_challenge_', attrs=attrs)