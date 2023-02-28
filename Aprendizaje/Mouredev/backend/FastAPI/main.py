# Importamos la librería FastAPI
from fastapi import FastAPI

# Creamos una instancia de FastAPI
app = FastAPI()

# Creamos una ruta raíz con el get que es el método HTTP de la petición
# Creamos una función que devuelva "¡Hola FastAPI!"


@app.get("/")
async def root():
    return "¡Hola FastAPI!"

# uvicorn main:app --reload
# Es el comando para ejecutar el servidor de FastAPI
# El servidor se despliega en una ip local y un puerto
# http://127.0.0.1:8000


# Creamos una ruta con el get que es el método HTTP de la petición
# En este caso la ruta es /url
@app.get("/url")
async def url():
    return {"url": "https://mouredev.com/python"}
# http://127.0.0.1:8000/url


# http://127.0.0.1:8000/docs
# Si ponemos /docs, nos muestra la documentación de la API

# http://127.0.0.1:8000/redoc
# Es otra forma de ver la documentación de la API

# ctrl + c para parar el servidor

# Postman:
# Es una herramienta para hacer peticiones HTTP

# Thunder Client:
# Es una extensión de VS Code para hacer peticiones HTTP


# Tipos de métodos HTTP:
# POST: Para crear datos
# GET: Para leer datos
# PUT: Para actualizar datos
# DELETE: Para eliminar datos

# Documentación de FastAPI:
# https://fastapi.tiangolo.com/es/
