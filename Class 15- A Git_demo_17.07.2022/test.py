import pymongo
client = pymongo.MongoClient("mongodb+srv://sam01091994:Shub1994@clustershub.jujlbeo.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "shubham" ,
    "email" : "shubham@ineuron.ai",
    "surname" : "verma"
}
d = {
    "name" : "shubham" ,
    "email" : "shubham@ineuron.ai",
    "surname" : "verma"
}
d = {
    "name" : "shubham" ,
    "email" : "shubham@ineuron.ai",
    "surname" : "verma"
}
d = {
    "name" : "shubham" ,
    "email" : "shubham@ineuron.ai",
    "surname" : "verma"
}d = {
    "name" : "shubham" ,
    "email" : "shubham@ineuron.ai",
    "surname" : "verma"
}d = {
    "name" : "shubham" ,
    "email" : "shubham@ineuron.ai",
    "surname" : "verma"
}d = {
    "name" : "shubham" ,
    "email" : "shubham@ineuron.ai",
    "surname" : "verma"
}



db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)



