"""
Разработать API для управления списком пользователей с
использованием базы данных SQLite. Для этого создайте
модель User со следующими полями:
    ○ id: int (идентификатор пользователя, генерируется
    автоматически)
    ○ username: str (имя пользователя)
    ○ email: str (электронная почта пользователя)
    ○ password: str (пароль пользователя)
API должно поддерживать следующие операции:
    ○ Получение списка всех пользователей: GET /users/
    ○ Получение информации о конкретном пользователе: GET /users/{user_id}/
    ○ Создание нового пользователя: POST /users/
    ○ Обновление информации о пользователе: PUT /users/{user_id}/
    ○ Удаление пользователя: DELETE /users/{user_id}/
Для валидации данных используйте параметры Field модели User.
Для работы с базой данных используйте SQLAlchemy и модуль databases.

"""
from typing import List

import databases
import sqlalchemy
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, SecretStr

DATABASE_URL = "sqlite:///database_seminar_6.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
    sqlalchemy.Column("password", sqlalchemy.String(16)),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)

app = FastAPI()


class UserWithId(BaseModel):
    id: int = Field(title="Id")
    username: str = Field(title="Username", max_length=32)
    email: EmailStr = Field(title="Email", max_length=128)
    password: str = Field(title="Password", max_length=16)


class User(BaseModel):
    username: str = Field(title="Username", max_length=32)
    email: EmailStr = Field(title="Email", max_length=128)
    password: str = Field(title="Password", max_length=16)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# создание нового user
@app.post("/users/", response_model=UserWithId)
async def create_user(user: User):
    query = users.insert().values(username=user.username, email=user.email, password=user.password)
    # query = users.insert().values(**user.model_dump())
    last_record_id = await database.execute(query)
    return {**user.model_dump(), "id": last_record_id}


# вывод всех user
@app.get("/users/", response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


# вывод user по id
@app.get("/user/{user_id}", response_model=User)
async def read_user_id(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


# создание списка user по указанному кол-ву
@app.get("/temp/{count}")
async def create_user(count: int):
    for i in range(count):
        query = users.insert().values(username=f'username{i}', email=f'mail{i}@mail.ru', password=f'1234')
        await database.execute(query)
    return {'message': f'{count} users create'}


# изменение user по id
@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: User):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}


# удаление user по id
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}

# if __name__ == '__main__':
#     uvicorn.run("main_1:app")
