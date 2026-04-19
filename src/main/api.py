from fastapi import FastAPI

app = FastAPI()

@app.get("/getUsers")
async def get_user():
    return {"user1":"Manish"}

@app.post("/postUserDataToTable")
def create_user(name:str,age,salary):
    return {"Message":"User added successfully"}
