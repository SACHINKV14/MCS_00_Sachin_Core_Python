

import psycopg2
conn = psycopg2.connect(database="postgres",
                        user="postgres",
                        password="postgres123",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()

def some_db_fun():
    rec1 = "select * from new_employee "
    cursor.execute(rec1)
    datas = cursor.fetchall()
    for data in datas:
        conn.commit()
        cursor.close()
        conn.close()
        return data



