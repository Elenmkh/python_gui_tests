import random


def test_add_group(app):
    old_list = app.groups.get_group_list()
    if len(old_list)==0:
        app.groups.add_new_group("my group")
        old_list = app.groups.get_group_list()
    random_group = random.choice(old_list)
    app.groups.delete_group(random_group)
    new_list = app.groups.get_group_list()
    old_list.remove(random_group)
    assert sorted(old_list) == sorted(new_list)
