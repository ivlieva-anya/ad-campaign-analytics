
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import  users, sources, router_routes

from backend.core.config import settings

app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем роутеры
app.include_router(router=router_routes, prefix=settings.api_v1_prefix)
@app.get("/")
async def root():
    return {"message": "Welcome to Ad Campaign Analytics API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="localhost", reload=True, port=settings.api_port)