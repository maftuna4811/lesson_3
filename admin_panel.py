from classes import Speciality, Course


def back(email, password):
    back = input("""
         0.back
            -->>>>""")
    if back == "0":
        return admin(email, password)
    else:
        print("Error")
        return course(email, password)


def course_insert(email, password):
    name = input("Name: ")
    tittle = input("Tittle: ")
    description = input("description: ")
    active_students = input("active_students: ")
    rating = input("rating: ")
    price = input("price: ")
    money_status = input("money_status: ")
    spec = Course(name,tittle, description, active_students, rating, price, money_status)
    print(spec.insert("course"))
    return back(email, password)


def course_list(email, password):
    data = Course.select("course")
    for i in data:
        print(f"""
               ID: {i[0]}
               Name: {i[1]}
               Tittle: {[2]}
               Description: {i[3]}
               Active student: {i[4]}
               Rating: {i[5]}
               Price: {i[6]}
               Money Status: {[7]}
                    """)
    return back(email, password)


def course_update(email, password):
    column_name = input("Column Name: ")
    old_data = input("Now data")
    new_data = input("New data")
    if column_name == "course":
        print(Course.update_id("course", column_name, old_data, new_data))
    else:
        print(Course.update("course", column_name, old_data, new_data))
    return course(email, password)


def course_delete(email, password):
    column_name = input("Column Name: ")
    data = input("Data: ")
    if column_name == "course_id":
        print(Course.delete_id("course", column_name, data))
    else:
        print(Course.delete_id("course", column_name, data))

    return course(email, password)


def course(email, password):
    services = input("""
             1.List
             2.Insert
             3.Update 
             4.Delete
             0.Back
                 -->>>> """)

    if services == "1":
        return course_list(email, password)
    elif services == "2":
        return course_insert(email, password)
    elif services == "3":
        return course_update(email, password)
    elif services == "4":
        return course_delete(email, password)
    elif services == "0":
        return admin(email, password)
    else:
        return course(email, password)


def speciality_insert(email, password):
    name = input("Name: ")
    spec = Speciality(name)
    print(spec.insert("speciality"))
    return back(email, password)


def speciality_list(email, password):
    data = Speciality.select("speciality")
    for i in data:
        print(f"""
               ID: {i[0]}
               Name: {i[1]}
                    """)
    return back(email, password)


def speciality_update(email, password):
    column_name = input("Column Name: ")
    old_data = input("Now data")
    new_data = input("New data")
    if column_name == "speciality":
        print(Speciality.update_id("speciality", column_name, old_data, new_data))
    else:
        print(Speciality.update("speciality", column_name, old_data, new_data))
    return speciality(email, password)


def speciality_delete(email, password):
    column_name = input("Column Name: ")
    data = input("Data: ")
    if column_name == "speciality_id":
        print(Speciality.delete_id("speciality", column_name, data))

    return speciality(email, password)


def speciality(email, password):
    services = input("""
             1.List
             2.Insert
             3.Update 
             4.Delete
             0.Back
                 -->>>> """)

    if services == "1":
        return speciality_list(email, password)
    elif services == "2":
        return speciality_insert(email, password)
    elif services == "3":
        return speciality_update(email, password)
    elif services == "4":
        return speciality_delete(email, password)
    elif services == "0":
        return admin(email, password)
    else:
        return speciality(email, password)


def admin(email, password):
    print("Admin page")
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
        return admin(email, password)