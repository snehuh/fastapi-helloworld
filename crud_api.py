from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# create an in-memory database
items = {}
next_id = 1

# import a base model  (Qn: What is a base model? Ans: A foundation class used for creating data structure with strict input validation)

class Item(BaseModel):
    id: int | None = None
    name: str
    price: float

@app.get("/")
def root():
    return{"message":"Hello World!"}

@app.post("/items", status_code=201)
def create_item(item: Item):
    global next_id
    item.id = next_id
    items[next_id] = item
    next_id += 1
    return item

@app.get("/list-items")
def get_items(items):
    return items