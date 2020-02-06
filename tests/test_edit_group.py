from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        group = Group(name="1111", header="111", footer="111")
        app.group.create(group)
    old_groups = app.group.get_group_list()
    group = Group(name="222", header="333", footer="444")
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
