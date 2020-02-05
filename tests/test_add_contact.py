# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="asdasdasd", middlename="asdasd", lastname="asdfvf", nickname="asdfsdf",
                               title="sadfvsdf", company="asdfsdfsdf", address="bvbbgfbdfgb", home="dcfscfsd",
                               mobile="12312323", work="dsfsdf", fax="123123123", mail="asdasd@mail.ru",
                               email2="asdsad@mail.ru", email3="ghh213@gmail.ru", homepage="asdasd", bday="1",
                               bmonth="January", byear="1999", aday="11", amonth="February", ayear="2000",
                               address2="sdfsdfsdf", phone2="ghjnhjkn", notes="hgjkhmjkhjkm"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
