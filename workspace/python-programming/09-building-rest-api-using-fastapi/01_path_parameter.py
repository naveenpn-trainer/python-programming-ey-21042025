from enum import Enum
from typing import Optional
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    task:str
    status:str

fake_todos = [
    {"id": 1, "task": "Learning Fast API", "status": "IN_PROGRESS"},
    {"id": 2, "task": "Learning FAKE API", "status": "IN_PROGRESS"}
]

@app.get("/test")
def test_api():
    return {"message": "Test API"}

@app.get("/todos/")
def get_all_todos():
    return fake_todos

@app.get("/todos/{todo_id}")
def get_to_do_by_id(todo_id):
    return {"message":f"Fetching todo with id: {todo_id}"}

class TodoStatus(str,Enum):
    pending="pending"
    in_progress="in_progress"
    completed="completed"


@app.get("/todos")
def get_todos(status:TodoStatus,
              limit:Optional[int]=10):
    if status == TodoStatus.pending:
        return {
            "status":status,
            "limit":limit,
            "message":"Returning todos with query parameters"
        }
    elif status == TodoStatus.completed:
        return {
            "status":status,
            "limit":limit,
            "message":"Returning todos with query parameters"
        }
    return None


@app.post("/todos")
def create_todo(todo:Todo):
    return {"message":"Todo created","todo":todo}


if __name__ == '__main__':
    uvicorn.run("01_path_parameter:app",
                host="127.0.0.1",
                port=8001,
                reload=True
                )
