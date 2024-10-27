import psycopg2

class APIPostgres:
    '''
    как пользоваться:
    
    from APIPostgres import APIPostgres

    db = APIPostgres()
    
    rez = db.executeQuery("create table if not exists test (a int);")

    print(rez)

    rez = db.executeQuery("insert into test values (1)")

    print(rez)

    rez = db.executeQuery("select * from test;")

    print(rez)
    '''

    __host = 'db'
    __port = 5432
    __database = 'postgres'
    __user = 'postgres'
    __password = 'postgres'

    __conn = None
    __cur = None

    __sql_user_create = '''create table if not exists user_ (
        id int primary key,
        name varchar(256),
        login varchar(128),
        password varchar(128),
        position varchar(128),
        department varchar(256),
        create_date date
    );'''

    __sql_challenge_create = '''create table if not exists challenge_(
        id int primary key,
        name varchar(256),
        start_date date,
        end_date date,
        description varchar(2048),
        organizer int references public.user_ on delete cascade,
        status varchar(128),
        amount_members int,
        prize int
    );'''

    __sql_link_user_challenge_create = '''create table if not exists user_challenge_(
        id_user int REFERENCES public.user_ on delete cascade,
        id_challenge int REFERENCES public.challenge_ on delete cascade
    );'''

    __sql_teams_create = '''create table if not exists teams_(
        id int primary key,
        team_id varchar(128),
        name varchar(128),
        members int,
        id_challenge int REFERENCES public.challenge_ on delete cascade
    );'''

    __sql_link_teams_user_create = '''create table if not exists teams_user_(
        id_team int REFERENCES public.teams_ on delete cascade,
        id_user int REFERENCES public.user_ on delete cascade
    );'''

    def __init__(self):
        if APIPostgres.__conn == None or APIPostgres.__conn == None:
            self.__create_cur()

    def __create_conn(self):
        if APIPostgres.__conn == None: 
            APIPostgres.__conn = psycopg2.connect(
                host = APIPostgres.__host,  # Если база на локальном сервере
                database = APIPostgres.__database,  # Название базы данных
                user = APIPostgres.__user,  # Пользователь
                password = APIPostgres.__password  # Пароль
            )

    def __create_cur(self):
        if APIPostgres.__cur == None:
            self.__create_conn()
            APIPostgres.__cur = APIPostgres.__conn.cursor()

    def executeQuery(self, query : str):
        '''
        выполняет запрос query

        может вызывать ошибки - нужно оборачивать в try catch

        return:
            возвращает результат запроса если select
        '''

        APIPostgres.__cur.execute(query)

        # commit изменений
        APIPostgres.__conn.commit()

        if 'select' in query.lower():
            return [row for row in APIPostgres.__cur]
            
        return None

    def init_tables(self):
        self.executeQuery(self.__sql_user_create)
        self.executeQuery(self.__sql_challenge_create)
        self.executeQuery(self.__sql_link_user_challenge_create)
        self.executeQuery(self.__sql_teams_create)
        self.executeQuery(self.__sql_link_teams_user_create)

class APIPostgresException(Exception):
    pass