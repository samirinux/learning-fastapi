from fastapi import FastAPI
from fastapi import HTTPException
from mongita import MongitaClientDisk
from pydantic import BaseModel


class Shape(BaseModel):
    id: int
    type: str
    no_of_sides: int


app = FastAPI()

client = MongitaClientDisk()
db = client.db
shapes = db.shapes
# shapes.insert_one({"id": 1, "type": "circle", "no_of_sides": 1})

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get("/shapes")
async def get_shapes():
    available_shapes = shapes.find({})
    return [
        {key: shape[key] for key in shape if key != "_id"}
        for shape in available_shapes
    ]

@app.get("/shapes/{shape_id}")
async def get_shape(shape_id: int):
    if shapes.count_documents({"id": shape_id}) > 0:
        shape = shapes.find_one({"id": shape_id})
        return {key: shape[key] for key in shape if key != "_id"}
    # return {"error": "Shape not found"}
    raise HTTPException(status_code=404, detail="Shape not found")

@app.post("/shapes")
async def create_shape(shape: Shape):
    if shapes.find_one({"id": shape.id}):
        raise HTTPException(status_code=400, detail="Shape with this ID already exists")
    shapes.insert_one(shape.dict())
    return shape
