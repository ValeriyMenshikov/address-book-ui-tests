from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.edit_first_contact(Contact(firstname="fdsdf", middlename="asdffssdasd", lastname="213123f",
                                           nickname="12fdvsdf", byear="2000", aday="11",
                                           amonth="February", ayear="2001", address2="asdawe21e2", phone2="123123dasf",
                                           notes="sfdsd"))
