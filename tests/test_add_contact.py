# -*- coding: utf-8 -*-
from model.contact import Contact

import pytest
import random
import string


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + ' ' * 10
    return ''.join([random.choice(symbols) for _ in range(random.randrange(maxlen))])


test_data = [''] + [random_string(20) for _ in range(2)]


@pytest.mark.parametrize("field", test_data, ids=[repr(x) for x in test_data])
def test_add_contact_name(app, field):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname=field, middlename='middlename',
                      lastname='lastname', nickname='nickname',
                      title='title', company='company',
                      address='address', homephone=r'+79509999999',
                      mobilephone=r'+79509999999', workphone=r'+79509999999',
                      faxphone=r'+79509999999', mail='mail',
                      email2='email2', email3='email3',
                      homepage='homepage',
                      bday="1", bmonth="January", byear="1999",
                      aday="11", amonth="February", ayear="2000",
                      address2='address2', secondaryphone='secondaryphone')
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


test_data = [''] + [random_string(12) for _ in range(2)]


@pytest.mark.parametrize("field", test_data, ids=[repr(x) for x in test_data])
def test_add_contact_middlename(app, field):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname='firstname', middlename=field,
                      lastname='lastname', nickname='nickname',
                      title='title', company='company',
                      address='address', homephone=r'+79509999999',
                      mobilephone=r'+79509999999', workphone=r'+79509999999',
                      faxphone=r'+79509999999', mail='mail',
                      email2='email2', email3='email3',
                      homepage='homepage',
                      bday="1", bmonth="January", byear="1999",
                      aday="11", amonth="February", ayear="2000",
                      address2='address2', secondaryphone='secondaryphone')
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


test_data = [''] + [random_string(12) for _ in range(2)]


@pytest.mark.parametrize("field", test_data, ids=[repr(x) for x in test_data])
def test_add_contact_lastname(app, field):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname='firstname', middlename='middlename',
                      lastname=field, nickname='nickname',
                      title='title', company='company',
                      address='address', homephone=r'+79509999999',
                      mobilephone=r'+79509999999', workphone=r'+79509999999',
                      faxphone=r'+79509999999', mail='mail',
                      email2='email2', email3='email3',
                      homepage='homepage',
                      bday="1", bmonth="January", byear="1999",
                      aday="11", amonth="February", ayear="2000",
                      address2='address2', secondaryphone='secondaryphone')
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


test_data = [''] + [random_string(12) for _ in range(2)]


@pytest.mark.parametrize("field", test_data, ids=[repr(x) for x in test_data])
def test_add_contact_nickname(app, field):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname='firstname', middlename='middlename',
                      lastname='lastname', nickname=field,
                      title='title', company='company',
                      address='address', homephone=r'+79509999999',
                      mobilephone=r'+79509999999', workphone=r'+79509999999',
                      faxphone=r'+79509999999', mail='mail',
                      email2='email2', email3='email3',
                      homepage='homepage',
                      bday="1", bmonth="January", byear="1999",
                      aday="11", amonth="February", ayear="2000",
                      address2='address2', secondaryphone='secondaryphone')
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


test_data = [''] + [random_string(12) for _ in range(2)]


@pytest.mark.parametrize("field", test_data, ids=[repr(x) for x in test_data])
def test_add_contact_title(app, field):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname='firstname', middlename='middlename',
                      lastname='lastname', nickname='nickname',
                      title=field, company='company',
                      address='address', homephone=r'+79509999999',
                      mobilephone=r'+79509999999', workphone=r'+79509999999',
                      faxphone=r'+79509999999', mail='mail',
                      email2='email2', email3='email3',
                      homepage='homepage',
                      bday="1", bmonth="January", byear="1999",
                      aday="11", amonth="February", ayear="2000",
                      address2='address2', secondaryphone='secondaryphone')
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


test_data = [''] + [random_string(12) for _ in range(2)]


@pytest.mark.parametrize("field", test_data, ids=[repr(x) for x in test_data])
def test_add_contact_company(app, field):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname='firstname', middlename='middlename',
                      lastname='lastname', nickname='nickname',
                      title='title', company=field,
                      address='address', homephone=r'+79509999999',
                      mobilephone=r'+79509999999', workphone=r'+79509999999',
                      faxphone=r'+79509999999', mail='mail',
                      email2='email2', email3='email3',
                      homepage='homepage',
                      bday="1", bmonth="January", byear="1999",
                      aday="11", amonth="February", ayear="2000",
                      address2='address2', secondaryphone='secondaryphone')
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


test_data = [''] + [random_string(12) for _ in range(2)]


@pytest.mark.parametrize("field", test_data, ids=[repr(x) for x in test_data])
def test_add_contact_address(app, field):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname='firstname', middlename='middlename',
                      lastname='lastname', nickname='nickname',
                      title='title', company='company',
                      address=field, homephone=r'+79509999999',
                      mobilephone=r'+79509999999', workphone=r'+79509999999',
                      faxphone=r'+79509999999', mail='mail',
                      email2='email2', email3='email3',
                      homepage='homepage',
                      bday="1", bmonth="January", byear="1999",
                      aday="11", amonth="February", ayear="2000",
                      address2='address2', secondaryphone='secondaryphone')
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


test_data = [''] + [random_string(12) for _ in range(2)]


@pytest.mark.parametrize("field", test_data, ids=[repr(x) for x in test_data])
def test_add_contact_homephone(app, field):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname='firstname', middlename='middlename',
                      lastname='lastname', nickname='nickname',
                      title='title', company='company',
                      address='address', homephone=field,
                      mobilephone=r'+79509999999', workphone=r'+79509999999',
                      faxphone=r'+79509999999', mail='mail',
                      email2='email2', email3='email3',
                      homepage='homepage',
                      bday="1", bmonth="January", byear="1999",
                      aday="11", amonth="February", ayear="2000",
                      address2='address2', secondaryphone='secondaryphone')
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
