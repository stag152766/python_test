from model.contact import Contact


def test_modify_first_contact_firstname(app):
    app.contact.modify_contact(Contact(first="New name"))
