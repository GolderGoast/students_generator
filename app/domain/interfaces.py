from abc import ABC, abstractmethod

from domain.entities import Group, Student, Subject, TimeTable


class IReportBuilder(ABC):
    def __init__(self, groups: list[Group], report_path: str = "report"):
        self.groups = groups
        self.report_path = report_path

    @abstractmethod
    def get_report(self):
        pass


class IFakeStudentDataCreator(ABC):
    @abstractmethod
    def get_fullname(self) -> str:
        pass

    @abstractmethod
    def get_email(self) -> str:
        pass

    @abstractmethod
    def get_password(self) -> str:
        pass

    @abstractmethod
    def get_age(self) -> int:
        pass

    @abstractmethod
    def get_gender(self) -> str:
        pass

    @abstractmethod
    def get_weight(self) -> int:
        pass

    @abstractmethod
    def get_height(self) -> int:
        pass

    @abstractmethod
    def get_average_score(self) -> float:
        pass


class IFakeGroupDataCreator(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass


class IStudentCreator(ABC):
    def __init__(self, faker: IFakeStudentDataCreator):
        self.faker = faker

    @abstractmethod
    def run(self) -> Student:
        pass


class IGroupCreator(ABC):
    def __init__(self, faker: IFakeGroupDataCreator):
        self.faker = faker

    @abstractmethod
    def run(self, students: list[Student], timetable: TimeTable) -> Group:
        pass


class ISubjectDataCreator(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_day(self):
        pass

    @abstractmethod
    def get_time(self):
        pass


class ISubjectCreator(ABC):
    def __init__(self, subj_data: ISubjectDataCreator):
        self.subj_data = subj_data

    @abstractmethod
    def run(self) -> Subject:
        pass


class ITimeTableCreator(ABC):
    def __init__(self):
        self.subjects: list[Subject] = []

    @abstractmethod
    def run(self, week: tuple[str, ...], times: tuple[str, ...], names: tuple[str, ...]) -> TimeTable:
        pass
