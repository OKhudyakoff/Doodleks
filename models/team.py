from models.model import Model

class Team(Model):
    attrs = {
        'team_id' : 'Null',
        'name' : 'Null',
        'members' : 'Null'
    }
    def __init__(self, attrs):
        super().__init__(table_name='teams_', attrs=attrs)