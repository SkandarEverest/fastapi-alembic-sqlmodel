from pydantic import BaseModel


class CategoryRequest(BaseModel):
    name: str


class CategoryResponse(BaseModel):
    id: str
    name: str