# ports/course

from typing import Protocol
from domain.course import Course
from ports.database import AppDatabasePort


class CourseRepository(Protocol):
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


class CourseService(Protocol):
    def __init__(self, repo: CourseRepository):
        pass

    def get_course(self, course_id: str):
        pass

    def new_course(self, course: Course):
        pass

    def get_all_courses(self):
        pass

    def delete_course(self, course: Course):
        pass
