import pymongo
from pymongo import MongoClient
# add in your MongoDB connection string here
uri = "mongodb+srv://user:RtbNqkZV4b86QBdw@cluster0-1vo38.mongodb.net/test?retryWrites=true&w=majority"
cluster = MongoClient(uri)

# insert name of database you created earlier here
db = cluster["suspect_database"]
# insert name of collection you created earlier here
collection = db["suspect"]

pipeline = [
    {"$match": {"$and": [
        {"age": {"$gte": 20, "$lt": 30}},
        {"company": {"$in": ["PRINTSPAN", "TECHMANIA",
                             "NEPTIDE", "MULTRON", "SKYNET", "UPDAT", "STANTON"]}},
        {"eyeColour": {"$nin": ["black", "brown"]}},
        {"friends.name": {"$regex": "^C"}},
        {"gender": "female"}
    ]}},
    {"$project":
        {"name": 1, "_id": 0}}
]

# time to use the pipeline!
# Note: pipeline aggregation returns you a cursor object to the MongoDB database so you need to iterate through result to get the actual values.
result = collection.aggregate(pipeline)
for i in result:
    print(i)
