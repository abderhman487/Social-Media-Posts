from datetime import datetime
from typing import Annotated, Optional
from pydantic import BaseModel , EmailStr, conint


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


class PostResponse(BaseModel):
    title : str
    content : str
    published : bool = True
    id: int
    created_at: datetime
    creator_id: int
    creator: UserResponse
    
    class Config:
        orm_mode = True   

class PostWithVotes(BaseModel):
    Post: PostResponse
    votes: int

    class Config:
        orm_mode = True         


class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id : Optional[int] = None

class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, conint(ge=0, le=1)] 