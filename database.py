import pymongo

passd = "ckZpYU8HGpnc5i9i"
named = "Trading_bot"
# named = "test"

client = pymongo.MongoClient("mongodb+srv://test:"+passd+"@cluster1.9glic.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.get_database(named)

class user():
    def findpost1(collection):
        collection = db[collection]
        data = collection.find({})
        numbercomment = collection.count_documents({})
        return data, numbercomment

    def findallpost(collection):
        collection = db[collection]
        ps = {"Status":"True"}
        data = collection.find(ps)
        numbercomment = collection.count_documents(ps)
        return data, numbercomment

    def findpostbyow(collection, new):
        collection = db[collection]
        ps = {"Owenr":new}
        data = collection.find(ps)
        return data

    def insertpost(collection, IDO, IDP):
        collection = db[collection]
        Comment = {"ID":IDO, "IDP":IDP}
        collection.insert_one(Comment)

    def countdelpost(collection):
        collection = db[collection]
        data = collection.find({})
        numbercomment = collection.count_documents({})
        return data, numbercomment

    def deletepost(collection, IDO, IDP):
        collection = db[collection]
        ps  = {"ID":IDO, "IDP":IDP}
        collection.delete_one(ps)

    def deleteall(collection):
        collection = db[collection]
        collection.delete_many({})

    def edit(collection, Owenr, Image):
        collection = db[collection]
        api = {"Owenr":Owenr}
        api1 = {"$set":{"Image":Image}}
        collection.update_one(api, api1)

    def edit1(collection, IDO, Status):
        collection = db[collection]
        api = {"ID":IDO}
        api1 = {"$set":{"Status":Status}}
        collection.update_one(api, api1)

    def edit2(collection, Owenr, Status):
        collection = db[collection]
        api = {"Owenr":Owenr}
        api1 = {"$set":{"Status":Status}}
        collection.update_one(api, api1)