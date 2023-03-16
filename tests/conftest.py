from random import randint

import pytest

from app.domain.create_group_student import FakeStudentData, FakeGroupData


@pytest.fixture()
def create_mock_faker():
    class MockFaker:
        def __init__(self):
            self._name_male = 'John'
            self._name_female = 'Anna'
            self._group_name = 'MyGroup'
            self._email = 'abcd@mail.ru'

        def name_male(self):
            return self._name_male

        def name_female(self):
            return self._name_female

        def company(self):
            return self._group_name

        def free_email(self):
            return self._email

        @staticmethod
        def random_int(a, b):
            return randint(a, b)

    return MockFaker()


@pytest.fixture()
def s_data(create_mock_faker):
    s_data = FakeStudentData(create_mock_faker)
    return s_data


@pytest.fixture()
def g_data(create_mock_faker):
    g_data = FakeGroupData(create_mock_faker)
    return g_data
