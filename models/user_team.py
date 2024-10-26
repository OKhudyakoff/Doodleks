from models.model import Model

class UserTeam(Model):
    attrs = {
        'id_team' : 'Null',
        'id_user' : 'Null'
    }
    def __init__(self, attrs):
        super().__init__(table_name='teams_user_', attrs=attrs)