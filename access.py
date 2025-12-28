from pymongo import MongoClient
from datetime import datetime
try :
    client= MongoClient("mongodb://localhost:27017/")
    #print("DB connected")
except Exception as e:
    print(e)
db=client['Firstdb']
#print(db.list_collection_names())

D=int(input("Enter the date"))
D=datetime(2025,12, D)
collection =db["shift"]
result = collection.find_one({"date": D})
print(result)
# for doc in collection.find():
#     a="Date is "
#     day=doc.get('date').date()
#     if D.date
#     a=a+str(day)
#     a+="\nManpower is: "

#     for man in doc.get('manpower'):
#         a+=man.get('name')+"("+man.get('desig')+") "
#     a+="\nShift is "+ doc.get('shift')

#     print(a)

    
