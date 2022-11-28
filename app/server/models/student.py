from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class StudentSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(..., gt=0, lt=9)
    gpa: float = Field(..., le=4.0)

    class Config:
        schema_extra = {
            'example': {
                'fullname': 'Pham Ba Vu',
                'email': 'phambavu@gmail.com',
                'course_of_study': 'software engineer',
                'year': 3,
                'gpa': 3.0
            }
        }


class UpdateStudentSchema(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    course_of_study: Optional[str]
    year: Optional[int]
    gpa: Optional[float]

    class Config:
        extra_schema = {
            'example': {
                'fullname': 'Pham Ba Vu',
                'email': 'phambavu@gmail.com',
                'course_of_study': 'software',
                'year': 3,
                'gpa': 3.0
            }
        }


def ResponseModel(data, message):
    return {
        'data': [data],
        'code': 200,
        'message': message
    }


def ErrorResponseModel(error, code, message):
    return {
        'error': error,
        'code': code,
        'message': message
    }
