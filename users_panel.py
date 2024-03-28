from connect_db import Database


def course(email, password):
    query = "SELECT * FROM course"
    data = Database.connect(query, "select")
    for i in data:
        print(f"""
           ID: {i[0]}
           Name: {i[1]}
           Tittle: {i[2]}
           Description: {i[3]}
           Active student: {i[4]}
           Rating: {i[5]}
           Price: {i[6]}
           Money status: {[7]}
                """)
    back = input("""
      0.back
         -->>>>""")
    if back == "0":
        return users(email, password)
    else:
        print("Error")
        return course(email, password)


def speciality(email, password):
    query = "SELECT * FROM speciality"
    data = Database.connect(query, "select")
    for i in data:
        print(f"""
           ID: {i[0]}
           Name: {i[1]}
                """)
    back = input("""
      0.back
         -->>>>""")
    if back == "0":
        return users(email, password)
    else:
        print("Error")
        return speciality(email, password)


def users(email, password):
    print("Users page")
    services = input("""
        1.Speciality
        2.Course
        3.Profile
        4.Log out
            -->>>> """)
    if services == "1":
        return speciality(email, password)
    elif services == "2":
        return course(email, password)
    elif services == "3":
        pass
    elif services == "4":
        pass

    else:
        return users(email, password)