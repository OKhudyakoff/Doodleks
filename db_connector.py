import firebird.driver as fdb

def connect_db():
    conn = fdb.connect(
        database='//192.168.1.136/User_log2/USER_LOG2.FBD', 
        user='sysdba',             
        password='456123',         
        charset='UTF8'            
    )

    print(conn)
    print(conn.cursor())
    return conn

# Функция для проверки логина и пароля
def check_user_credentials(login, password):
    conn = connect_db()  
    cur = conn.cursor()  

    try:
        cur.execute("SELECT password FROM user_log WHERE loggin = ?", (login,))
        result = cur.fetchone()
        
        print("DB Result:", result)  # Добавляем отладочное сообщение

        if result:
            db_password = result[0]
            print("DB Password:", db_password)  # Проверяем, какой пароль возвращает БД
            if db_password == password:
                return True
        return False
    finally:
        cur.close()
        conn.close()

print(connect_db())