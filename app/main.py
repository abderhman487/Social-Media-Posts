from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote

models.Base.metadata.create_all(bind=engine)
   
app = FastAPI(
    title="Posts API",
    description="API for posts management",
    version="1.0.0"
)

app.include_router(post.router)       
app.include_router(user.router)       
app.include_router(auth.router)       
app.include_router(vote.router)       

@app.get("/")
async def root():
    return "Hello to the home page, add /docs for more information"
