from models.model import Model

class Team(Model):
    attrs = {
        'team_id' : 'Null',
        'name' : 'Null',
        'members' : 'Null',
        'id_challenge' : 'Null'
    }
    def __init__(self, attrs_=attrs):
        super().__init__(table_name='teams_', attrs_=attrs_)