from typing import Protocol, List

from domain import Student
from ports.external.database import AppDatabasePort


class StudentRepositoryPort(Protocol):
    def __init__(self, db: AppDatabasePort):
        pass

    def insert_student(self, student: Student):
        pass

    def get_student(self, student_id):
        pass

    def delete_student(self, students: List[Student]):
        pass
