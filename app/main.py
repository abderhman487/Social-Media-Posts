from typing import Optional, List
from fastapi import Body, FastAPI, status ,Response , HTTPException , Depends
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models,schemas
from .database import engine, get_db
from passlib.context import CryptContext

pwd_context = CryptContext(schemes= ["bcrypt"], deprecated= "auto")

models.Base.metadata.create_all(bind=engine)


while True :
    try:
        connection = psycopg2.connect(
        host="localhost",
        database="posts",
        user="abderhman487", 
        password = "password123", 
        cursor_factory=RealDictCursor
        )
        cursor = connection.cursor()
        print("Connection to database succesed")
        break
    except Exception as error:
        print("Connection to database failed")
        print({"Error":error})
        time.sleep(10)     



app = FastAPI(
    title="Posts API",
    description="API for posts management",
    version="1.0.0"
)

       

@app.get("/")
async def root():
    return "Hello to the home page, add /docs for more information"

 

@app.get("/posts",
         response_model = List[schemas.PostResponse]
        )
async def get_all_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts



@app.get("/posts/{id}",
         response_model= schemas.PostResponse
         )
async def get_post(id:int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The post with the id {id} was not found")
    return post


@app.post("/posts", 
          status_code= status.HTTP_201_CREATED,
          response_model=schemas.PostResponse
         )
async def create_post(post:schemas.PostCreate, 
                      db: Session = Depends(get_db)
                      ):
    
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post




@app.delete("/posts/{id}" , status_code= status.HTTP_204_NO_CONTENT)
async def delete_post(id:int, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)

    if post_query.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,
                            detail=f"The post with the id {id} was not found")
    post_query.delete(synchronize_session=False)
    db.commit()
    return post_query.first()



@app.put("/posts/{id}",
         response_model= schemas.PostResponse
        )
async def update_post(id:int,post:schemas.PostCreate , db: Session = Depends(get_db)):
    
    post_query = db.query(models.Post).filter(models.Post.id == id)
    if post_query.first() is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail={"message":f"the post with id {id} is not found"})
    post_query.update(post.model_dump(), synchronize_session=False)
    db.commit()
    return post_query.first()



@app.post("/users",
          status_code=status.HTTP_201_CREATED, 
          response_model= schemas.UserResponse
         )
async def create_user(user : schemas.UserCreate, db: Session = Depends(get_db)):

    hashed_password = pwd_context.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user