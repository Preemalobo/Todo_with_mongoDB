
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo

# uri = "mongodb+srv://preemalobo:1234@cluster0.jgme9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
uri = "mongodb+srv://preemalobo:1234@cluster0.jgme9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = pymongo.MongoClient(uri, server_api=ServerApi('1'))

db=client.todo_db
collection=db["todo_data"]