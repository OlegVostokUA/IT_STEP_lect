import sqlite3 as sq


def create_db():
    base = sq.connect('test_db2.db')
    cursor = base.cursor()
    sql_query = """CREATE TABLE IF NOT EXISTS Students(
                        name TEXT, 
                        s_name TEXT, 
                        age INT, 
                        date_s DATE, 
                        group_s TEXT, 
                        grants INT
                        )"""
    sql_query_2 = """CREATE TABLE IF NOT EXISTS Departments(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name_d TEXT,
                        phone TEXT)"""
    sql_query_3 = """CREATE TABLE IF NOT EXISTS Teachers(
                        name_t TEXT,
                        s_name_t TEXT,
                        dep_id INT,
                        FOREIGN KEY (dep_id) REFERENCES Departments (id))"""
    cursor.execute(sql_query)
    cursor.execute(sql_query_2)
    cursor.execute(sql_query_3)
#create_db()

def insert_data_db():
    base = sq.connect('test_db2.db')
    cursor = base.cursor()
    sql_query = """
    INSERT INTO Students(name, s_name, age, date_s, group_s, grants) VALUES
    ('Джеймс', 'Хант', 22, '2012-08-21', 'B', 1200),
    ('Ніккі', 'Лауда', 25, '2011-05-22', 'A', 1300),
    ('Артур', 'Сенна', 22, '2013-04-23', 'B', 1500),
    ('Міхаель', 'Шумахер', 25, '2016-07-24', 'A', 1800),
    ('Кен', 'Блок', 35, '2010-02-35', 'B', 2500),
    ('Коллін', 'Макрей', 21, '2017-10-26', 'A', 2200)
    """
    create_teachers = """
    INSERT INTO Teachers (name_t, s_name_t, dep_id) VALUES
    ('Алан', 'Тюрінг', 1),
    ('Ада', 'Лавлейс', 1),
    ('Лінус', 'Торвальдс', 2),
    ('Гвідо', 'ван Россум', 2),
    ('Джеймс', 'Гослінг', 2),
    ('Андерс', 'Хейлсберг', 5),
    ('Брем', 'Коен', 3),
    ('Брендан', 'Айк', 4),
    ('Лінус', 'Торвальдс', 6),
    ('Бярне', 'Страуструп', 6),
    ('Дональд', 'Кнут', 4),
    ('Денніс', 'Річі', 3);
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
    cursor.execute(sql_query)
    cursor.execute(create_teachers)
    cursor.execute(create_deps)
    base.commit() ##### !!!!!!!!!!!!!
#insert_data_db()



def select_data_db():

    #name = input('Enter name: ')
    #s_name = input('Enter second name: ')

    base = sq.connect('test_db2.db')
    cursor = base.cursor()
    # 'Джеймс', 'Хант'
    sql_query = """SELECT * FROM Students WHERE name == 'Джеймс' AND s_name == 'Хант'"""


    cursor.execute(sql_query)

    records = cursor.fetchall()
    for i in records:
        print(i)

select_data_db()
