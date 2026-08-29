import os

from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://admin_user:web3@mongo:27017/")
mongo_client = MongoClient(MONGO_URI)
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