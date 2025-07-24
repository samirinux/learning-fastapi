# FastAPI Documentation

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

## Features

- Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic).
- Fast to code: Increase the speed to develop features by about 200% to 300%. *
- Fewer bugs: Reduce about 40% of human (developer) induced errors. *
- Intuitive: Great editor support. Completion everywhere. Less time debugging.
- Easy: Designed to be easy to use and learn. Less time reading docs.
- Short: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
- Robust: Get production-ready code. With automatic interactive documentation.

## Installation

To install FastAPI, you can use pip:

```bash
uv add install fastapi
```

You'll also need an ASGI server, such as uvicorn, to run your application:

```bash
uv add install uvicorn
```

## Example Application

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}
```

## Run Application

```bash
uv run uvicorn main:app --host "0.0.0.0" --port 8000 --reload
```

## Parameterizing Endpoints

from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

## POST Requests

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float = None

@app.post("/items/")
async def create_item(item: Item):
    return item
```

