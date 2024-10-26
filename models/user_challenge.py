from models.model_link import ModelLink

class UserChallenge(ModelLink):
    attrs = {
        'id_user' : 'Null',
        'id_challenge' : 'Null'
    }
    def __init__(self, attrs_=attrs):
        super().__init__(table_name='user_challenge_', attrs_=attrs_)