# ports/student
from typing import Protocol, List

from domain.student import Student

from ports.database import AppDatabasePort


class StudentRepository(Protocol):
    def __init__(self, db: AppDatabasePort):
        pass

    def insert_student(self, student: Student):
        pass

    def get_student(self, student_id):
        pass

    def delete_student(self, students: List[Student]):
        pass


class StudentService(Protocol):
    def __init__(self, repo: StudentRepository):
        pass

    def new_student(self, student: Student):
        pass

    def get_student(self, student_id):
        pass

    def delete_student(self, student: Student):
        pass
