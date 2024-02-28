from enum import Enum
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Request


router = APIRouter(prefix="/user")
