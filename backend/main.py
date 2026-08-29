from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

mongo_client = MongoClient("mongodb://admin_user:web3@mongo_container:27017/")
database = mongo_client["desarrollo_web_III"]
productos = database["productos"]

@app.get("/health")
def health_check():
  return {"status": "ok"}

@app.get("/productos")
def get_productos():
  print(productos.find({}, {"_id": 0}))
  return list(productos.find({}, {"_id": 0}))
