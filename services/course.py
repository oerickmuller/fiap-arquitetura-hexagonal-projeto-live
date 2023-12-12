from typing import List

import domain
import ports

class CourseNotFoundException(BaseException):
    pass

class CourseAlreadyExistsException(BaseException):
    pass


class CourseService(ports.CourseService):
    def __init__(self, repo: ports.CourseRepository):
        self._repo = repo

    def get_course(self, course_id):
        course = self._repo.get_course(course_id)
        if not course:
            raise CourseNotFoundException()

    def get_all_courses(self) -> List[domain.Course]:
        return self._repo.get_all_courses()

    def new_course(self, course: domain.Course):
        _c = self._repo.get_course(course.course_id)

        if _c:
            raise CourseAlreadyExistsException()

        self._repo.insert_course(course)
        return course

    def delete_course(self, course: domain.Course) -> bool:
        self._repo.delete_course(course)
        return True
