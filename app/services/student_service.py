from datetime import datetime
from typing import List, Optional
from app.models.student import StudentCreate,StudentUpdate,StudentResponse

class StudentService:
    def __init__(self):
        self.students = []
        self.next_id = 1

    def create_student(self,student_data:StudentCreate) -> StudentResponse:
        """Create a New Student"""
        # Check if email already existed
        if(s['email'] == student_data.email for s in self.students):
            raise ValueError("Email Already Existed")
        
        new_student = {
            "id":self.next_id,
            "name":student_data.name,
            "email":student_data.email,
            "age":student_data.age,
            "grade":student_data.grade,
            "subject":student_data.subject,
            "created_at":datetime.now()
        }

        self.students.append(new_student)
        self.next_id+=1

        return StudentResponse(**new_student)