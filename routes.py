from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine
from middleware.application_middleware import default_dependency
models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/get_one')
async def get_get_one(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.get_get_one(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/post_one')
async def post_post_one(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.post_post_one(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/post_two')
async def post_post_two(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.post_post_two(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/get_two')
async def get_get_two(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.get_get_two(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

