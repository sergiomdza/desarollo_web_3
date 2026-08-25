from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()
mongocliente = MongoClient("mongodb://localhost:27017/")
database = mongo_client["desarrollo_web_3"]
productos = database["productos"]


@app.get("/helpth")
def health_check():
    return("canto:exito")

## canto se vino a qui en mi dentro de mi :) p