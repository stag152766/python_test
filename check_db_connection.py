from fixture.orm import OrmFixture


db = OrmFixture(host='127.0.0.1', database='addressbook', user='root', password='')

try:
    l = db.get_contact_list()
    for item in l:
        print(item)
    print(len(l))
finally:
    pass #db.destroy()
