from fastapi import FastAPI
import uvicorn
from app.api.endpoints.todo import todo_router

app = FastAPI()

app.include_router(todo_router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)