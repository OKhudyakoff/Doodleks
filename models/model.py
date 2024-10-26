from api.APIPostgres import APIPostgres, APIPostgresException

from datetime import datetime

class Model:
    __is_save = False
    __table_name = None

    db = APIPostgres()

    # атрибуты модели
    __attrs = dict()

    def __init__(self, table_name, attrs):
        self.set_attrs(attrs)
        self.__table_name = table_name
        
    def save(self):
        '''
        сохранение объекта
        '''
        try:
            id = self.__get_id()
            self.__attrs['id'] = str(id)

            columns = ', '.join(key for key in self.__attrs.keys())
            values = ', '.join(item for item in self.__attrs.values())

            query = f'''insert into {self.__table_name} ({columns}) values ({values})'''

            self.db.executeQuery(query)

        except APIPostgresException as e:
            print(f'save [1]: {self.__table_name} error = ' + str(e.getMessage()))


    def update(self):
        '''
        изменение объекта
        '''
        try:
            key_values = ', '.join([
                f'{key}={value}' for key, value in self.__attrs.items() if key != 'id'
            ])

            print(key_values)

            query = f'''update {self.__table_name} set {key_values} where id = {self.__attrs['id']}'''

            self.db.executeQuery(query)
        except APIPostgresException as e:
            print(f'update [1]: {self.__table_name} error = ' + str(e.getMessage()))

    def remove(self):
        '''
        удаление объекта
        '''
        try:
            query = f'''delete from {self.__table_name} where id = {self.__attrs['id']}'''
            
            self.db.executeQuery(query)
        except APIPostgresException as e:
            print(f'remove [1]: {self.__table_name} error = ' + str(e.getMessage()))

    def get_one(self):
        '''
        получение одного объекта

        возвращает кортеж
        '''
        try:
            list_select = ', '.join([key for key in self.__attrs.keys()])

            query = f'''select {list_select} from {self.__table_name} where id = {self.__attrs['id']}'''

            return self.db.executeQuery(query)

        except APIPostgresException as e:
            print(f'save [1]: {self.__table_name} error = ' + str(e.getMessage()))
    
        return None

    def get_all(self):
        '''
        получение всех строк

        return: 
            возвращает список кортежей
        '''
        try:
            list_select = ', '.join([key for key in self.__attrs.keys()])

            query = f'''select {list_select} from {self.__table_name}'''

            return self.db.executeQuery(query)
        except APIPostgresException as e:
            print(f'save [1]: {self.__table_name} error = ' + str(e.getMessage()))

        return None


    def set_attrs(self, attrs):
        self.__attrs = attrs

    def get_attrs(self):
        return self.__attrs

    def __get_id(self):
        '''
        генерим след айди

        return: 
            возвращает макс айди + 1
        '''
        try:

            query = f'''select coalesce(max(id), 0) + 1 from {self.__table_name}'''

            return self.db.executeQuery(query)[0][0]
        except APIPostgresException as e:
            print(f'save [1]: {self.__table_name} error = ' + str(e.getMessage()))

        return None