from typing import List

import pymongo

import domain

from ports.repositories.student import StudentRepositoryPort
from ports.repositories.course import CourseRepositoryPort


class MongoRepo(CourseRepositoryPort, StudentRepositoryPort):
    def __init__(self):
        self._conn = pymongo.MongoClient(
            host="localhost",
            username="root",
            password="erm"
        )
        self._db = self._conn['ha']

    def get_course(self, course_id) -> domain.Course:
        r = self._db.get_collection("course").find_one({
            "course_id": course_id
        })
        if r:
            return domain.Course(**r)
        return None

    def insert_course(self, course: domain.Course):
        self._db.get_collection("course").insert_one({
            "course_id": course.course_id,
            "name": course.name,
            "is_active": course.is_active
        })
        return course

    def get_all_courses(self) -> List[domain.Course]:
        r = self._db.get_collection("course").find()
        rx = [domain.Course(**data) for data in r]
        return rx

    def delete_course(self, course: domain.Course):
        self._db.get_collection("course").delete_one({'course_id': course.course_id})
        return True

    def insert_student(self, student: domain.Student):
        self._db.get_collection("students").insert_one({
            "student_id": student.student_id,
            "name": student.name,
            "age": student.age
        })

    def get_student(self, student_id: str) -> domain.Student | None:
        r = self._db.get_collection("students").find_one({
            "student_id": student_id,
        })
        if not r:
            return None
        return domain.Student(**r)
