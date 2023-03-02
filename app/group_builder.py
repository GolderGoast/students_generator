from entities import Group, IGroupCreator, IStudentCreator


class GroupsBuilder:
    def __init__(
        self, group_creator: IGroupCreator, student_creator: IStudentCreator, groups_count: int, students_count: int
    ):
        self.group_creator = group_creator
        self.student_creator = student_creator
        self.groups_count = groups_count
        self.students_count = students_count

    def run(self) -> list[Group]:
        groups = [
            self.group_creator.run([self.student_creator.run() for _ in range(self.students_count)])
            for _ in range(self.groups_count)
        ]

        return groups
