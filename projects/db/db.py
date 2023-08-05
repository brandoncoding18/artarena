import pymongo 

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["ArtArena"]
users = mydb["Users"]
attacks = mydb["Attacks"]
characters = mydb["Characters"]


