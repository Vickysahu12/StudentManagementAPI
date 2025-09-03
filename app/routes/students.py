from fastapi import APIRouter,HTTPException,Query,Path,status
from typing import Optional
from app.models.student import StudentCreate,StudentUpdate,StudentResponse,StudentListResponse
from app.services.student_service import student_service

router = APIRouter(
    prefix="api/v1/student",
    tags=["student"],
    responses={404:{"description":"Not found"}}
)

@router.post("/",
             response_model=StudentResponse,
             status_code=status.HTTP_201_CREATED,
             summary="Create New Students",
             description="Create a New Student with all the required information")
async def create_student(student:StudentCreate):
    """Create a New student in the system"""
    try:
        return student_service.create_student(student)
    except ValueError as e:
        raise HTTPException(status_code=404,detail=str(e))
    
@router.get("/",
            response_model=StudentResponse,
            summary="Get All Student",
            description="Retrieve all student with pagination and search")
async def get_student(
    skip: int = Query(0,ge=0,description="Numbers of Record to skip"),
    limit: int = Query(10,ge=1,le=100,description="Numbers of record to Fetch"),
    search: Optional[str] = Query(None,max_length=50,description="Search by name or email")
):
    """Get all student with optional search with pagination"""
    result = student_service.get_all_students(skip=skip,limit=limit,search=search)
    return StudentListResponse(**result)

@router.get("/{student_id}",
            response_model=StudentResponse,
            summary="Get a Single Student By Id",
            description="Retrive a specific student By their Id")
async def get_students(student_id:int = Path(...,gt=0,description="student id must be a positve number")):
    """Get a specific student By their Id"""
    student = student_service.get_student_by_id(student_id)
    if not student:
        raise HTTPException(
            status_code=404,
            detail=f"student with {student_id} Not Found"
        )
    return student

@router.put("/{student_id}",
            response_model=StudentResponse,
            summary="Update Student",
            description="Update all the students By ID")
async def update_student(
    student_update:StudentUpdate,
    student_id: int = Path(...,gt=0,description="student id must be positive")
):
    """Update Student Information"""
    try:
        updated_student = student_service.update_student(student_id,student_update)
        if not updated_student:
            raise HTTPException(
                status_code=404,
                detail=f"student with {student_id} Not Found"
            )
        return updated_student
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))
    
@router.delete("/{student_id}",
               response_model=StudentResponse,
               summary="Delete Student",
               description="Delete a student from the system")
async def delete_student(student_id:int = Path(...,ge=0,description="Student ID must be positive")):
    """Delete Student"""
    success = student_service.delete_student(student_id)
    if not success:
        raise HTTPException(
            status_code=404,
            detail=f"studnt with {student_id} Not Found"
        )
    return{"message":"Student Deleted SuccesFully"}