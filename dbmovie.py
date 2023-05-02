import requests
from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://sparta:test@cluster0.bwwoewj.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

db.movies.drop()