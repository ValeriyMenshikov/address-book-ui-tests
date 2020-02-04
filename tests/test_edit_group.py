from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="1111", header="111", footer="111"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="222", header="333", footer="444"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)