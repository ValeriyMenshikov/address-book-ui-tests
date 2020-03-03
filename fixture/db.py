import pymysql
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        group_list = []
        with self.connection.cursor() as cursor:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                group_list.append(Group(id=str(id), name=name, header=header, footer=footer))
        return group_list

    def get_contact_list(self):
        contact_list = []
        with self.connection.cursor() as cursor:
            cursor.execute("""select 
                                    id, firstname, middlename, lastname, nickname, company, 
                                    title, address, home, mobile, work, fax, email, email2, 
                                    email3, homepage, bday, bmonth, byear, aday, amonth,	
                                    ayear, address2, phone2 
                               from addressbook""")

            for row in cursor:
                (id, firstname, middlename, lastname, nickname, company,
                 title, address, homephone, mobilephone, workphone, faxphone, email, email2,
                 email3, homepage, bday, bmonth, byear, aday, amonth,
                 ayear, address2, secondaryphone) = row
                contact_list.append(Contact(id=id, firstname=firstname, middlename=middlename,
                                            lastname=lastname, nickname=nickname,
                                            title=title, company=company,
                                            address=address, homephone=homephone,
                                            mobilephone=mobilephone, workphone=workphone,
                                            faxphone=faxphone, mail=email,
                                            email2=email2, email3=email3,
                                            homepage=homepage,
                                            bday=bday, bmonth=bmonth, byear=byear,
                                            aday=aday, amonth=amonth, ayear=ayear,
                                            address2=address2, secondaryphone=secondaryphone))
        return contact_list

    def destroy(self):
        self.connection.close()
