# -*- coding: utf-8 -*-
from model.contact import Contact



def test_add_contact(app, db,json_contact):
    contact = json_contact
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) + 1 == len(db.get_contact_list())
    old_contacts.append(contact)
    assert old_contacts == new_contacts