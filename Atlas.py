from pymongo import MongoClient
from datetime import datetime
dt=datetime.now()
print(dt.month)
x=int(input("Enter number of persons"))
client=MongoClient("mongodb+srv://user_id:Password@cluster0.sqfbmkq.mongodb.net/")
db=client['first']
collec=db['Shift']
date=int(input("Enter the day"))
shi=input("Enter the shift")
l=[]
for i in range(x):
    name=input("Enter the name")
    desig=input("Enter the designation")
    l.append({"name": name, "desig": desig})

data={
    "date": datetime(dt.year, dt.month,dt.day),
    "manpower": l,
    "shift":shi
    }
collec.insert_one(data)
