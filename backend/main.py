from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()
mongo_client = MongoClient("mongodb://admin_user:web3@mongo_container:27017/")
database = mongo_client["WEB3"]
productos = database["Productos"]

@app.get("/health")
def health_check():
  return {"status": "ok"} 

@app.get("/")
def default():
  return {"message": "Corriendo"}

@app.get("/productos")
def get_productos():
  return list(productos.find({}, {"_id": 0}))  