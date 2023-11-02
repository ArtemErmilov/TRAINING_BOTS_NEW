# Создание базы данных

import sqlite3

PATH = 'sqlite3.db' # Путь к файлу относительный

# Для просмотра базы данных необходимо скачать DB browser for SQLite

def db_connect():
    connection = sqlite3.Connection(PATH) # Соединение с базой данных

    cursor = connection.cursor() # Соединение с базой данных, сущьность базы данных

    return cursor


def database_connect():
    """
    Создание базы данных
    """   

    connection = sqlite3.Connection(PATH) # Соединение с базой данных

    cursor = connection.cursor() # Соединение с базой данных, создание сущьность базы данных и подключение к ней

    # Создание таблицы и столбцов в ней

    cursor.execute('''CREATE TABLE IF NOT  EXISTS  user 
                        (id_user INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, 
                        surname TEXT, tg_id INTEGER)''')
    
    connection.commit()

def add_user(name,surname,tg_id):
    """
    Добавление пользователя в базу данных.
    """

    connection = sqlite3.Connection(PATH) # Соединение с базой данных

    cursor = connection.cursor() # Соединение с базой данных, создание сущность базы данных и подключение к ней

    sql = 'INSERT INTO user (name, surname,tg_id) VALUES(?,?,?)' # Добавление данных пользователя в базу
    cursor.execute(sql,(name, surname,tg_id))
    connection.commit() # Сохранение информации в базе данных.

def select_user(name:str):# tg_id:int
    """
    Вывод данных пользователя по запросу тг ID
    """
    connection = sqlite3.Connection(PATH) # Соединение с базой данных

    cursor = connection.cursor() # Соединение с базой данных, создание сущность базы данных и подключение к ней

    #sql = 'SELECT * FROM user WHERE tg_id=? and name=?' # Создание запроса для вывода данных из БД по телеграм id

    sql = 'SELECT * FROM user WHERE name=?' # Создание запроса для вывода данных из БД по телеграм id

    #user =  cursor.execute(sql,(tg_id,name,)).fetchmany() # запись данных полученных из базы данных

    #user =  cursor.execute(sql,(tg_id,name)).fetchall() # запись данных полученных из базы данных

    user =  cursor.execute(sql,(name,)).fetchall() # запись данных полученных из базы данных

    return user # Вывод данных по пользователю.

def update_user(tg_id:int, new_name:str):# tg_id:int
    """
    Обновление данных пользователя.
    """
    connection = sqlite3.Connection(PATH) # Соединение с базой данных

    cursor = connection.cursor() # Соединение с базой данных, создание сущность базы данных и подключение к ней
    sql = 'UPDATE user SET name=? WHERE tg_id=?' # Создание запроса для изменение имени по tg_id
    cursor.execute(sql,(new_name,tg_id)) # запись данных полученных из базы данных
    connection.commit()


def delete_user(tg_id:int):# tg_id:int
    """
    Удаление пользователя из базы данных.
    """
    connection = sqlite3.Connection(PATH) # Соединение с базой данных

    cursor = connection.cursor() # Соединение с базой данных, создание сущность базы данных и подключение к ней
    sql = 'DELETE FROM user WHERE tg_id=?' # Создание запроса для удаления данных по  tg_id
    cursor.execute(sql,(tg_id,)) # запись данных полученных из базы данных
    connection.commit()

    """
    Типы данных в SQlit
    Python      SQLlit

    None        NULL
    int         INTEGER
    float       REAL
    str         TEXT
    bytes       BLOB        
    """