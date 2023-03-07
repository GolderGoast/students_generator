from app.domain.create_subject_time_table import SubjectDataCreator, SubjectCreator, TimeTableCreator
from app.domain.entities import Subject, TimeTable


def test_subj_creator():
    subject = SubjectCreator(SubjectDataCreator('Math', 'Mon', '07:00')).run()
    assert isinstance(subject, Subject)
    assert subject.name == 'Math'
    assert subject.day_of_week == 'Mon'
    assert subject.time == '07:00'


def test_timetable_creator():
    timetable = TimeTableCreator().run(names=('Math', ), times=('07:00', ), week=('Mon', ))
    assert isinstance(timetable, TimeTable)
    assert len(timetable.subjects) == 1
    for subj in timetable.subjects:
        assert isinstance(subj, Subject)
