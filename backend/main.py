from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

# mongo db connection
mongo_client = MongoClient("mongodb://admin_user:web3@mongo:27017/")
database = mongo_client["desarrollo_web_3"]
productos = database["productos"]

@app.get("/")
def default():
    return {"message":"Uvicorn server running"}

@app.get("/health")
def health_check():
    return {"Status":"Estoy malito nene"}

@app.get("/productos")
def get_products():
    return list(productos.find({}, {"_id": 0}))