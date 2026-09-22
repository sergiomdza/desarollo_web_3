from fastapi import FastAPI
from pymongo import MongoClient
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

Instrumentator().instrument(app).expose(app, endpoint="/metrics")

mongo_client = MongoClient("mongodb://admin_user:dfjkdfjk_2@mongo-service.default.svc.cluster.local:27017/")
database = mongo_client["desarrollo_web_3"]
productos = database["productos"]

@app.get("/")
def default():
    return {"status": "Uvicorn server running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/productos")
def get_productos():
    return list(productos.find({}, {"_id": 0}))