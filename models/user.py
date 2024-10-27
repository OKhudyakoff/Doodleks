from models.model import Model

from models.user_challenge import UserChallenge

from auth import Auth


class User(Model):

    attrs = {
        'name' : 'Null',
        'login' : 'Null',
        'password' : 'Null',
        'position' : 'Null',
        'department' : 'Null',
        'create_date' : 'Null'
    }

    def __init__(self, attrs_=attrs):
        super().__init__(table_name='user_', attrs_=attrs_)

    def register_user(self, login='test', password='test'):
        '''
        регистрируем пользователя

        return: 
            возвращает False - когда регистрация провалена
            возвращает True - когда регистрация завершилась успешно
        '''
        rez = True

        if self.is_there_user_by_login(login):
            return False

        self.attrs['login'] = f"'{login}'"
        self.attrs['password'] = f"'{password}'"

        self.set_attrs(self.attrs)
        self.save()

        Auth.set_is_auth()
        Auth.set_attrs(self.get_attrs())
        Auth.set_user(self)

        return rez

    def auth_user(self, login='test', password='test'):
        '''
        авторизуем пользователя

        return: 
            возвращает
            (True, 1) - валидация успешна
            (False, 0) - такого логина нет
            (False, -1) - неверный пароль
            (False, -2) - другие случаи
        '''
        
        rez = self.validate_auth_user(login, password)
        if rez[0] == 1:
            self.attrs['id'] = rez[1]
            self.set_attrs(self.attrs)
            
            values = self.get_one()

            ats = dict(zip(self.attrs.keys(), *values))
            
            self.set_attrs(ats)
            Auth.set_is_auth()
            Auth.set_attrs(ats)
            Auth.set_user(self)

            return (True, rez[0])

        return (False, rez[0])

    def is_there_user_by_login(self, login):
        '''
        проверяет есть ли такой пользователь

        return: None
        '''
        query = f"""select id from user_ where login = '{login}'"""
        return self.db.executeQuery(query)

    def validate_auth_user(self, login, password):
        '''
        возвращает коды возврата

        return: 
            (1, id) - валидация успешна
            (0, None) - такого логина нет
            (-1, None) - неверный пароль
            (-2, None) - другие случаи
        '''

        query = f"""select id from user_ where login = '{login}'"""
        rez = self.db.executeQuery(query)
        if not rez:
            return (0, None)

        query = f"""select id from user_ where login = '{login}' and password <> '{password}'"""
        rez = self.db.executeQuery(query)
        if rez:
            return (-1, None)

        query = f"""select id from user_ where login = '{login}' and password = '{password}'"""
        rez = self.db.executeQuery(query)
        if rez:
            return (1, str(rez[0][0]))
        
        return (-2, None)

    def is_there_challenger(self, id_challenge):
        """
        метод проверяет есть ли такой вызов у пользователя

        return:
            True - такой вызов у пользователя есть
            False - такого вызовы у пользователя нет
        """
        query = f"""select 1 from user_challenge_ where id_user = {self.get_attrs()['id']} and id_challenge = {id_challenge}"""

        rez = self.db.executeQuery(query)

        if rez:
            return True
        return False

    def join_to_challenge(self, id_challenge):
        """
        метод добавляет новый вызов для пользователя
        """
        UserChallenge({
            "id_user" : self.get_attrs()['id'],
            "id_challenge" : id_challenge
        }).save()
