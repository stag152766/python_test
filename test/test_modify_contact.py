from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='fnfnfnfnf', lastname='llnlnlnln'))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="New name")
    contact.id = old_contacts[0].id
    contact.lastname = old_contacts[0].lastname
    app.contact.modify_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)