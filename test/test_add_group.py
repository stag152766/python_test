# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    # создается объект, который передает значения параметров в конструктор
    app.group.create(Group(name="asdfsaf", header="sdfsadf", footer="sadfsdaf"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
