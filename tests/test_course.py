from pytest import fixture
import services
import adapters.repositories as repositories
import domain

import uuid

@fixture
def mongo_repo():
     return repositories.MongoRepo()


def test_list_courses(mongo_repo):
    course_svc = services.CourseService(mongo_repo)
    all_courses = course_svc.get_all_courses()
    assert len(all_courses) > 0

# def test_new_course(mongo_repo):
#     course_svc = services.CourseService(mongo_repo)
#     new_course_id = str(uuid.uuid4())
#     new_course = domain.Course(
#         course_id=new_course_id,
#         name="Test Course",
#         is_active=True
#     )
#     created_course = course_svc.new_course(new_course)
#     assert (created_course.course_id == new_course.course_id) and (created_course.name == new_course.name) and \
#            (created_course.is_active == new_course.is_active)
#
#     course_from_repo = course_svc.get_course(new_course_id)
#     assert (new_course.course_id == course_from_repo.course_id) and \
#            (new_course.name == course_from_repo.name) and \
#            (new_course.is_active == course_from_repo.is_active)
#
#     course_svc.delete_course(new_course)