from model.contact import Contact
from model.group import Group
from random import randrange, choice


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname='Peter'))
    old_contacts = db.get_contact_list()
    contact = choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_delete_contact_from_group(app, orm):
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

    groups = orm.get_group_list()
    contacts = [c.id for c in orm.get_contact_list()]
    contact_index = choice(contacts)
    group_index = randrange(len(groups))
    delete_from_group = groups[group_index].name
    old_contacts_in_group = orm.get_contact_in_group(Group(id=groups[group_index].id))
    if len(old_contacts_in_group) == 0:
        app.contact.add_contact_to_group_by_index(contact_index, delete_from_group)
        contact_index = 0
    app.contact.delete_contact_from_group_by_index(contact_index, delete_from_group)
    new_contacts_in_group = orm.get_contact_in_group(Group(id=groups[group_index].id))
    assert str(contact_index) not in str(new_contacts_in_group)
