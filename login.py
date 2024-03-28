from connect_db import Database
import admin_panel
import users_panel


def check(query, status):
    email = input("Email: ")
    password = input("Password: ")

    data = Database.connect(query, "select")
    print(data)
    for i in data:
        if i[3] == email and i[4] == password:
            if status == "1":
                return admin_panel.admin(email, password)
            else:
                return users_panel.users(email, password)

    else:
        print("Password or Email xato")
        return check(query, status)


def login():
    print("Login page")
    status = input("""
       1. erp.admin.najot_ta'lim.uz
       2. erp.users.najot_ta'lim.uz
              -->>>> """)

    if status == "1":
        query = """SELECT * FROM admin;"""
        return check(query, status)

    elif status == "2":
        query = """SELECT * FROM users"""
        return check(query, status)

    else:
        print("Error!!!")
        return login()
