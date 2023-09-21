from fastapi import FastAPI


app = FastAPI()

users = [
    {"id":1,"name":'John','password':1234},
    {"id":2,"name":'Tom','password':24561},
    {"id":3,"name":'Igor','password':1201834}
]

@app.get("/")
def helllo():
    return "HI"


@app.get("/users/")
def helllo(chip:int = 0 ,crp:int = 3):
    return users[chip:][:crp]

@app.get("/users/{id}")
def helllo(id:int):
    return [user for user in users if user.get("id") == id]

@app.post("/users/{id}")
def helllo(id:int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == id, users))[0]
    current_user["name"]  = new_name
    return {"status":200, "data":current_user}