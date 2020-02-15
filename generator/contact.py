# -*- coding: utf-8 -*-
import os.path
import random
import string
import jsonpickle
import getopt
import sys
from model.contact import Contact

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", 'file'])
except getopt.GetoptError:
    sys.exit(2)

n = 5
max_tests_for_field = n

f = 'data/contacts.json'

for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == '-f':
        f = a


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + ' ' * 10
    return ''.join([random.choice(symbols) for _ in range(random.randrange(maxlen))])


test_data = [Contact(firstname='Степан ', middlename='Иванович ',
                     lastname='Петров ', nickname='Иваныч ',
                     title='title', company='ОАО ОмПО Радиозавод им. А.С.Попова(РЕЛЕРО) ',
                     address='г. Омск ул.Ленина д.1 кв. 99', homephone=r'+79509999999',
                     mobilephone=r'+79509999999', workphone=r'+79509999999',
                     faxphone=r'+79509999999', mail='email1@mail.ru',
                     email2='email2@mail.ru', email3='email3@mail.ru',
                     homepage='www.homepage.ru',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='г. Омск ул. Маршала Жукова д.№ 79 кв.№ 105 ', secondaryphone='84952000600')] + \
            [Contact(firstname=random_string(20), middlename='Иванович ',
                     lastname='Петров ', nickname='Иваныч ',
                     title='title', company='ОАО ОмПО Радиозавод им. А.С.Попова(РЕЛЕРО) ',
                     address='г. Омск ул.Ленина д.1 кв. 99', homephone=r'+79509999999',
                     mobilephone=r'+79509999999', workphone=r'+79509999999',
                     faxphone=r'+79509999999', mail='email1@mail.ru',
                     email2='email2@mail.ru', email3='email3@mail.ru',
                     homepage='www.homepage.ru',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='г. Омск ул. Маршала Жукова д.№ 79 кв.№ 105 ', secondaryphone='84952000600') for _ in
             range(max_tests_for_field)] + \
            [Contact(firstname='Степан ', middlename=random_string(20),
                     lastname='Петров ', nickname='Иваныч ',
                     title='title', company='ОАО ОмПО Радиозавод им. А.С.Попова(РЕЛЕРО) ',
                     address='г. Омск ул.Ленина д.1 кв. 99', homephone=r'+79509999999',
                     mobilephone=r'+79509999999', workphone=r'+79509999999',
                     faxphone=r'+79509999999', mail='email1@mail.ru',
                     email2='email2@mail.ru', email3='email3@mail.ru',
                     homepage='www.homepage.ru',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='г. Омск ул. Маршала Жукова д.№ 79 кв.№ 105 ', secondaryphone='84952000600') for _ in
             range(max_tests_for_field)] + \
            [Contact(firstname='Степан ', middlename='Иванович ',
                     lastname=random_string(20), nickname='Иваныч ',
                     title='title', company='ОАО ОмПО Радиозавод им. А.С.Попова(РЕЛЕРО) ',
                     address='г. Омск ул.Ленина д.1 кв. 99', homephone=r'+79509999999',
                     mobilephone=r'+79509999999', workphone=r'+79509999999',
                     faxphone=r'+79509999999', mail='email1@mail.ru',
                     email2='email2@mail.ru', email3='email3@mail.ru',
                     homepage='www.homepage.ru',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='г. Омск ул. Маршала Жукова д.№ 79 кв.№ 105 ', secondaryphone='84952000600') for _ in
             range(max_tests_for_field)] + \
            [Contact(firstname='Степан ', middlename='Иванович ',
                     lastname='Петров ', nickname=random_string(20),
                     title='title', company='ОАО ОмПО Радиозавод им. А.С.Попова(РЕЛЕРО) ',
                     address='г. Омск ул.Ленина д.1 кв. 99', homephone=r'+79509999999',
                     mobilephone=r'+79509999999', workphone=r'+79509999999',
                     faxphone=r'+79509999999', mail='email1@mail.ru',
                     email2='email2@mail.ru', email3='email3@mail.ru',
                     homepage='www.homepage.ru',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='г. Омск ул. Маршала Жукова д.№ 79 кв.№ 105 ', secondaryphone='84952000600') for _ in
             range(max_tests_for_field)] + \
            [Contact(firstname='Степан ', middlename='Иванович ',
                     lastname='Петров ', nickname='Иваныч ',
                     title=random_string(20), company='ОАО ОмПО Радиозавод им. А.С.Попова(РЕЛЕРО) ',
                     address='г. Омск ул.Ленина д.1 кв. 99', homephone=r'+79509999999',
                     mobilephone=r'+79509999999', workphone=r'+79509999999',
                     faxphone=r'+79509999999', mail='email1@mail.ru',
                     email2='email2@mail.ru', email3='email3@mail.ru',
                     homepage='www.homepage.ru',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='г. Омск ул. Маршала Жукова д.№ 79 кв.№ 105 ', secondaryphone='84952000600') for _ in
             range(max_tests_for_field)] + \
            [Contact(firstname='Степан ', middlename='Иванович ',
                     lastname='Петров ', nickname='Иваныч ',
                     title='title', company=random_string(20),
                     address='г. Омск ул.Ленина д.1 кв. 99', homephone=r'+79509999999',
                     mobilephone=r'+79509999999', workphone=r'+79509999999',
                     faxphone=r'+79509999999', mail='email1@mail.ru',
                     email2='email2@mail.ru', email3='email3@mail.ru',
                     homepage='www.homepage.ru',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='г. Омск ул. Маршала Жукова д.№ 79 кв.№ 105 ', secondaryphone='84952000600') for _ in
             range(max_tests_for_field)] + \
            [Contact(firstname='Степан ', middlename='Иванович ',
                     lastname='Петров ', nickname='Иваныч ',
                     title='title', company='ОАО ОмПО Радиозавод им. А.С.Попова(РЕЛЕРО) ',
                     address=random_string(20), homephone=r'+79509999999',
                     mobilephone=r'+79509999999', workphone=r'+79509999999',
                     faxphone=r'+79509999999', mail='email1@mail.ru',
                     email2='email2@mail.ru', email3='email3@mail.ru',
                     homepage='www.homepage.ru',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='г. Омск ул. Маршала Жукова д.№ 79 кв.№ 105 ', secondaryphone='84952000600') for _ in
             range(max_tests_for_field)] + \
            [Contact(firstname='Степан ', middlename='Иванович ',
                     lastname='Петров ', nickname='Иваныч ',
                     title='title', company='ОАО ОмПО Радиозавод им. А.С.Попова(РЕЛЕРО) ',
                     address='г. Омск ул.Ленина д.1 кв. 99', homephone=random_string(20),
                     mobilephone=r'+79509999999', workphone=r'+79509999999',
                     faxphone=r'+79509999999', mail='email1@mail.ru',
                     email2='email2@mail.ru', email3='email3@mail.ru',
                     homepage='www.homepage.ru',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='г. Омск ул. Маршала Жукова д.№ 79 кв.№ 105 ', secondaryphone='84952000600') for _ in
             range(max_tests_for_field)] + \
            [Contact(firstname='Степан ', middlename='Иванович ',
                     lastname='Петров ', nickname='Иваныч ',
                     title='title', company='ОАО ОмПО Радиозавод им. А.С.Попова(РЕЛЕРО) ',
                     address='г. Омск ул.Ленина д.1 кв. 99', homephone=r'+79509999999',
                     mobilephone=random_string(20), workphone=r'+79509999999',
                     faxphone=r'+79509999999', mail='email1@mail.ru',
                     email2='email2@mail.ru', email3='email3@mail.ru',
                     homepage='www.homepage.ru',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='г. Омск ул. Маршала Жукова д.№ 79 кв.№ 105 ', secondaryphone='84952000600') for _ in
             range(max_tests_for_field)] + \
            [Contact(firstname='Степан ', middlename='Иванович ',
                     lastname='Петров ', nickname='Иваныч ',
                     title='title', company='ОАО ОмПО Радиозавод им. А.С.Попова(РЕЛЕРО) ',
                     address='г. Омск ул.Ленина д.1 кв. 99', homephone=r'+79509999999',
                     mobilephone=r'+79509999999', workphone=random_string(20),
                     faxphone=r'+79509999999', mail='email1@mail.ru',
                     email2='email2@mail.ru', email3='email3@mail.ru',
                     homepage='www.homepage.ru',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='г. Омск ул. Маршала Жукова д.№ 79 кв.№ 105 ', secondaryphone='84952000600') for _ in
             range(max_tests_for_field)] + \
            [Contact(firstname='Степан ', middlename='Иванович ',
                     lastname='Петров ', nickname='Иваныч ',
                     title='title', company='ОАО ОмПО Радиозавод им. А.С.Попова(РЕЛЕРО) ',
                     address='г. Омск ул.Ленина д.1 кв. 99', homephone=r'+79509999999',
                     mobilephone=r'+79509999999', workphone=r'+79509999999',
                     faxphone=random_string(20), mail='email1@mail.ru',
                     email2='email2@mail.ru', email3='email3@mail.ru',
                     homepage='www.homepage.ru',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='г. Омск ул. Маршала Жукова д.№ 79 кв.№ 105 ', secondaryphone='84952000600') for _ in
             range(max_tests_for_field)] + \
            [Contact(firstname='Степан ', middlename='Иванович ',
                     lastname='Петров ', nickname='Иваныч ',
                     title='title', company='ОАО ОмПО Радиозавод им. А.С.Попова(РЕЛЕРО) ',
                     address='г. Омск ул.Ленина д.1 кв. 99', homephone=r'+79509999999',
                     mobilephone=r'+79509999999', workphone=r'+79509999999',
                     faxphone=r'+79509999999', mail=random_string(20),
                     email2='email2@mail.ru', email3='email3@mail.ru',
                     homepage='www.homepage.ru',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='г. Омск ул. Маршала Жукова д.№ 79 кв.№ 105 ', secondaryphone='84952000600') for _ in
             range(max_tests_for_field)] + \
            [Contact(firstname='Степан ', middlename='Иванович ',
                     lastname='Петров ', nickname='Иваныч ',
                     title='title', company='ОАО ОмПО Радиозавод им. А.С.Попова(РЕЛЕРО) ',
                     address='г. Омск ул.Ленина д.1 кв. 99', homephone=r'+79509999999',
                     mobilephone=r'+79509999999', workphone=r'+79509999999',
                     faxphone=r'+79509999999', mail='email1@mail.ru',
                     email2=random_string(20), email3='email3@mail.ru',
                     homepage='www.homepage.ru',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='г. Омск ул. Маршала Жукова д.№ 79 кв.№ 105 ', secondaryphone='84952000600') for _ in
             range(max_tests_for_field)] + \
            [Contact(firstname='Степан ', middlename='Иванович ',
                     lastname='Петров ', nickname='Иваныч ',
                     title='title', company='ОАО ОмПО Радиозавод им. А.С.Попова(РЕЛЕРО) ',
                     address='г. Омск ул.Ленина д.1 кв. 99', homephone=r'+79509999999',
                     mobilephone=r'+79509999999', workphone=r'+79509999999',
                     faxphone=r'+79509999999', mail='email1@mail.ru',
                     email2='email2@mail.ru', email3=random_string(20),
                     homepage='www.homepage.ru',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='г. Омск ул. Маршала Жукова д.№ 79 кв.№ 105 ', secondaryphone='84952000600') for _ in
             range(max_tests_for_field)] + \
            [Contact(firstname='Степан ', middlename='Иванович ',
                     lastname='Петров ', nickname='Иваныч ',
                     title='title', company='ОАО ОмПО Радиозавод им. А.С.Попова(РЕЛЕРО) ',
                     address='г. Омск ул.Ленина д.1 кв. 99', homephone=r'+79509999999',
                     mobilephone=r'+79509999999', workphone=r'+79509999999',
                     faxphone=r'+79509999999', mail='email1@mail.ru',
                     email2='email2@mail.ru', email3='email3@mail.ru',
                     homepage=random_string(20),
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='г. Омск ул. Маршала Жукова д.№ 79 кв.№ 105 ', secondaryphone='84952000600') for _ in
             range(max_tests_for_field)] + \
            [Contact(firstname='Степан ', middlename='Иванович ',
                     lastname='Петров ', nickname='Иваныч ',
                     title='title', company='ОАО ОмПО Радиозавод им. А.С.Попова(РЕЛЕРО) ',
                     address='г. Омск ул.Ленина д.1 кв. 99', homephone=r'+79509999999',
                     mobilephone=r'+79509999999', workphone=r'+79509999999',
                     faxphone=r'+79509999999', mail='email1@mail.ru',
                     email2='email2@mail.ru', email3='email3@mail.ru',
                     homepage='www.homepage.ru',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2=random_string(20), secondaryphone='84952000600') for _ in range(max_tests_for_field)] + \
            [Contact(firstname='Степан ', middlename='Иванович ',
                     lastname='Петров ', nickname='Иваныч ',
                     title='title', company='ОАО ОмПО Радиозавод им. А.С.Попова(РЕЛЕРО) ',
                     address='г. Омск ул.Ленина д.1 кв. 99', homephone=r'+79509999999',
                     mobilephone=r'+79509999999', workphone=r'+79509999999',
                     faxphone=r'+79509999999', mail='email1@mail.ru',
                     email2='email2@mail.ru', email3='email3@mail.ru', homepage='www.homepage.ru',
                     bday="1", bmonth="January", byear="1999",
                     aday="11", amonth="February", ayear="2000",
                     address2='г. Омск ул. Маршала Жукова д.№ 79 кв.№ 105 ', secondaryphone=random_string(20)) for _ in
             range(max_tests_for_field)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, 'w') as out:
    jsonpickle.set_encoder_options('json', indent=2)
    out.write(jsonpickle.encode(test_data))
