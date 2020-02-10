# -*- coding: utf-8 -*-
from model.contact import Contact

import pytest
import random
import string


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + ' ' * 10
    return ''.join([random.choice(symbols) for _ in range(random.randrange(maxlen))])


max_tests_for_field = 1
test_data = [Contact(firstname='firstname', middlename='middlename',
                     lastname='lastname', nickname='nickname',
                     title='title', company='company',
                     address='address', homephone=r'+79509999999',
                     mobilephone=r'+79509999999', workphone=r'+79509999999',
                     faxphone=r'+79509999999', mail='mail',
                     email2='email2', email3='email3',
                     homepage='homepage',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='address2', secondaryphone='secondaryphone')] + \
            [Contact(firstname=random_string(20), middlename='middlename',
                     lastname='lastname', nickname='nickname',
                     title='title', company='company',
                     address='address', homephone=r'+79509999999',
                     mobilephone=r'+79509999999', workphone=r'+79509999999',
                     faxphone=r'+79509999999', mail='mail',
                     email2='email2', email3='email3',
                     homepage='homepage',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='address2', secondaryphone='secondaryphone') for _ in range(max_tests_for_field)] + \
            [Contact(firstname='firstname', middlename=random_string(20),
                     lastname='lastname', nickname='nickname',
                     title='title', company='company',
                     address='address', homephone=r'+79509999999',
                     mobilephone=r'+79509999999', workphone=r'+79509999999',
                     faxphone=r'+79509999999', mail='mail',
                     email2='email2', email3='email3',
                     homepage='homepage',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='address2', secondaryphone='secondaryphone') for _ in range(max_tests_for_field)] + \
            [Contact(firstname='firstname', middlename='middlename',
                     lastname=random_string(20), nickname='nickname',
                     title='title', company='company',
                     address='address', homephone=r'+79509999999',
                     mobilephone=r'+79509999999', workphone=r'+79509999999',
                     faxphone=r'+79509999999', mail='mail',
                     email2='email2', email3='email3',
                     homepage='homepage',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='address2', secondaryphone='secondaryphone') for _ in range(max_tests_for_field)] + \
            [Contact(firstname='firstname', middlename='middlename',
                     lastname='lastname', nickname=random_string(20),
                     title='title', company='company',
                     address='address', homephone=r'+79509999999',
                     mobilephone=r'+79509999999', workphone=r'+79509999999',
                     faxphone=r'+79509999999', mail='mail',
                     email2='email2', email3='email3',
                     homepage='homepage',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='address2', secondaryphone='secondaryphone') for _ in range(max_tests_for_field)] + \
            [Contact(firstname='firstname', middlename='middlename',
                     lastname='lastname', nickname='nickname',
                     title=random_string(20), company='company',
                     address='address', homephone=r'+79509999999',
                     mobilephone=r'+79509999999', workphone=r'+79509999999',
                     faxphone=r'+79509999999', mail='mail',
                     email2='email2', email3='email3',
                     homepage='homepage',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='address2', secondaryphone='secondaryphone') for _ in range(max_tests_for_field)] + \
            [Contact(firstname='firstname', middlename='middlename',
                     lastname='lastname', nickname='nickname',
                     title='title', company=random_string(20),
                     address='address', homephone=r'+79509999999',
                     mobilephone=r'+79509999999', workphone=r'+79509999999',
                     faxphone=r'+79509999999', mail='mail',
                     email2='email2', email3='email3',
                     homepage='homepage',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='address2', secondaryphone='secondaryphone') for _ in range(max_tests_for_field)] + \
            [Contact(firstname='firstname', middlename='middlename',
                     lastname='lastname', nickname='nickname',
                     title='title', company='company',
                     address=random_string(20), homephone=r'+79509999999',
                     mobilephone=r'+79509999999', workphone=r'+79509999999',
                     faxphone=r'+79509999999', mail='mail',
                     email2='email2', email3='email3',
                     homepage='homepage',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='address2', secondaryphone='secondaryphone') for _ in range(max_tests_for_field)] + \
            [Contact(firstname='firstname', middlename='middlename',
                     lastname='lastname', nickname='nickname',
                     title='title', company='company',
                     address='address', homephone=random_string(20),
                     mobilephone=r'+79509999999', workphone=r'+79509999999',
                     faxphone=r'+79509999999', mail='mail',
                     email2='email2', email3='email3',
                     homepage='homepage',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='address2', secondaryphone='secondaryphone') for _ in range(max_tests_for_field)] + \
            [Contact(firstname='firstname', middlename='middlename',
                     lastname='lastname', nickname='nickname',
                     title='title', company='company',
                     address='address', homephone=r'+79509999999',
                     mobilephone=random_string(20), workphone=r'+79509999999',
                     faxphone=r'+79509999999', mail='mail',
                     email2='email2', email3='email3',
                     homepage='homepage',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='address2', secondaryphone='secondaryphone') for _ in range(max_tests_for_field)] + \
            [Contact(firstname='firstname', middlename='middlename',
                     lastname='lastname', nickname='nickname',
                     title='title', company='company',
                     address='address', homephone=r'+79509999999',
                     mobilephone=r'+79509999999', workphone=random_string(20),
                     faxphone=r'+79509999999', mail='mail',
                     email2='email2', email3='email3',
                     homepage='homepage',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='address2', secondaryphone='secondaryphone') for _ in range(max_tests_for_field)] + \
            [Contact(firstname='firstname', middlename='middlename',
                     lastname='lastname', nickname='nickname',
                     title='title', company='company',
                     address='address', homephone=r'+79509999999',
                     mobilephone=r'+79509999999', workphone=r'+79509999999',
                     faxphone=random_string(20), mail='mail',
                     email2='email2', email3='email3',
                     homepage='homepage',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='address2', secondaryphone='secondaryphone') for _ in range(max_tests_for_field)] + \
            [Contact(firstname='firstname', middlename='middlename',
                     lastname='lastname', nickname='nickname',
                     title='title', company='company',
                     address='address', homephone=r'+79509999999',
                     mobilephone=r'+79509999999', workphone=r'+79509999999',
                     faxphone=r'+79509999999', mail=random_string(20),
                     email2='email2', email3='email3',
                     homepage='homepage',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='address2', secondaryphone='secondaryphone') for _ in range(max_tests_for_field)] + \
            [Contact(firstname='firstname', middlename='middlename',
                     lastname='lastname', nickname='nickname',
                     title='title', company='company',
                     address='address', homephone=r'+79509999999',
                     mobilephone=r'+79509999999', workphone=r'+79509999999',
                     faxphone=r'+79509999999', mail='mail',
                     email2=random_string(20), email3='email3',
                     homepage='homepage',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='address2', secondaryphone='secondaryphone') for _ in range(max_tests_for_field)] + \
            [Contact(firstname='firstname', middlename='middlename',
                     lastname='lastname', nickname='nickname',
                     title='title', company='company',
                     address='address', homephone=r'+79509999999',
                     mobilephone=r'+79509999999', workphone=r'+79509999999',
                     faxphone=r'+79509999999', mail='mail',
                     email2='email2', email3=random_string(20),
                     homepage='homepage',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='address2', secondaryphone='secondaryphone') for _ in range(max_tests_for_field)] + \
            [Contact(firstname='firstname', middlename='middlename',
                     lastname='lastname', nickname='nickname',
                     title='title', company='company',
                     address='address', homephone=r'+79509999999',
                     mobilephone=r'+79509999999', workphone=r'+79509999999',
                     faxphone=r'+79509999999', mail='mail',
                     email2='email2', email3='email3',
                     homepage=random_string(20),
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='address2', secondaryphone='secondaryphone') for _ in range(max_tests_for_field)] + \
            [Contact(firstname='firstname', middlename='middlename',
                     lastname='lastname', nickname='nickname',
                     title='title', company='company',
                     address='address', homephone=r'+79509999999',
                     mobilephone=r'+79509999999', workphone=r'+79509999999',
                     faxphone=r'+79509999999', mail='mail',
                     email2='email2', email3='email3',
                     homepage='homepage',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2=random_string(20), secondaryphone='secondaryphone') for _ in range(max_tests_for_field)] + \
            [Contact(firstname='firstname', middlename='middlename',
                     lastname='lastname', nickname='nickname',
                     title='title', company='company',
                     address='address', homephone=r'+79509999999',
                     mobilephone=r'+79509999999', workphone=r'+79509999999',
                     faxphone=r'+79509999999', mail='mail',
                     email2='email2', email3='email3', homepage='homepage',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='address2', secondaryphone=random_string(20)) for _ in range(max_tests_for_field)]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert app.contact.count() == len(old_contacts) + 1
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_contact_by_index(0)
    assert len(old_contacts) - 1 == app.contact.count()