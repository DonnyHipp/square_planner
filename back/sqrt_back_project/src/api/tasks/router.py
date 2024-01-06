from fastapi import APIRouter

router = APIRouter(prefix='/task')

@router.get("")
def get_task():
    return 1

# create_engine('postgresql+asyncpg://user:password@host:port/name')
