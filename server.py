from fastapi import FastAPI

app = FastAPI()

users = []


@app.get("/")
def welcome():
    return "Hello world"


@app.post("/user/{name}", status_code=201)
def create_user(name: str):
    if not name:
        raise Exception()

    users.append(name)
    return users

@app.get('/user',status_code=200)
def get_user():
    return users
