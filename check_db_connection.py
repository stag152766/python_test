import mysql.connector
from fixture.db import DbFixture

# установка соединения
"""connection = mysql.connector.connect(host='127.0.0.1', database='addressbook', username='root', password='')

# чтение
try:
    cursor = connection.cursor()
    cursor.execute('select * from group_list')
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()
"""

db = DbFixture(host='127.0.0.1', database='addressbook', user='root', password='')

try:
    contacts = db.get_contact_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))
finally:
    db.destroy()
