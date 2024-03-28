from connect_db import Database


def create_table():
    course_table = """
        CREATE TABLE course(
          course_id SERIAL PRIMARY KEY,
          name VARCHAR(50),
          tittle VARCHAR(50),
          description TEXT,
          active_student INT,
          rating FLOAT,
          price NUMERIC,
          money_status NUMERIC,
          last_update DATE,
          create_date TIMESTAMP DEFAULT now());  
           """

    admin_table = """
        CREATE TABLE ADMIN(
           admin_id SERIAL PRIMARY KEY,
           name VARCHAR(50),
           surname VARCHAR(50),
           email VARCHAR(50),
           password VARCHAR(50),
           contact_url VARCHAR(50),
           last_updated DATE,
           create_date TIMESTAMP DEFAULT now()); """

    users_table = """
        CREATE TABLE users(
           users_id SERIAL PRIMARY KEY,
           name VARCHAR(50),
           surname VARCHAR(50),
           email VARCHAR(50),
           password VARCHAR(50),
           contact_url VARCHAR(50),
           last_updated DATE,
           create_date TIMESTAMP DEFAULT now()); """

    language_table = """
             CREATE TABLE language(
                 language_id SERIAL PRIMARY KEY,
                 name VARCHAR(50),
                 last_updated DATE,
                 create_date TIMESTAMP DEFAULT now()); """

    speciality_table = """
             CREATE TABLE speciality(
                 speciality_id SERIAL PRIMARY KEY,
                 name VARCHAR(50),
                 create_date TIMESTAMP DEFAULT now()); """

    speciality_course_table = """
             CREATE TABLE speciality_course(
                 speciality_course_id SERIAL PRIMARY KEY,
                 speciality_id INT REFERENCES speciality(speciality_id),
                 course_id INT REFERENCES course(course_id),
                 create_date TIMESTAMP DEFAULT now()); """

    lesson_status_table = """
             CREATE TABLE lesson_status(
                 lesson_status_id SERIAL PRIMARY KEY,
                 name VARCHAR(50),
                 create_date TIMESTAMP DEFAULT now()); """

    lesson_table = """
             CREATE TABLE lesson(
                 lesson_id SERIAL PRIMARY KEY,
                 name VARCHAR(50),
                 description TEXT,
                 admin_id INT REFERENCES admin(admin_id),
                 lesson_status_id INT REFERENCES lesson_status(lesson_status_id),
                 create_date TIMESTAMP DEFAULT now()); """

    category_table = """
                 CREATE TABLE category(
                     category_id SERIAL PRIMARY KEY,
                     tittle VARCHAR(50),
                     count_courses INT,
                     admin_id INT REFERENCES admin(admin_id),
                     users_id INT REFERENCES users(users_id),
                     course_id INT REFERENCES course(course_id),
                     create_date TIMESTAMP DEFAULT now()); """

    payment_table = """
                 CREATE TABLE payment(
                     payment_id SERIAL PRIMARY KEY,
                     course_id INT REFERENCES course(course_id),
                     users_id INT REFERENCES users(users_id),
                     amount NUMERIC,
                     card_number INT,
                     create_date TIMESTAMP DEFAULT now()); """

    data = {
        "course_table": course_table,
        "admin_table": admin_table,
        "users_table": users_table,
        "language_table": language_table,
        "speciality_table": speciality_table,
        "speciality_course_table": speciality_course_table,
        "lesson_status_table": lesson_status_table,
        "lesson_table": lesson_table,
        "category_table": category_table,
        "payment_table": payment_table
    }

    for i in data:
        print(f"{i} {Database.connect(data[i], "create")}")


if __name__ == "__main__":
    create_table()
