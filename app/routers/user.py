from fastapi import FastAPI, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import schemas, models, utils
from ..database import get_db

router = APIRouter(
    prefix= "/users",
    tags=["Users"]
)

@router.post("/",
          status_code=status.HTTP_201_CREATED, 
          response_model= schemas.UserResponse
         )
async def create_user(user : schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        hashed_password = utils.hash(user.password)
        user.password = hashed_password

        new_user = models.User(**user.model_dump())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except: 
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,
                            detail= {"message":f"the email is already exist"})

@router.get("/{id}",
         response_model= schemas.UserResponse)
async def get_user(id:int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail= {"message":f"the user with id {id} is not found"})
    
    return user