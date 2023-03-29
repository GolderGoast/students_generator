from random import choice

from domain.entities import ISubjectCreator, ISubjectDataCreator, ITimeTableCreator, Subject, TimeTable

SUBJECTS_NAMES = ("Математика", "Русский язык", "Литература", "История", "Информатика", "Биология", "Физкультура", "")
WEEK = ("Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс")
TIMES = ("07:00", "09:00", "11:00", "13:00", "15:00", "17:00")


class SubjectDataCreator(ISubjectDataCreator):
    def __init__(self, name: str, day: str, time: str):
        self.name = name
        self.day = day
        self.time = time

    def get_name(self):
        return self.name

    def get_day(self):
        return self.day

    def get_time(self):
        return self.time


class SubjectCreator(ISubjectCreator):
    def run(self) -> Subject:
        name = self.subj_data.get_name()
        day = self.subj_data.get_day()
        time = self.subj_data.get_time()

        return Subject(name=name, day_of_week=day, time=time)


class TimeTableCreator(ITimeTableCreator):
    def run(self, week: tuple[str, ...], times: tuple[str, ...], names: tuple[str, ...]) -> TimeTable:
        if self.subjects:
            self.subjects = []

        for day in week:
            for time in times:
                if day in ["Сб", "Вс"]:
                    self.subjects.append(SubjectCreator(SubjectDataCreator(name="", day=day, time=time)).run())
                else:
                    self.subjects.append(
                        SubjectCreator(SubjectDataCreator(name=choice(names), day=day, time=time)).run()
                    )
        return TimeTable(subjects=self.subjects, week=week, times=times)
