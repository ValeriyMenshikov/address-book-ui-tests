from model.group import Group
from random import randrange


def test_edit_some_group(app):
    if app.group.count() == 0:
        group = Group(name="1111", header="111", footer="111")
        app.group.create(group)
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="222", header="333", footer="444")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
