import sqlite3
from parse_class_1 import *

# Создание таблицы
def create_tables_in_db():
    conn = sqlite3.connect("olympiad.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE Olympiad
                      (olymp_id int,
                      name text,
                      description text,
                      status text,
                      class_start int,
                      class_stop int,
                      id_sub int)
                    """)
    cursor.execute("""CREATE TABLE Date
                      (olymp_id int,
                      date_start text,
                      date_stop text,
                      name text)
                    """)
    cursor.execute("""CREATE TABLE User
                      (user_id int,
                      email text)
                      """)
    cursor.execute("""CREATE TABLE User_Subject
                      (user_id int,
                      subject text)
                      """)
    cursor.execute("""CREATE TABLE User_Class
                      (user_id int,
                      class int)
                      """)
    cursor.close()
def inserting(k):
    conn = sqlite3.connect("olympiad.db")
    cursor = conn.cursor()
    a = parse_sub(k)
    ##@%В52а#@н$я л$о%@х
    print(a)
    for i in range(len(a)):
        ##ID
        execute1 = '''insert into Olympiad(olymp_id,name,description,status,class_start,class_stop,id_sub) values(?,?,?,?,?,?,?)'''
        cursor.execute(execute1, (
        a[i].id,
        a[i].name,
        a[i].desc,
        a[i].status,
        a[i].class_start,
        a[i].class_stop,
        a[i].id_sub
        ))
        if len(a[i].date) != 0:
            for k in range(len(a[i].date)):
                execute2 = '''insert into Date(olymp_id,date_start,date_stop,name) values(?,?,?,?)'''
                cursor.execute(execute2, (
                a[i].id,
                a[i].date[k].get('start'),
                a[i].date[k].get('stop'),
                a[i].date[k].get('name')
                ))
        ##НАДО!
        #a = parse_sub(k)
    conn.commit()
    ##results
    ##ID
    """cursor.execute("SELECT olymp_id FROM Olympiad ORDER BY olymp_id")
    results = cursor.fetchall()
    print(results)
    ##name
    cursor.execute("SELECT name FROM Olympiad ORDER BY name")
    results = cursor.fetchall()
    print(results)
    ##description
    cursor.execute("SELECT description FROM Olympiad ORDER BY description")
    results = cursor.fetchall()
    print(results)
    ##status
    cursor.execute("SELECT status FROM Olympiad ORDER BY status")
    results = cursor.fetchall()
    print(results)
    ##class_start
    cursor.execute("SELECT class_start FROM Olympiad ORDER BY class_start")
    results = cursor.fetchall()
    print(results)
    ##class_stop
    cursor.execute("SELECT class_stop FROM Olympiad ORDER BY class_stop")
    results = cursor.fetchall()
    print(results)"""
    ##date_start
    #cursor.execute("SELECT date_start FROM Date ORDER BY date_start")
    #results = cursor.fetchall()
    #print(results)
    ##date_stop
    #cursor.execute("SELECT date_stop FROM Date ORDER BY date_stop")
    #results = cursor.fetchall()
    #print(results)
"""create_tables_in_db()
i = 1
call = is_sub_exist(i)
while call != False:
    inserting(i)
    i += 1
    call = is_sub_exist(i)"""

def reading():
    conn = sqlite3.connect("olympiad.db")
    cursor = conn.cursor()
    cursor.execute("SELECT olymp_id FROM Olympiad ORDER BY olymp_id")
    id = cursor.fetchall()
    print(id)
    ##name
    cursor.execute("SELECT name FROM Olympiad ORDER BY name")
    name = cursor.fetchall()
    print(name)
    ##description
    cursor.execute("SELECT description FROM Olympiad ORDER BY description")
    description = cursor.fetchall()
    print(description)
    ##status
    cursor.execute("SELECT status FROM Olympiad ORDER BY status")
    status = cursor.fetchall()
    print(status)
    ##class_start
    cursor.execute("SELECT class_start FROM Olympiad ORDER BY class_start")
    class_start = cursor.fetchall()
    print(class_start)
    ##class_stop
    cursor.execute("SELECT class_stop FROM Olympiad ORDER BY class_stop")
    class_stop = cursor.fetchall()
    print(class_stop)

reading()
