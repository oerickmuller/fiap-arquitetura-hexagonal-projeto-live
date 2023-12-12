# ports/course

from typing import Protocol
from domain.course import Course
from ports.repositories.course import CourseRepositoryPort


class CourseServicePort(Protocol):
    def __init__(self, repo: CourseRepositoryPort):
        pass

    def get_course(self, course_id: str):
        pass

    def new_course(self, course: Course):
        pass

    def get_all_courses(self):
        pass

    def delete_course(self, course: Course):
        pass
