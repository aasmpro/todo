from pydantic import BaseModel

from database import Database

Database.read()


class ToDoInput(BaseModel):
    title: str
    desc: str


class ToDoOutput(ToDoInput):
    id: int


class ToDoList:
    data = Database.data.get("todo", [])
    input = ToDoInput
    output = ToDoOutput

    @staticmethod
    def save():
        Database.data["todo"] = ToDoList.data
        Database.write()

    @staticmethod
    def get_new_id():
        try:
            return ToDoList.data[-1]["id"] + 1
        except IndexError:
            return 1

    @staticmethod
    def create(todo: ToDoInput):
        id = ToDoList.get_new_id()
        data = {"id": id, **todo.dict()}
        ToDoList.data.append(data)
        ToDoList.save()
        return data

    @staticmethod
    def get_index(id: int):
        for index, todo in enumerate(ToDoList.data):
            if todo["id"] == id:
                return index
        return None

    @staticmethod
    def get(id: int):
        index = ToDoList.get_index(id)
        if index:
            return ToDoList.data[index]
        return {}

    @staticmethod
    def update(id: int, todo: ToDoInput):
        index = ToDoList.get_index(id)
        if index:
            old_todo = ToDoList.data[index]
            new_todo = {**old_todo, **todo.dict()}
            ToDoList.data[index] = new_todo
            ToDoList.save()
            return new_todo
        return {}

    @staticmethod
    def delete(id: int):
        index = ToDoList.get_index(id)
        if index:
            todo = ToDoList.data.pop(index)
            ToDoList.save()
            return todo
        return {}
