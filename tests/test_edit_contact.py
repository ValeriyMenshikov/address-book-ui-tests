from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.edit_first_contact(Contact(firstname="fdsdf", middlename="asdffssdasd", lastname="213123f",
                                           nickname="12fdvsdf", photo="D:\\DocLuber.pdf", title="fvdg35435 345",
                                           company="34554 fgd ", address="45435", home="dcfs78678cfsd",
                                           mobile="fgdfgf", work="cvbcv", fax="cbbvb", mail="asdasd@dfgdfgdfgmail.ru",
                                           email2="dgdfg453543@mail.ru", email3="34534gfdgdf@gmail.ru",
                                           homepage="dfg43345", bday="12", bmonth="January", byear="2000", aday="11",
                                           amonth="February", ayear="2001", address2="asdawe21e2", phone2="123123dasf",
                                           notes="sfdsd"))
