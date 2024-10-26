from models.model import Model

class Challenge(Model):
    attrs = {
        'name' : 'Null',
        'start_date' : 'Null',
        'end_date' : 'Null',
        'description' : 'Null',
        'organizer' : 'Null',
        'status' : 'Null',
        'amount_members' : 'Null'
    }
    def __init__(self, attrs_=attrs):
        super().__init__(table_name='challenge_', attrs_=attrs_)