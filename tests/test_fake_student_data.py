import app
from app.domain.create_group_student import StudentCreator, GroupCreator
from app.domain.create_subject_time_table import TimeTableCreator
from app.domain.entities import Student, Group, Gender


def test_get_full_name_male(s_data, monkeypatch):
    def mock_male_gender(*args, **kwargs):
        return Gender.MALE

    monkeypatch.setattr(app.domain.create_group_student, "choice", mock_male_gender)
    assert s_data.get_fullname() == 'John'


def test_get_full_name_female(s_data, monkeypatch):
    def mock_female_gender(*args, **kwargs):
        return Gender.FEMALE

    monkeypatch.setattr(app.domain.create_group_student, "choice", mock_female_gender)
    assert s_data.get_fullname() == 'Anna'


def test_get_age(s_data):
    assert 18 <= s_data.get_age() <= 25


def test_get_height(s_data):
    assert 150 <= s_data.get_height() <= 210


def test_get_weight(s_data):
    assert 50 <= s_data.get_weight() <= 120


def test_get_average_score(s_data):
    assert 3 <= s_data.get_average_score() <= 5


def test_get_gender_male(s_data):
    s_data.gender = Gender.MALE
    assert s_data.get_gender() == 'М'


def test_get_gender_female(s_data):
    s_data.gender = Gender.FEMALE
    assert s_data.get_gender() == 'Ж'


def test_get_group_name(g_data):
    assert g_data.get_name() == 'MyGroup'


def test_student_creator(s_data):
    student = StudentCreator(s_data).run()
    assert isinstance(student, Student)


def test_group_creator(g_data, s_data):
    student = StudentCreator(s_data).run()
    timetable = TimeTableCreator().run(names=('Math', ), times=('07:00', ), week=('Mon', ))
    group = GroupCreator(g_data).run([student], timetable)
    assert isinstance(group, Group)
