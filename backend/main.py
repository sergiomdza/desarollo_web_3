from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

# MongoDB connection
mongo_client = MongoClient("mongodb://admin_user:web3@localhost:27017/")
database = mongo_client["desarrollo_web_3"]
productos = database["productos"]

@app.get("/")
def read_root():
    return {"message": "Toma pinga putita"}

@app.get("/productos")
def get_productos():
    productos_list = list(productos.find({}, {"_id": 0}))  # Exclude the _id field
    return {"productos": productos_list}

@app.get("/health")
def health_check():
    return {"status": "ok"}