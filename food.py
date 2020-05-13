import pymongo

# Create
# Connected to a cleint
client = pymongo.MongoClient(
    "mongodb+srv://user:RtbNqkZV4b86QBdw@cluster0-1vo38.mongodb.net/test?retryWrites=true&w=majority")

# Connecting / creating a database
Consumerables = client.get_database("consumerables")

# Connecting / creaing a collection in a database
Fruits = Consumerables.get_collection("Fruits")

# Insert one document into a collection
Fruits.insert_one({"item": "bannana", "price": 3, "weight": 300, "length": 10})
# Insert many document into a collection
manystuff = [{
    "Item": "Apple",
    "Weight": 50,
    "Price": 0.30,
    "Radius": "5cm"  # Dynamic schema! :o
}, {
    "Item": "Grapes",
    "Weight": 100,
    "Price": 10,
    "Colour": "Green",
    "Bundle_Quantity": 42
}]
Fruits.insert_many(manystuff)

# Read

# List down all database in a client
databases = client.list_database_names()
print(databases)

# List down all collections in a database
collections = Consumerables.list_collection_names()
print(collections)

# List down all documents in a collection
documents = Fruits.find()
# for stuff in documents:
#     print(stuff)

# UPDATE

# Updatea field in a document in a collection
for stuff in documents:
    print(stuff)
Fruits.update_one({"Item": "Apple"}, {"$set": {"Weight": 70}})

# Updating many fields in a document in a collection
Fruits.update_many({"price": {"$lte": 3.00}}, {"$set": {"price": 4.00}})

# Delete
print("Delete")
# Deleting a document in a collection
for stuff in documents:
    print(stuff)
print("Delete 1")
Fruits.delete_one({"item": "bannana"})
for stuff in documents:
    print(stuff)
Fruits.delete_many({})
print("Delete everything")
for stuff in documents:
    print(stuff)
