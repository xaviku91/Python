from fastapi import FastAPI
from pydantic import BaseModel

# Iniciamos el servidor con:
# uvicorn users:app --reload

app = FastAPI()

# Estructura de datos de entrada de usuarios
# No sería lo más optimo, pero es para ver como funciona


@app.get("/usersjson")
async def usersjson():
    return [{"Nombre": "Xavi", "Apellido": "Quesada", "Edad": 30, "Email": "xaviku@gmail.com"}, {"Nombre": "Antonio", "Apellido": "Soler", "Edad": 52, "Email": "antonio@gmail.com"}, {"Nombre": "Pepa", "Apellido": "Perez", "Edad": 25, "Email": "pepa@gmail.com"}]

# Arrancar servidor: uvicorn users:app --reload
# URL SERVIDOR: http://127.0.0.1:8000/users

# Estructura de datos de entrada de usuarios
# Esto sería más optimo, que lo que hemos hecho antes


class User(BaseModel):
    id: int
    nombre: str
    apellido: str
    edad: int
    email: str

# Primera manera de crear un usuario con FastAPI


@app.get("/usersclass")
async def usersclass():
    return User(nombre="Xavi", apellido="Quesada", edad=30, email="xaviku@gmail.com")

# Segunda manera de crear un usuario con FastAPI
usuarios_listado = [
    User(id=1, nombre="Xavi", apellido="Quesada",
         edad=30, email="xaviku@gmail.com"),
    User(id=2, nombre="Antonio", apellido="Soler",
         edad=52, email="antonio@gmail.com"),
    User(id=3, nombre="Pepa", apellido="Perez", edad=25, email="pepa@gmail.com")
]


@app.get("/usuarios")
async def usuarios():
    return usuarios_listado

# Buscar usuario por ID

'''
@app.get("/user/{id}")
async def user(id: int):
    users = filter(lambda user: user.id == id, usuarios_listado)
    return list(users)[0]
'''

# El problema de esto es que si ponemos por ejemplo un id 4 el servidor se rompe,

# Para solucionarlo, tenemos que hacer lo siguiente:


@app.get("/user/{id}")
async def user(id: int):
    users = filter(lambda user: user.id == id, usuarios_listado)
    try:
        return list(users)[0]
    except:
        return {"error": "Usuario no encontrado"}
