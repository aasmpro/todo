from fastapi import FastAPI

from todo_list import ToDoList

app = FastAPI(version="0.0.0")


@app.get("/", tags=["main"])
async def root():
    return {
        "get": {
            "todo_items": "/api/todo",
            "todo": "/api/todo/{id}",
        },
        "post": {
            "create_todo": "/api/todo",
        },
        "put": {
            "update_todo": "/api/todo/{id}",
        },
    }


@app.get("/api/todo", tags=["todo"])
async def get_todo_items():
    return ToDoList.data


@app.post("/api/todo", tags=["todo"])
async def post_todo_items(todo: ToDoList.input):
    return ToDoList.create(todo)


@app.get("/api/todo/{id}", tags=["todo"])
async def get_todo_item(id: int):
    return ToDoList.get(id)


@app.put("/api/todo/{id}", tags=["todo"])
async def put_todo_item(id: int, todo: ToDoList.input):
    return ToDoList.update(id, todo)


@app.delete("/api/todo/{id}", tags=["todo"])
async def delete_todo_item(id: int):
    return ToDoList.delete(id)
