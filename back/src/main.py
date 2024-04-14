from fastapi import FastAPI

from src.api.auth.router import router as authrouter
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
    "http://localhost:5173",
]

app = FastAPI(title="PDCA")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


routes = [
    authrouter,
]
for rout in routes:
    app.include_router(rout)
