from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
class SBookAdd(BaseModel):
    title:str
    author:str
    year:int
    pages:int
    is_read:bool=False

class SBook(SBookAdd):
    id:int
    from_attributes:bool=True
    



