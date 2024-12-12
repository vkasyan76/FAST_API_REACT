import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

# fast API can automatically validate data coming in and format data going out based on Pydantic models.

class Fruit (BaseModel):
    name: str

class Fruits(BaseModel):
    fruits: List[Fruit]

app = FastAPI(debug=True)

# when we mov to production, we will need to change the origins to the domain of the frontend

origins = [
    "http://localhost:3000",
    # Add more origins here
]

# CORS = Cross Origin Resource Sharing - prohibits unauthorized websites, endpoints, or servers from accessing your API

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# set-up a database in memory
memory_db = {"fruits": []}

@app.get("/fruits", response_model=Fruits)
def get_fruits():
    return Fruits(fruits=memory_db["fruits"])

@app.post("/fruits")
def add_fruit(fruit: Fruit):
    memory_db["fruits"].append(fruit)
    return fruit

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)