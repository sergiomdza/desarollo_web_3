import os
import time

from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app, endpoint="/metrics")

mongo_uri = os.getenv("MONGO_URI")
if mongo_uri:
    mongo_client = MongoClient(mongo_uri)
else:
    mongo_username = os.getenv("MONGO_USERNAME")
    mongo_options = {}
    if mongo_username:
        mongo_options = {
            "username": mongo_username,
            "password": os.getenv("MONGO_PASSWORD"),
            "authSource": "admin",
        }
    mongo_client = MongoClient(os.getenv("MONGO_HOST", "localhost"), **mongo_options)

database = mongo_client["desarrollo_web_3"]
productos = database["productos"]


@app.get("/")
def default():
    return {"message": "HOLA MUNDO!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/productos")
def get_productos():
    return list(productos.find({}, {"_id": 0}))


@app.get("/error_400")
def get_error_400():
    raise HTTPException(status_code=400, detail="El ID no puede ser cero")


@app.get("/error_500")
def get_error_500():
    raise HTTPException(status_code=500, detail="Error en la conexión a la DB")


@app.get("/logins")
def get_logins():
    return [1, 2, 3, 4, 5]


@app.get("/wait")
def get_wait():
    time.sleep(3)
    return "Respuesta despues de 3 segundos"
