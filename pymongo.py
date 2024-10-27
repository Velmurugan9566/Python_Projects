'''import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")

#client=MongoClient('mongodb+srv://velmca24:vel9566@cluster0.i4qp0rb.mongodb.net/?retryWrites=true&w=majority')
con=client.velu.stu
if client:
    print('success')
else:
    pirnt('not')'''
from pymongo import MongoClient
uri = "mongodb+srv://velmca24:vel9566@cluster0.i4qp0rb.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
