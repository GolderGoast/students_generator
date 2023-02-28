from abc import ABC, abstractmethod
from dataclasses import dataclass

from entities import Group


@dataclass
class Report:
    type: str
    path: str = 'report'


class ITypeReport(ABC):
    def __init__(self, report_type: str):
        self.report_type = report_type

    @abstractmethod
    def run(self):
        pass


class IReportGetter(ABC):
    def __init__(self, groups: list[Group], report_type: ITypeReport):
        self.groups = groups
        self.report_type = report_type

    @abstractmethod
    def get_report(self):
        pass
