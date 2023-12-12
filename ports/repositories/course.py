from typing import Protocol

from domain import Course
from ports.external.database import AppDatabasePort


class CourseRepositoryPort(Protocol):
    def __init__(self, db: AppDatabasePort):
        pass

    def get_course(self, course_id):
        pass

    def insert_course(self, course: Course):
        pass

    def get_all_courses(self):
        pass

    def delete_course(self, course: Course):
        pass