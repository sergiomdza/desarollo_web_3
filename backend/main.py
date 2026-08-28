from fastapi import FastAPI
from pymongo import MongoClient

mongo_client = MongoClient("mongodb://admin_user:web3@localhost:27017/")
database = mongo_client["WEB3"]
productos = database["PRODUCTOS"]

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/productos")
def get_productos():
    return list(productos.find({}, {"_id": 0}))
