# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
from random import randrange


def test_add_contact(app, db, data_contacts, check_ui):
    contact = data_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


def test_add_contact_to_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        contact = Contact(firstname='Степан ', middlename='Иванович ',
                          lastname='Петров ', nickname='Иваныч ',
                          title='title', company='ОАО ОмПО Радиозавод им. А.С.Попова(РЕЛЕРО) ',
                          address='г. Омск ул.Ленина д.1 кв. 99', homephone=r'+79509999999',
                          mobilephone=r'+79509999999', workphone=r'+79509999999',
                          faxphone=r'+79509999999', mail='email1@mail.ru',
                          email2='email2@mail.ru', email3='email3@mail.ru',
                          homepage='www.homepage.ru',
                          bday="1", bmonth="January", byear="1999",
                          aday="11", amonth="February", ayear="2000",
                          address2='г. Омск ул. Маршала Жукова д.№ 79 кв.№ 105 ', secondaryphone='84952000600')
        app.contact.create(contact)
    if len(orm.get_group_list()) == 0:
        group = Group(name="1111", header="111", footer="111")
        app.group.create(group)

    contacts = orm.get_contact_list()
    groups = orm.get_group_list()
    contact_index = randrange(len(contacts))
    group_index = randrange(len(groups))
    group_for_add = groups[group_index].name
    app.contact.add_contact_to_group_by_index(contact_index, group_for_add)
    new_contacts_in_group = orm.get_contact_in_group(Group(id=groups[group_index].id))
    assert contacts[contact_index].id in str(new_contacts_in_group)
