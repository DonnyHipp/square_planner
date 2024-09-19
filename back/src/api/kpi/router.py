from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/task")


class TestBody(BaseModel):
    s: str


@router.post("")
def get_task(body: TestBody):
    print(body.s)
    return body.s
