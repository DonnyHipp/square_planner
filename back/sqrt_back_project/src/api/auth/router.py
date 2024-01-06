from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Request


router = APIRouter(prefix='/user')


@router.get("/test")
def get_payments():
    return "my payments...."