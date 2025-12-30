from urllib.parse import quote_plus
from pymongo import MongoClient
from bson.json_util import dumps

username = "compliance027_db_user"
password = quote_plus("Annot27@viT")  

uri = f"mongodb+srv://{username}:{password}@cluster1.njaepi9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"

client = MongoClient(uri)

# Test connection
print(client.list_database_names())

# Create House DB and HousePricingDB collection
db = client["House"]
collection = db["HousePricingDB"]

priceInfo = [
    {"location": "Bangalore","price": 7500000,"bedrooms": 3,"bathrooms": 2,"area_sqft": 1500,"floor":3},
    {"location": "Mumbai","price": 12000000,"bedrooms": 4,"bathrooms": 3,"area_sqft": 2000,"floor":5},
    {"location": "Chennai","price": 6000000,"bedrooms": 2,"bathrooms": 2,"area_sqft": 1200,"floor":2},
    {"location": "Delhi","price": 9000000,"bedrooms": 3,"bathrooms": 2,"area_sqft": 1600,"floor":4},
    {"location": "Kolkata","price": 5000000,"bedrooms": 2,"bathrooms": 1,"area_sqft": 1100,"floor":1},
    {"location": "Hyderabad","price": 7000000,"bedrooms": 3,"bathrooms": 2,"area_sqft": 1400,"floor":3},
    {"location": "Pune","price": 8000000,"bedrooms": 3,"bathrooms": 2,"area_sqft": 1550,"floor":4},
    {"location": "Patna","price": 4000000,"bedrooms": 2,"bathrooms": 5,"area_sqft": 1000,"floor":2},
    {"location": "Patna","price": 4050000,"bedrooms": 7,"bathrooms": 3,"area_sqft": 1050,"floor":2},
    {"location": "Patna","price": 4900000,"bedrooms": 5,"bathrooms": 8,"area_sqft": 1200,"floor":6},
    {"location": "Jaipur","price": 4500000,"bedrooms": 2,"bathrooms": 4,"area_sqft": 1050,"floor":2},
    {"location": "Lucknow","price": 4800000,"bedrooms": 2,"bathrooms": 6,"area_sqft": 1100,"floor":3}
]
# result = collection.insert_many(priceInfo)
# print("Inserted IDs:", result.inserted_ids)
#Operations in a typical aggreagtion pipeline
#input -->$match--> $group -->$sort -->output
print(list(db.HousePricingDB.aggregate([
    {"$match": {"location": "Patna"}}
]))) 
# for python use direct query for mongo shell
documents = db.HousePricingDB.aggregate([
    {"$match": {"location": "Patna"}},
    {"$group":{"_id":"$_id","price":{"$first":"$price"},"floorrooms":{"$sum":{"$add":["$bedrooms","$floor"]}}}},
    {"$sort":{"floorrooms":1}},
    ])
o=[]
with open("data.json", "a") as f:
    for doc in documents:
        o.append({"location":str(doc["_id"]), "price": doc["price"], "floorrooms": doc["floorrooms"]})
        f.write(dumps(o)+"\n")
#for doc in documents:
#    print(doc)