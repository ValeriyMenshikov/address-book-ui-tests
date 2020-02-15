# -*- coding: utf-8 -*-
from model.contact import Contact

test_data = [
    Contact(firstname='Степан ', middlename='Иванович ',
            lastname='Петров ', nickname='Иваныч ',
            title='title', company='ОАО ОмПО Радиозавод им. А.С.Попова(РЕЛЕРО) ',
            address='г. Омск ул.Ленина д.1 кв. 99', homephone=r'+79509999999',
            mobilephone=r'+79509999999', workphone=r'+79509999999',
            faxphone=r'+79509999999', mail='email1@mail.ru',
            email2='email2@mail.ru', email3='email3@mail.ru',
            homepage='www.homepage.ru',
            bday="1", bmonth="January", byear="1999",
            aday="11", amonth="February", ayear="2000",
            address2='г. Омск ул. Маршала Жукова д.№ 79 кв.№ 105 ', secondaryphone='84952000600'),
    Contact(firstname='Петр ', middlename='Степанович ',
            lastname='Степанович ', nickname='Иваныч ',
            title='title', company='ОАО ОмПО Радиозавод им. А.С.Попова(РЕЛЕРО) ',
            address='г. Омск ул.Ленина д.1 кв. 99', homephone=r'+79509999999',
            mobilephone=r'+79509999999', workphone=r'+79509999999',
            faxphone=r'+79509999999', mail='email1@mail.ru',
            email2='email2@mail.ru', email3='email3@mail.ru',
            homepage='www.homepage.ru',
            bday="1", bmonth="January", byear="1999",
            aday="11", amonth="February", ayear="2000",
            address2='г. Омск ул. Маршала Жукова д.№ 79 кв.№ 105 ', secondaryphone='84952000600')
]
