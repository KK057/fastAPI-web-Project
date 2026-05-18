from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field

class UserBase():
    pass

class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=30)
    content: str = Field(min_length=1,max_length=300)
    author: str = Field(min_length=1,max_length=50)

class PostCreate(PostBase):
    pass 

class PostResponse(PostBase):
    model_config=ConfigDict(from_attributes=True)
    id: int
    date_posted: str