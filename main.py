from fastapi import FastAPI
from fastapi import HTTPException


shapes = [
    {"item_name": "Circle", "no_of_sides": 1, "id": 1},
    {"item_name": "Square", "no_of_sides": 4, "id": 2},
    {"item_name": "Triangle", "no_of_sides": 3, "id": 3},
    {"item_name": "Rectangle", "no_of_sides": 4, "id": 4},
    {"item_name": "Pentagon", "no_of_sides": 5, "id": 5},
    {"item_name": "Hexagon", "no_of_sides": 6, "id": 6},
    {"item_name": "Heptagon", "no_of_sides": 7, "id": 7},
    {"item_name": "Octagon", "no_of_sides": 8, "id": 8}
]
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get("/shapes")
async def get_shapes():
    return shapes

@app.get("/shapes/{shape_id}")
async def get_shape(shape_id: int):
    for shape in shapes:
        if shape["id"] == shape_id:
            return shape
    # return {"error": "Shape not found"}
    raise HTTPException(status_code=404, detail="Shape not found")
