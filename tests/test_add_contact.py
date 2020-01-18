# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(firstname="asdasdasd", middlename="asdasd", lastname="asdfvf", nickname="asdfsdf",
                                   photo="D:\\DocLuber.pdf", title="sadfvsdf", company="asdfsdfsdf",
                                   address="bvbbgfbdfgb", home="dcfscfsd", mobile="12312323", work="dsfsdf",
                                   fax="123123123", mail="asdasd@mail.ru", email2="asdsad@mail.ru",
                                   email3="ghh213@gmail.ru", homepage="asdasd", bday="1",
                                   bmonth="January", byear="1999", aday="11", amonth="February", ayear="2000",
                                   address2="sdfsdfsdf", phone2="ghjnhjkn", notes="hgjkhmjkhjkm"))
    app.logout()
