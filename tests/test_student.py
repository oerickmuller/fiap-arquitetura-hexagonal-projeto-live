import pytest

from adapters import repositories

import services
import domain
from services import StudentAlreadyExistentException


@pytest.fixture
def mongo_repo():
    return repositories.MongoRepo()


def test_create_student(mongo_repo):
    student_svc = services.StudentService(mongo_repo)
    student = domain.Student(
        student_id="1234",
        name="Erick",
        age=43,
    )
    new_student = student_svc.new_student(student)
    assert student.student_id == new_student.student_id
    student_svc.delete_student(student)


def test_create_same_student(mongo_repo):
    student_svc = services.StudentService(mongo_repo)
    student = domain.Student(
        student_id="999",
        name="Erick",
        age=43,
    )
    new_student = student_svc.new_student(student)
    assert student.student_id == new_student.student_id

    with pytest.raises(StudentAlreadyExistentException):
        _ = student_svc.new_student(student)
