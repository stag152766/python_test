import mysql.connector

# установка соединения
connection = mysql.connector.connect(host='127.0.0.1', database='addressbook', username='root', password='')

# чтение
try:
    cursor = connection.cursor()
    cursor.execute('select * from group_list')
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()
