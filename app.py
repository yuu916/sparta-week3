from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://sparta:test@cluster0.bwwoewj.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

doc = {
    'name':'太郎',
    'age':24
}

db.users.insert_one(doc)

db.users.insert_one({"name":"bobby", "age":21})
db.users.insert_one({"name":"太郎", "age":20})
db.users.insert_one({"name":"john", "age":30})

all_users = list(db.users.find({},{'_id':False}))

for a in all_users:
    print(a)