from fastapi import FastAPI
from app.routers import endpoints
from app.routers.auth import router as auth_router

app = FastAPI()
app.include_router(endpoints.router)
app.include_router(auth_router)