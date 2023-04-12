from typing import List, Optional

from pydantic import BaseModel


class PersonBase(BaseModel):
    id: int
    name: str
    age: str
    city: str

class PersonCreate(PersonBase):
    pass

class Person(PersonBase):
    id: int

    class Config:
        orm_mode = True
