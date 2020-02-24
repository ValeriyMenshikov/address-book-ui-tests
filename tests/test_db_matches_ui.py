from model.group import Group
import re


def test_group_list(app, db):
    def clean(group):
        return Group(id=re.sub(r'\s', '', group.id), name=re.sub(r'\s', '', group.name))

    ui_list = map(clean, app.group.get_group_list())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
