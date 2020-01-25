from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="asdasdasd", middlename="asdasd", lastname="asdfvf", nickname="asdfsdf",
                                   title="sadfvsdf", company="asdfsdfsdf", address="bvbbgfbdfgb", home="dcfscfsd",
                                   mobile="12312323", work="dsfsdf", fax="123123123", mail="asdasd@mail.ru",
                                   email2="asdsad@mail.ru", email3="ghh213@gmail.ru", homepage="asdasd", bday="1",
                                   bmonth="January", byear="1999", aday="11", amonth="February", ayear="2000",
                                   address2="sdfsdfsdf", phone2="ghjnhjkn", notes="hgjkhmjkhjkm"))

    app.contact.edit_first_contact(Contact(firstname="fdsdf", middlename="asdffssdasd", lastname="213123f",
                                           nickname="12fdvsdf", byear="2000", aday="11",
                                           amonth="February", ayear="2001", address2="asdawe21e2", phone2="123123dasf",
                                           notes="sfdsd"))
