from model.group import Group
import random


def test_add_contact_to_group(app, orm, json_contact):
    group_list = orm.get_group_list()
    if len(group_list) == 0:
        app.group.create(Group(name='n_test1'))
        group_list = orm.get_group_list()
    contact = json_contact
    group = random.choice(group_list)
    old_contacts_in_group = orm.get_contacts_from_group(group)
    app.contact.create(contact, group)
    new_contacts_in_group = orm.get_contacts_from_group(group)
    old_contacts_in_group.append(contact)
    assert sorted(old_contacts_in_group, key=Group.id_or_max) == sorted(new_contacts_in_group, key=Group.id_or_max)
