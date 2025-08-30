from pydantic import BaseModel, Field, EmailStr
from typing import Optional,List
from datetime import datetime


class StudentCreate(BaseModel):
    name:str = Field(..., min_length=3, max_length=50, description="Student Name")
    email:str = Field(...,description="Valid email address")
    age:int = Field(...,ge=5, le=25 , description="Student age Between 5-25")
    grade:str = Field(...,description="grade level (1-12 or college)")
    subject:Optional[List[str]] = Field(default=[], description="List Of Subject")

class StudentUpdate(BaseModel):
    name:Optional[str] = Field(None, min_length=5, max_length=50)
    email:Optional[str] = None
    age:Optional[int] = Field(None,ge=5,le=25)
    grade:Optional[str] = None
    subject:Optional[List[str]] = None

class StudentResponse(BaseModel):
    id:int
    name:str
    email:str
    age:int
    grade:str
    subject:List[str]
    created_at:datetime

    class config:
        from_attributes = True


class StudentListResponse(BaseModel):
    total:int
    students:List[StudentResponse]
    page:int
    Limit:int