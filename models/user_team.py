from models.model_link import ModelLink

class UserTeam(ModelLink):
    attrs = {
        'id_team' : 'Null',
        'id_user' : 'Null'
    }
    def __init__(self, attrs_=attrs):
        super().__init__(table_name='teams_user_', attrs=attrs_)