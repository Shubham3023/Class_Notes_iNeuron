import pymongo

client = pymongo.MongoClient("mongodb+srv://sam01091994:Shub1994@clustershub.jujlbeo.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['myinfo']
collection = database["shubham"]
collection1 = database["dpkt"]
"""
record = collection.find()
for i in record :
    print(i)
"""
"""
data = collection.find({"companyName": "iNeuron"})
"""

data = collection.find({"courseOffered": {"$gt" : "E"}})  #course offered name starts with letter greater than E
for i in data:
    print(i)





