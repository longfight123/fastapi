from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()



class UserIn(BaseModel):
    name: str
    password: str
    email: EmailStr
    full_name: str | None = None

class UserOut(BaseModel):
    name: str
    email: EmailStr
    full_name: str | None = None

class UserDB(BaseModel):
    name: str
    email: EmailStr
    hashed_password: str
    full_name: str | None = None

def fake_password_hasher(user: UserIn):
    return "supersecret" + user.password

def fake_save_user(user: UserIn):
    hashed_password = fake_password_hasher(user)
    user_in_db = UserDB(**user.dict(), hashed_password=hashed_password)
    print("Saving " + user_in_db.name + " to database")
    return user_in_db

@app.post("/user", response_model=UserOut, response_model_exclude_unset=True)
async def create_user(user: UserIn):
    user_saved = fake_save_user(user)
    return user_saved