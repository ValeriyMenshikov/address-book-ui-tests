# -*- coding: utf-8 -*-
from model.group import Group
import random
import string

constant = [
    Group(name="name", header="header", footer="footer"),
    Group(name="name1", header="header1", footer="footer")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + ' ' * 10
    return prefix + ''.join([random.choice(symbols) for _ in range(random.randrange(maxlen))])


test_data = [Group(name="", header="", footer="")] + \
            [Group(name=random_string('name', 10),
                   header=random_string('header', 20),
                   footer=random_string('footer', 20)) for _ in range(5)]
