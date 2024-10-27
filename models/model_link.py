from models.model import Model

from api.APIPostgres import APIPostgresException

class ModelLink(Model):

    def __init__(self, table_name, attrs_):
        super().__init__(table_name=table_name, attrs_=attrs_)

    def save(self):
        '''
        сохранение объекта
        '''
        try:
            
            columns = ', '.join(str(key) for key in self.get_attrs().keys())
            values = ', '.join(str(item) for item in self.get_attrs().values())

            query = f'''insert into {self._table_name} ({columns}) values ({values})'''

            self.db.executeQuery(query)

        except APIPostgresException as e:
            print(f'save [1]: error = ' + str(e.getMessage()))

    def remove(self):
        """
        удаление объекта
        """

        try:
            query = f'''delete from {self._table_name} where id_user = {self.get_attrs()['id_user']} and id_challenge = {self.get_attrs()['id_challenge']}'''

            self.db.executeQuery(query)

        except APIPostgresException as e:
            print(f'save [1]: error = ' + str(e.getMessage()))
