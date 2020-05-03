from model.contact import Contact
from random import randrange


def test_modify_contact_by_index(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='fnfnfnfnf', lastname='llnlnlnln'))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="New name")
    contact.id = old_contacts[index].id
    contact.lastname = old_contacts[0].lastname
    app.contact.open_contact_to_edit_by_index(contact, index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)