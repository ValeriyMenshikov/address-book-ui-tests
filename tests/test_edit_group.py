from model.group import Group


def test_edit_first_group(app):
    app.group.edit_first_group(Group(name="1111", header="111", footer="111"))
