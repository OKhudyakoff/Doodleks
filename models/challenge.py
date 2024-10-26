from models.model import Model

class Challenge(Model):
    attrs = {
        'name' : 'Null',
        'start_date' : 'Null',
        'end_date' : 'Null',
        'description' : 'Null',
        'organizer' : 'Null',
        'status' : 'Null'
    }
    def __init__(self, attrs):
        super().__init__(table_name='challenge_', attrs=attrs)