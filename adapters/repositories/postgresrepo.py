from typing import List

import domain
import ports

class PostgresRepo(ports.CourseRepository):
    def insert_course(self, course: domain.Course):
        super().insert_course(course)

    def get_all_courses(self) -> List[domain.Course]:
        return super().get_all_courses()

    def delete_course(self, course: domain.Course) -> bool:
        return super().delete_course(course)

    def get_course(self, course_id) -> domain.Course:
        return []
