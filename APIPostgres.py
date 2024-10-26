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

    __host = 'desktop-5h7tutm'
    __port = 5432
    __database = 'postgres'
    __user = 'vizov'
    __password = 'vizov'

    __conn = None
    __cur = None

    

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

        print(APIPostgres.__conn)

    def __create_cur(self):
        if APIPostgres.__cur == None:
            self.__create_conn()
            APIPostgres.__cur = APIPostgres.__conn.cursor()

        print(APIPostgres.__cur)

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

    def init_tables():
        pass


class APIPostgresException(Exception):
    pass