from datetime import datetime
from typing import List, Optional
from app.models.student import StudentCreate, StudentUpdate, StudentResponse

class StudentService:
    def __init__(self):
        self.students = []
        self.next_id = 1

    def create_student(self, student_data: StudentCreate) -> StudentResponse:
        """Create a New Student"""
        # ✅ FIX: Correct email uniqueness check
        if any(s['email'] == student_data.email for s in self.students):
            raise ValueError("Email Already Existed")
        
        new_student = {
            "id": self.next_id,
            "name": student_data.name,
            "email": student_data.email,
            "age": student_data.age,
            "grade": student_data.grade,
            "subject": student_data.subject,
            "created_at": datetime.now()
        }

        self.students.append(new_student)
        self.next_id += 1

        return StudentResponse(**new_student)
    
    def get_all_students(self, skip: int = 0, limit: int = 10, search: Optional[str] = None) -> dict:
        """Get all Students with pagination and search"""
        filtered_students = self.students

        # ✅ FIX: Correct search functionality
        if search:
            search_lower = search.lower()
            filtered_students = [
                s for s in self.students
                if search_lower in s['name'].lower() or search_lower in s['email'].lower()
            ]

        # ✅ FIX: Pagination should work outside `if search`
        total = len(filtered_students)
        paginated_students = filtered_students[skip:skip+limit]

        return {
            "total": total,
            "students": [StudentResponse(**s) for s in paginated_students],
            "page": (skip // limit) + 1 if limit else 1,
            "limit": limit
        }
    
    def get_student_by_id(self, student_id: int) -> Optional[StudentResponse]:
        """Get Student By Id"""
        for student in self.students:
            if student["id"] == student_id:
                return StudentResponse(**student)
        return None
            
    def update_student(self, student_id: int, update_data: StudentUpdate) -> Optional[StudentResponse]:
        """Update Student"""
        for i, student in enumerate(self.students):
            if student["id"] == student_id:
                update_dict = update_data.model_dump(exclude_unset=True)

                # ✅ FIX: Check email uniqueness properly
                if "email" in update_dict:
                    if any(s["email"] == update_dict["email"] and s["id"] != student_id for s in self.students):
                        raise ValueError("Email already exists")
                        
                self.students[i].update(update_dict)
                return StudentResponse(**self.students[i])
        return None
                
    def delete_student(self, student_id: int) -> bool:
        """Delete Student"""
        for i, student in enumerate(self.students):
            if student['id'] == student_id:
                self.students.pop(i)
                return True
        return False

# Global service instance
student_service = StudentService()
