from pydantic import BaseModel


class Course(BaseModel):
    course_id: str
    name: str
    is_active: bool
