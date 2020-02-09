from model.contact import Contact
from random import randrange
import time


def test_delete_first_contact(app, t):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='Peter'))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    time.sleep(1)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contacts
