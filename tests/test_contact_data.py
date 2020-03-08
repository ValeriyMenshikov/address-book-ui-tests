from model.contact import Contact
from random import randrange
import re


def test_data_on_contact_page(app):
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
    contact_from_homepage = app.contact.get_contact_list()[index]
    contact_from_editpage = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_homepage.firstname == contact_from_editpage.firstname
    assert contact_from_homepage.lastname == contact_from_editpage.lastname
    assert contact_from_homepage.address == contact_from_editpage.address
    assert contact_from_homepage.address == contact_from_editpage.address
    assert clear(contact_from_homepage.all_phones_from_home_page) == merge_phones_like_on_homepage(contact_from_editpage)
    assert clear(contact_from_homepage.all_emails_from_home_page) == merge_emails_like_on_homepage(contact_from_editpage)


def test_data_on_contact_page_and_db(app, db):
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
    contacts_from_homepage = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()
    assert contacts_from_homepage == contacts_from_db


def merge_phones_like_on_homepage(contact):
    return '\n'.join(filter(lambda x: x != '',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone,
                                        contact.secondaryphone]))))


def merge_emails_like_on_homepage(contact):
    return '\n'.join(filter(lambda x: x != '',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.mail, contact.email2, contact.email3]))))


def clear(s):
    return re.sub(r'[ ()-/.]', '', s)
