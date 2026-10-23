from fastapi import FastAPI
from pymongo import MongoClient
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app, endpoint="/metrics")

# Mongo DB connection
mongo_client = MongoClient("mongodb://admin:web3@mongo-service.default.svc.cluster.local:27017/")
database = mongo_client["desarrollo_web_3"]
products = database["productos"]

@app.get("/")
def default():
  return {"message": "Uvicorn corriendo"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/error_400")
def get_error():
    raise HTTPException(status_code=400, detail="ID no puede ser 0.")
    return []

@app.get("/error_500")
def get_error():
    raise HTTPException(status_code=500, detail="Error al conectarse a la base de datos.")
    return []

@app.get("/productos")
def get_productos():
    productList = list(products.find({}))   
    return {"productos": productList}

