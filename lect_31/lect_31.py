import sqlite3 as sq


def create_db():
    base = sq.connect('test_db.db')
    cursor = base.cursor()
    sql_query = """CREATE TABLE IF NOT EXISTS Students(
                        name TEXT, 
                        s_name TEXT, 
                        age INT, 
                        date_s DATE, 
                        group_s TEXT, 
                        grants INT
                        )"""
    cursor.execute(sql_query)
#create_db()


def insert_data_db():
    base = sq.connect('test_db.db')
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
    cursor.execute(sql_query)
    base.commit() ##### !!!!!!!!!!!!!
#insert_data_db()


def select_data_db():
    base = sq.connect('test_db.db')
    cursor = base.cursor()

    sql_query = """SELECT * FROM Students LIMIT 3"""
    #sql_query = """SELECT name FROM Students WHERE group_s == 'B'"""
    cursor.execute(sql_query)

    records = cursor.fetchall()
    for i in records:
        print(i)


select_data_db()
