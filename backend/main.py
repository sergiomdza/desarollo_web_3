from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()
mongocliente = MongoClient("mongodb://admin_user:web@mongo_container:27017/")
database = mongocliente["desarrollo_web_3"]
productos = database["productos"]


@app.get("/helpth")
def health_check():
    return("canto:exito")

@app.get("/productos")
def get_productos():
    return list(productos.find({},{"_id":0}))

## canto se vino a qui en mi dentro de mi :) p