from fastapi import FastAPI
from pymongo import MongoClient


app = FastAPI()

# Mongo DB connection
mongo_client = MongoClient("mongodb://admin_user:web3@mongo_container:27017/")
database = mongo_client ["Web3"]
productos = database["products"]

@app.get("/")
def default_route():
    return {"message": "Uvicorn is running!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/productos")
def get_productos():
    return list(productos.find({}, {"_id": 0}))