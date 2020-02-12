from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re
import time


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not len(wd.find_elements_by_name("searchstring")) > 0:
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # init user creation
        wd.find_element_by_link_text("add new").click()
        self.user_fill_form(contact)
        # submit user creation
        wd.find_element_by_name("submit").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def user_fill_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("photo", contact.photo)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("fax", contact.faxphone)
        self.change_field_value("email", contact.mail)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_select_field_value("bday", contact.bday)
        self.change_select_field_value("bmonth", contact.bmonth)
        self.change_select_field_value("aday", contact.aday)
        self.change_select_field_value("amonth", contact.amonth)
        self.change_field_value("byear", contact.byear)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("new_group", contact.new_group)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.secondaryphone)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_select_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        # submit contact deletion
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        # accept contact deletion
        wd.switch_to.alert.accept()
        # return to home page
        wd.find_element_by_link_text("home").click()
        self.contact_cache = None

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(0, contact)

    def open_edit_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        # init contact editing
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name('a').click()

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # init contact editing
        self.open_edit_contact_by_index(index)
        self.user_fill_form(contact)
        # submit user update
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def open_view_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        # View contact
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector('tr')[1:]:
                cells = element.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                lastname = cells[1].text.strip()
                firstname = cells[2].text.strip()
                address = cells[3].text.strip()
                all_emails = cells[4].text.strip()
                all_phones = cells[5].text.strip()
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, address=address, id=id,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_edit_contact_by_index(index)
        id = wd.find_element_by_name("id").get_attribute('value').strip()
        firstname = wd.find_element_by_name("firstname").get_attribute('value').strip()
        lastname = wd.find_element_by_name("lastname").get_attribute('value').strip()
        address = wd.find_element_by_name("address").text.strip()
        email1 = wd.find_element_by_name("email").get_attribute('value').strip()
        email2 = wd.find_element_by_name("email2").get_attribute('value').strip()
        email3 = wd.find_element_by_name("email3").get_attribute('value').strip()
        homephone = wd.find_element_by_name("home").get_attribute('value').strip()
        mobilephone = wd.find_element_by_name("mobile").get_attribute('value').strip()
        workphone = wd.find_element_by_name("work").get_attribute('value').strip()
        secondaryphone = wd.find_element_by_name("phone2").get_attribute('value').strip()
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                       homephone=homephone, mobilephone=mobilephone, mail=email1, email2=email2, email3=email3,
                       workphone=workphone, secondaryphone=secondaryphone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_view_contact_by_index(index)
        text = wd.find_element_by_id('content').text
        homephone = re.search('H: (.*)', text).group(1)
        mobilephone = re.search('M: (.*)', text).group(1)
        workphone = re.search('W: (.*)', text).group(1)
        secondaryphone = re.search('P: (.*)', text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)
