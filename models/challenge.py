from models.model import Model

from auth import Auth

class Challenge(Model):
    attrs = {
        'name' : 'Null',
        'start_date' : 'Null',
        'end_date' : 'Null',
        'description' : 'Null',
        'organizer' : 'Null',
        'status' : 'Null',
        'amount_members' : 'Null',
        'prize' : 1
    }
    def __init__(self, attrs_=attrs):
        super().__init__(table_name='challenge_', attrs_=attrs_)

    def get_auth_all(self):
        '''
        получение всех вызовов авторизованного пользователя

        return: 
            возвращает список кортежей
        '''
        try:
            list_select = ', '.join([str(key) for key in self.__attrs.keys()])

            query = f'''
                select {list_select} 
                from {self._table_name} 
                where organizer = {Auth.get_attrs()['id']} or id in (
                    select id_challenge 
                    from user_challenge_ 
                    where id_user = {Auth.get_attrs()['id']}
                )   
            '''

            return self.db.executeQuery(query)
        except APIPostgresException as e:
            print(f'save [1]: {self._table_name} error = ' + str(e.getMessage()))

        return None