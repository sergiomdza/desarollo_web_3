from fastapi import FastAPI
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
    return {"message": "SE ACABO LA CLASE"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/productos")
def get_productos():
    return list(productos.find({}, {"_id": 0}))