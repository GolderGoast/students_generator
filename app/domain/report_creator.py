from abc import ABC, abstractmethod

from app.domain.entities import Group


class IReportGetter(ABC):
    def __init__(self, groups: list[Group], report_path: str = "report"):
        self.groups = groups
        self.report_path = report_path

    @abstractmethod
    def get_report(self):
        pass
