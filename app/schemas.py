from datetime import datetime
from typing import Optional
from pydantic import BaseModel , EmailStr


class UserCreate(BaseModel):
    email : EmailStr
    password : str         

class UserResponse(BaseModel):
    id : int
    email : EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True    

class UserLogin(BaseModel):
    email : EmailStr
    password : str 



class PostBase(BaseModel):
    title : str
    content : str
    published : bool = True
    

class PostCreate(PostBase):
    pass    


class PostResponse(PostBase):
    id: int
    created_at: datetime
    creator_id: int
    creator: UserResponse
    
    class Config:
        orm_mode = True    




class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id : Optional[int] = None