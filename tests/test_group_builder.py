from app.domain.create_group_student import StudentCreator, GroupCreator
from app.domain.create_subject_time_table import TimeTableCreator
from app.domain.entities import Group
from app.domain.group_builder import GroupsBuilder


def test_build_groups_type(s_data, g_data):
    builder = GroupsBuilder(GroupCreator(g_data), StudentCreator(s_data), 2, 5, TimeTableCreator())
    groups = builder.run()
    assert all([isinstance(group, Group) for group in groups])


def test_build_groups_count(s_data, g_data):
    builder = GroupsBuilder(GroupCreator(g_data), StudentCreator(s_data), 2, 5, TimeTableCreator())
    groups = builder.run()
    assert len(groups) == 2


def test_build_groups_count_students(s_data, g_data):
    builder = GroupsBuilder(GroupCreator(g_data), StudentCreator(s_data), 2, 5, TimeTableCreator())
    groups = builder.run()
    assert len(groups[0].students) == 5
