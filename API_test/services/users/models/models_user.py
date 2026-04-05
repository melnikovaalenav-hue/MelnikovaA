from pydantic import BaseModel
from uuid import UUID
from typing import Optional, List


class Category(BaseModel):
    id: int
    name: str

class Tag(BaseModel):
    id: int
    name: str

class UserResponse(BaseModel):
    id: int
    category: Category
    name: str
    photoUrls: List[str]
    tags: List[Tag]
    status: str

