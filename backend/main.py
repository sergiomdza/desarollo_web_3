import os

from fastapi import FastAPI
from pymongo import MongoClient
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app, endpoint="/metrics")

# Mongo DB connection
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
    return {"message": "SE ACABO LA CLASE"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/productos")
def get_productos():
    return list(productos.find({}, {"_id": 0}))

@app.get("/error_400")
def get_error():
    raise HTTPException(status_code=400, detail="EL ID NO PUEDE SER CERO")
    return []


@app.get("/error_500")
def get_error_500():
    raise HTTPException(status_code=500, detail="ERROR CON LA CONEXION DE LA DB")

@app.get("/logins")
def get_error():
    return [1,2,3,4,5]
