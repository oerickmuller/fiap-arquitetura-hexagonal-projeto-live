# ports/student
from typing import Protocol

from domain.student import Student
from ports.repositories.student import StudentRepositoryPort


class StudentServicePort(Protocol):
    def __init__(self, repo: StudentRepositoryPort):
        pass

    def new_student(self, student: Student):
        pass

    def get_student(self, student_id):
        pass

    def delete_student(self, student: Student):
        pass
