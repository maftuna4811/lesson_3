from connect_db import Database
import login


def register():
    print("Register")
    name = input("Name: ")
    surname = input("Surname: ")
    email = input("Email: ")
    password_1 = input("Password_1: ")
    password_2 = input("Reply Password: ")
    while password_1 != password_2:
        password_1 = input("Password_1: ")
        password_2 = input("Reply Password: ")
    contact_url = input("Contact url")
    query = ""

    query = f"""INSERT INTO users(name, surname, email, password, contact_url)
            VALUES('{name}', '{surname}', '{email}', '{password_1}', '{contact_url}')"""

    print(Database.connect(query, "insert"))
    return login.login()