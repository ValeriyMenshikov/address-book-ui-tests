from model.group import Group
from random import randrange


def test_edit_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        group = Group(name="1111", header="111", footer="111")
        app.group.create(group)
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="222", header="333", footer="444")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
