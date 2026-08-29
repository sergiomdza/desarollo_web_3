from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

# MONGO DB connection
mongo_client = MongoClient ("mongodb://admin_user:web3@mongo:27017/")
database = mongo_client["desarrollo_web_3"]
productos = database["Productos"]

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/")
def default():
    return {"message": "uvicorn server running"}

@app.get("/productos")
def get_productos():
    return list(productos.find({}, {"_id": 0})) 
