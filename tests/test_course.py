from pytest import fixture
import services
import adapters.repositories as repositories
from domain.course import Course

import uuid


@fixture
def mongo_repo():
    repo = repositories.MongoRepo()
    repo._db.get_collection('course').delete_many({})
    return repo


def test_list_courses(mongo_repo):
    course_01 = Course(course_id=str(uuid.uuid4()), name="Curso 01", is_active=True)
    course_02 = Course(course_id=str(uuid.uuid4()), name="Curso 02", is_active=False)
    course_svc = services.CourseService(mongo_repo)
    course_svc.new_course(course_01)
    course_svc.new_course(course_02)
    all_courses = course_svc.get_all_courses()
    assert len(all_courses) > 0


def test_new_course(mongo_repo):
    course_svc = services.CourseService(mongo_repo)
    new_course_id = str(uuid.uuid4())
    new_course = Course(
        course_id=new_course_id,
        name="Test Course",
        is_active=True
    )
    created_course = course_svc.new_course(new_course)
    assert (created_course.course_id == new_course.course_id) and (created_course.name == new_course.name) and \
           (created_course.is_active == new_course.is_active)

    course_from_repo = course_svc.get_course(new_course_id)
    assert (new_course.course_id == course_from_repo.course_id) and \
           (new_course.name == course_from_repo.name) and \
           (new_course.is_active == course_from_repo.is_active)

    course_svc.delete_course(new_course)
