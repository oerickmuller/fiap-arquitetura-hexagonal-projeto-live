from pydantic import BaseModel

class Student(BaseModel):
    student_id: str
    age: int
    name: str