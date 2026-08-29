
from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://admin_user:web3@localhost:27017/")
mongo_client = MongoClient(MONGO_URI)
db = mongo_client[os.getenv("MONGO_DB", "web3_db")]
productos = db[os.getenv("PRODUCTOS_COLLECTION", "productos")]


@app.get("/")
def default():
    return {"message": "Uvicorn server running"}

@app.get("/health")
def health_check():
    return {"status":"ok"}

@app.get("/Productos")
def get_productos():
    return list(productos.find({}, {"_id": 0}))
 