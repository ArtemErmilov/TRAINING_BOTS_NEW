import sqlite3


class DataBase:
    db_path = 'database/sqlite3.db'


    @staticmethod
    def execute(sql:str, parameters: tuple = tuple(),
                    fetchone = False, fetchall = False, commit = False):
        """
        Функция для манипуляции с базой данных.
        """
        connection = sqlite3.connect(DataBase.db_path) # Подключение к базе данных
        cursor = connection.cursor()#Соединение с базой данных
        data = None
        cursor.execute(sql,parameters)
        if commit:
            connection.commit() # Сохранение информации в базе данных.

        if fetchone: # В date записываем одно значение
            data = cursor.fetchone()

        if fetchall: # В date записываем все значения
            data = cursor.fetchall()

        connection.close() # Закрытие соединения с базой данных
        
        return data
    @staticmethod
    def extract_kwargs(sql: str, parameters: dict, _and: bool = True) -> tuple:
        sql +=(' AND ' if _and else ', ').join([f'{key} = ?' for key in parameters])

        return sql, tuple(parameters.values())