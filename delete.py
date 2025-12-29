from pymongo import MongoClient
client= MongoClient("mongodb://localhost:27017/")
db=client['Firstdb']
collection =db["shift"]
result=collection.delete_many({})
print(result.deleted_count)