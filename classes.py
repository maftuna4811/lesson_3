from connect_db import Database


class Base:
    @staticmethod
    def select(table):
        query = f"SELECT * FROM {table}"
        return Database.connect(query, "select")

    @staticmethod
    def update_id(table, column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE {table} SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

    @staticmethod
    def update(table, column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE {table} SET {column_name} = '{new_data}' WHERE {column_name} = {old_data}"

    @staticmethod
    def delete_id(table, column_name, data):
        query = f"DELETE FROM {table} WHERE {column_name} = {data}"
        return Database.connect(query, "delete")

    @staticmethod
    def delete(table, column_name, data):
        query = f"DELETE FROM {table} WHERE {column_name} = '{data}'"
        return Database.connect(query, "delete")


class Speciality(Base):
    def __init__(self, name):
        self.name = name

    def insert(self, table):
        query = f"INSERT INTO {table}(name) VALUES('{self.name}')"
        return Database.connect(query, "insert")


class Course(Base):
    def __init__(self, name, tittle, description, active_student, rating, price, money_status):
        self.name = name
        self.tittle = tittle
        self.description = description
        self.active_student = active_student
        self.rating = rating
        self.price = price
        self.money_status = money_status

    def insert(self, table):
        query = (f"INSERT INTO {table}(name, tittle, description, active_student, rating, price, money_status)"
                 f" VALUES('{self.name}','{self.tittle}','{self.description}',{self.active_student},{self.rating},{self.price},{self.money_status})")
        return Database.connect(query, "insert")

