# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(first="asd", middle="sdsfdf", last="ssfghfs"))
