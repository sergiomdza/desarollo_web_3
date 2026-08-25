from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

mongo_client = MongoClient("mongodb://admin_user:web3@localhost:27017/")
database = mongo_client["desarrollo_web_3"]
productos = database["productos"]

@app.get("/")
def default():
    return {"message": "Uvicorn is running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/productos")
def get_productos():
    return list(productos.find({}, {"_id": 0}))