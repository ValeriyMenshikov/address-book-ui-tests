from model.contact import Contact
from random import randrange


def test_edit_some_contact(app):
    if app.contact.count() == 0:
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
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="fdsdf", middlename="asdffssdasd", lastname="213123f",
                      nickname="12fdvsdf", byear="2000", aday="11",
                      amonth="February", ayear="2001", address2="asdawe21e2", secondaryphone="123123dasf",
                      notes="sfdsd")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
