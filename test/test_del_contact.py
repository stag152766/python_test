from model.contact import Contact
import random
import time

def test_delete_contact_by_id(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname='test', lastname='asfasf', homephone='asff'))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    time.sleep(2)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts



