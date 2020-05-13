import pymongo
from pymongo import MongoClient
uri = "mongodb+srv://user:RtbNqkZV4b86QBdw@cluster0-1vo38.mongodb.net/test?retryWrites=true&w=majority" #add in your MongoDB connection string here
cluster = MongoClient(uri)

db = cluster["suspect_database"] #insert name of database you created earlier here
collection = db["suspect"] #insert name of collection you created earlier here

result = collection.find(
            filter = {"$and" : [
                {"age": {"$gte": 20, "$lt": 30}},
                {"company": {"$in": ["PRINTSPAN", "TECHMANIA", "NEPTIDE", "MULTRON", "SKYNET", "UPDAT", "STANTON"]}},
                {"eyeColor": {"$nin": ["black", "brown"]}},
                {"friends.name": {"$regex": "^C"}}
            ]},
            projection = {
                "name": 1,
                "_id": 0
            }
        )

#Note: collection.find() returns you a cursor object so need to iterate through result to get the actual values.
for i in result:
    print (i)
