from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)

# Pridobi povezavo iz okolja
mongo_uri = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/mojabaza')
client = MongoClient(mongo_uri)
db = client["mojabaza"]  # popravi iz .get_database() v natančno ime baze

@app.route('/')
def home():
    db.status.insert_one({"msg": "Pozdrav iz Flask aplikacije!"})
    return "Pozdravljeni! Nova verzija aplikacije je aktivna."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
