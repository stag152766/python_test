from fixture.orm import OrmFixture
from model.group import Group


db = OrmFixture(host='127.0.0.1', database='addressbook', user='root', password='')

try:
    l = db.get_contacts_not_in_group(Group(id='153'))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass #db.destroy()
