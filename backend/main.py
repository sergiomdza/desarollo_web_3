from fastapi import FastAPI, HTTPException, status
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

@app.get("/error_400")
def error_400():
  raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error 400")

@app.get("/error_500")
def error_500():
  raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error 500")
