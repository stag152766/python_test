from model.contact import Contact

#
# def test_modify_first_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(first="New name")
#     contact.id = old_contacts[0].id
#     app.contact.modify_contact(contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#     old_contacts[0] = contact
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)