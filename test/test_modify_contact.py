from model.contact import Contact


def test_modify_first_contact_firstname(app):
    app.session.login('admin', 'secret')
    app.contact.modify_contact(Contact(first="New name"))
    app.session.logout()