import domain
import ports


class StudentAlreadyExistentException(BaseException):
    pass


class StudentService(ports.StudentService):
    def __init__(self, repo):
        self._repo = repo

    def new_student(self, student: domain.Student):
        if self.get_student(student.student_id):
            raise StudentAlreadyExistentException("student already registered")

        self._repo.insert_student(student)
        return student

    def get_student(self, student_id: str):
        return self._repo.get_student(student_id)
