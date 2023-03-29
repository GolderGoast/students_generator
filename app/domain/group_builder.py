from domain.create_subject_time_table import SUBJECTS_NAMES, TIMES, WEEK
from domain.entities import Group, IGroupCreator, IStudentCreator, ITimeTableCreator


class GroupsBuilder:
    def __init__(
        self,
        group_creator: IGroupCreator,
        student_creator: IStudentCreator,
        groups_count: int,
        students_count: int,
        timetable_creator: ITimeTableCreator,
    ):
        self.group_creator = group_creator
        self.student_creator = student_creator
        self.groups_count = groups_count
        self.students_count = students_count
        self.timetable_creator = timetable_creator

    def run(self) -> list[Group]:
        groups = [
            self.group_creator.run(
                students=[self.student_creator.run() for _ in range(self.students_count)],
                timetable=self.timetable_creator.run(week=WEEK, times=TIMES, names=SUBJECTS_NAMES),
            )
            for _ in range(self.groups_count)
        ]

        return groups
