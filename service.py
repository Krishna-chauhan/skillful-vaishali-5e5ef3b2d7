from sqlalchemy.orm import Session, aliased
from database import SessionLocal
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
from datetime import datetime
import requests
import math
import random
import asyncio
from pathlib import Path


def convert_to_datetime(date_string):
    if date_string is None:
        return datetime.now()
    from fastapi import HTTPException

    if "T" in date_string:
        try:
            return datetime.fromisoformat(date_string.replace("Z", "+00:00"))
        except ValueError:
            date_part = date_string.split("T")[0]
            try:
                return datetime.strptime(date_part, "%Y-%m-%d")
            except ValueError:
                raise HTTPException(
                    status_code=422,
                    detail=f"Improper format in datetime: {date_string}",
                )
    else:
        try:
            return datetime.strptime(date_string, "%Y-%m-%d")
        except ValueError:
            raise HTTPException(
                status_code=422, detail=f"Improper format in datetime: {date_string}"
            )


async def get_get_one(request: Request, db: Session):
    res = {
        "status": 200,
        "message": "The request has been successfully processed",
        "data": {},
    }
    return res


async def post_post_one(request: Request, db: Session):
    res = {}
    return res


async def post_post_two(request: Request, db: Session):
    header_koala: str = request.headers.get("header-koala")

    header_panda: str = request.headers.get("header-panda")

    res = {
        "status": 200,
        "message": "The request has been successfully processed",
        "data": {},
    }
    return res


async def get_get_two(request: Request, db: Session):
    header_tiger: str = request.headers.get("header-tiger")

    header_leopard: str = request.headers.get("header-leopard")

    res = {
        "status": 200,
        "message": "The request has been successfully processed",
        "data": {},
    }
    return res
