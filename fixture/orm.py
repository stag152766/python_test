from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact


class OrmFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')

    def __init__(self, host, database, user, password):
        self.db.bind('mysql', host=host, database=database, user=user, password=password)
        self.db.generate_mapping()
        sql_debug(True)

    def conver_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), header=group.header, footer=group.footer)
        return list(map(convert, groups))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname
                           )
        return list(map(convert, contacts))

    @db_session
    def get_group_list(self):
        return self.conver_groups_to_model(select(g for g in OrmFixture.ORMGroup))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in OrmFixture.ORMContact if c.deprecated is None))


