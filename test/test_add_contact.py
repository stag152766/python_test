# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first="asd", middle="sdsfdf", last="ssfghfs"))
    app.session.logout()
