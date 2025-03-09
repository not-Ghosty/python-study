from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()


class UserModel(BaseModel):
    """Model representing a user with a name, phone, and optional city."""

    name: str
    phone: int
    city: str = None


class ResponseModel(BaseModel):
    """Standard response model for API responses."""

    status_code: int = 200
    message: str
    data: Dict


users: List[UserModel] = []


@app.get("/")
def welcome():
    """Returns a welcome message."""
    return "Hello world"


@app.post("/user", status_code=201, response_model=ResponseModel)
def create_user(user: UserModel) -> ResponseModel:
    """Creates a new user and returns a response model."""
    users.append(user)
    return ResponseModel(
        status_code=201,
        message="User created successfully",
        data=user.model_dump(),
    )


@app.get("/user", status_code=200)
def get_user():
    """Returns a list of all users."""
    return users


@app.get("/user/{user_id}", response_model=UserModel)
def get_user_details(user_id: int):
    """Returns details of a specific user by ID."""
    try:
        return users[user_id]
    except IndexError:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
