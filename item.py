from pydantic import BaseModel
class Item(BaseModel):
    text:str
    offset:int
    mode:str