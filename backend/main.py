from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app, endpoint="/metrics")

# Mongo DB connection
mongo_client = MongoClient("mongodb://admin:web3@mongo-service.default.svc.cluster.local:27017/")
database = mongo_client["desarrollo_web_3"]
productos = database["productos"]

@app.get("/")
def default():
    return {"message": "Si funciona"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/productos")
def get_productos():
    return list(productos.find({}, {"_id": 0}))

@app.get("/error_400")
def get_error():
    raise HTTPException(status_code=400, detail="El id no puede ser cero")
    return []

@app.get("/error_500")
def get_error():
    raise HTTPException(status_code=500, detail="Error en la conexión a la DB")
    return[]

@app.get("/logins")
def get_error():
    return [1,2,3,4,5]