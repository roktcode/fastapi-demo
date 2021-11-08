from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException

from models import Gender, Role, User, UserUpdateRequst

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("209ea1e8-f73f-41d9-80db-b95c2dae5804"),
        first_name="Jamila",
        last_name="Ahmad",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=UUID("858816ef-7e0d-4ba9-9fa1-dd57cec2a40d"),
        first_name="Aliaa",
        last_name="Yasser",
        gender=Gender.female,
        roles=[Role.admin, Role.user]
    )
]


@app.get("/")
async def root():
    return {"Hello": "Mundo"}


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
	for user in db:
		if user.id == user_id:
			db.remove(user)
			return
	raise HTTPException(
		status_code=404,
		detail=f"User with id: {user_id} doesn't exist."
	)

@app.put("/api/v1/users/{user_id}")
def update_user(user_update: UserUpdateRequst, user_id: UUID):
	for user in db:
		if user.id == user_id:
			if user_update.first_name is not None:
				user.first_name = user_update.first_name
			if user_update.last_name is not None:
				user.last_name = user_update.last_name
			if user_update.middle_name is not None:
				user.middle_name = user_update.middle_name
			if user_update.roles is not None:
				user.roles = user_update.roles
			return
	raise HTTPException(
		status_code=404,
		detail=f"User with id: {user_id} doesn't exist."
		)