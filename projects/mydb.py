from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://brandonweinsteinwriting:ArtTussle@cluster0.sdu3lzu.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


db = client["ArtArena"]

def insertMany(col_name, mylist):
    collection = db[str(col_name)]
    collection.insert_many(mylist)

def dropAll(): 
    for collection in db.list_collection_names(): 
        col = db[str(collection)]
        col.drop()
        print("Successfully dropped: " + collection)
