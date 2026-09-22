from fastapi import FastAPI
from pymongo import MongoClient
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app, endpoint="/metrics")

mongo_client = MongoClient("mongodb://admin:web3@mongo-service.default.svc.cluster.local:27017/")
database = mongo_client["desarrollo_web_III"]
productos = database["productos"]

@app.get("/health")
def health_check():
  return {"status": "ok"}

@app.get("/productos")
def get_productos():
  print(productos.find({}, {"_id": 0}))
  return list(productos.find({}))
