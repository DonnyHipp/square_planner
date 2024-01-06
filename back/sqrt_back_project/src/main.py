from fastapi import FastAPI

from api.auth.router import router as authrouter
from api.tasks.router import router as taskrouter

app = FastAPI(title='SQRTapp')

routes = [
    authrouter,
    taskrouter
]

for rout in routes:
    app.include_router(rout)