from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

# Mongo DB connection setup
mongo_client = MongoClient("mongodb://admin_user:web3@mongo_container:27017/")
database = mongo_client["desarrollo_web_3"]
productos = database["productos"]

@app.get("/")
def default_route():
  return {"message": "Uvicorn server is running!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/productos")
def get_productos():
    productos_list = list(productos.find({}))  # Exclude the _id field from the results
    return {"productos": productos_list}

