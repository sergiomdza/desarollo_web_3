from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

# Mongo DB connection
mongo_client = MongoClient(
  "mongodb://admin:web3@mongo-service:27017/?authSource=admin"
)
database = mongo_client["desarrollo_web_3"]
productos = database["productos"]

@app.get("/")
def default():
  return {"message": "Uvicorn server running"}

@app.get("/health")
def health_check():
  return {"status": "ok"}

@app.get("/productos")
def get_productos():
  return list(productos.find({}, {"_id": 0}))