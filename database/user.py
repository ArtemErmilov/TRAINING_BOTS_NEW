from .base import DataBase
from aiogram.types import Message


class User(DataBase):

    def __init__(self,data:dict ):
       
        if isinstance(data, dict):
            self.name = data['name']
            self.phone = data['phone']
            self.address= data['address']
            self.tg_id = data['tg_id']
            self.create()
        if isinstance(data,int):
            self.tg_id = data
        user = self.load(tg_id = self.tg_id)
        if (user):
            self.user_id, self.name, self.phone, self.address, self.tg_id = user
        else:
            self.user_id = None
            self.phone = None
            self.address= None
            self.tg_id = None
       

    # @staticmethod
    # def table():
    #     sql = '''CREATE TABLE IF NOT  EXISTS  users
    #                     (user_id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR,
    #                     surname VARCHAR, tg_id INTEGER)'''
    #     DataBase.execute(sql,commit= True)
    
    @staticmethod
    def table():
        """
        Создание таблицы.
        """
        sql = '''CREATE TABLE IF NOT  EXISTS  users
                        (user_id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR,
                        phone VARCHAR, address  VARCHAR, tg_id INTEGER)'''
        DataBase.execute(sql,commit= True)

    def load(self,**kwargs):
        """
        Выгрузка данных из базы.
        """
        sql = 'SELECT * FROM users WHERE '
        sql, parameters = self.extract_kwargs(sql,kwargs)
        user = self.execute(sql,parameters,fetchone=True)
        return user

    def create(self, **kwargs):
        """
        Изменение запись в БД.
        """
        sql = 'INSERT INTO users (name, phone, address, tg_id) VALUES (?,?,?,?) '

        self.execute(sql,(self.name, self.phone, self.address, self.tg_id),commit=True)


    def save(self,**kwargs):
        """
        Сохранение данных в базе.
        """
        sql = 'UPDATE users SET '
        sql, parameters = self.extract_kwargs(sql,self.__dict__,_and = False)
        sql = sql + f' WHERE user_id={self.user_id}'
        self.execute(sql,parameters, commit= True)
    
    def delete(self,**kwargs):
        """
        Удаление пользователя из БД.
        """
        sql = f'DELETE FROM users WHERE tg_id=?'
        self.execute(sql,(self.tg_id,), commit= True)
    
    def __str__(self):
        data_print = f'user_id = {self.user_id}, name = {self.name}, phone = {self.phone}, address = {self.address}, tg_id = {self.tg_id}'  
        return data_print
    
    
        