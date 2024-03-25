import sqlite3 as sq

def database_create():

    base = sq.connect('testDB2.db')
    cursor = base.cursor()
    sql_query = '''CREATE TABLE IF NOT EXISTS Students(
        name TEXT,
        s_name TEXT,
        age INT,
        date_s DATE,
        group_n TEXT,
        grants INT)'''

    sql_query2 = '''CREATE TABLE IF NOT EXISTS Departments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_d TEXT,
        phone TEXT)'''

    sql_query3 = '''CREATE TABLE IF NOT EXISTS Teachers(
        name_t TEXT,
        s_name_t TEXT,
        date_s_t DATE,
        dep_id INT,
        FOREIGN KEY (dep_id) REFERENCES Departments (id))'''

    cursor.execute(sql_query)
    cursor.execute(sql_query2)
    cursor.execute(sql_query3)


    base.commit()
    print('tables create')

database_create()

def database_insert():

    base = sq.connect('testDB2.db')
    cursor = base.cursor()

    create_users = """
    INSERT INTO Students (name, s_name, age, date_s, group_n, grants) VALUES
    ('Джеймс', 'Хант', 28, '2002-08-21', 'B', 1200),
    ('Ніккі', 'Лауда', 25, '2001-05-22', 'A', 1300),
    ('Артур', 'Сенна', 22, '2003-04-23', 'B', 1500),
    ('Міхаель', 'Шумахер', 25, '2006-07-24', 'A', 1800),
    ('Кен', 'Блок', 35, '2000-02-35', 'B', 2500),
    ('Коллін', 'Макрей', 21, '2007-10-26', 'A', 2200);
    """

    create_teachers = """
    INSERT INTO Teachers (name_t, s_name_t, date_s_t, dep_id) VALUES
    ('Алан', 'Тюрінг', '1992-08-21', 1),
    ('Ада', 'Лавлейс', '1985-05-22', 1),
    ('Лінус', 'Торвальдс', '1989-04-23', 2),
    ('Гвідо', 'ван Россум', '1992-07-24', 2),
    ('Джеймс', 'Гослінг', '1992-07-24', 2),
    ('Андерс', 'Хейлсберг', '1992-07-24', 5),
    ('Брем', 'Коен', '1992-07-24', 3),
    ('Брендан', 'Айк', '1992-07-24', 4),
    ('Лінус', 'Торвальдс', '1989-04-23', 6),
    ('Бярне', 'Страуструп', '1982-02-35', 6),
    ('Дональд', 'Кнут', '1982-02-35', 4),
    ('Денніс', 'Річі', '1975-10-26', 3);
    """

    create_deps = """
    INSERT INTO Departments(name_d, phone) VALUES
    ('Cybersecurity', '2205-800'),
    ('Python', '1236-500'),
    ('Java', '3584-100'),
    ('Frontend', '4545-700'),
    ('C++', '4545-700'),
    ('DevOps', '4545-700');
    """

    cursor.execute(create_users)
    cursor.execute(create_teachers)
    cursor.execute(create_deps)

    base.commit() #####!!!!!

#database_insert()


#######################

#'Джеймс', 'Хант'

#i_name = 'Джеймс'

#i_name = 'Джеймс'/*'

i_s_name = 'Хант'


def database_select6():

    name = input() #Джеймс'/*  // Джеймс' OR 1==1/*  <<< SQL injection
    s_name = input()
    #name = i_name
    #s_name = i_s_name

    val = name# + s_name

    base = sq.connect('testDB2.db')
    cursor = base.cursor()

    select_users = f"""SELECT * FROM Students WHERE name == '{name}' AND s_name == '{s_name}'"""
    #print(select_users)

    #select_users = """SELECT * FROM Students WHERE name == ?""" # AND s_name == ?


    cursor.execute(select_users)

    records = cursor.fetchall()

    for i in records:
        print(i)

database_select6()
