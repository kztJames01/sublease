
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from urllib.parse import quote_plus


username = quote_plus(os.getenv("MONGO_USER", "default_username"))
password = quote_plus(os.getenv("MONGO_PASSWORD", "default_password"))
uri = f"mongodb+srv://{username}:{password}@cluster0.ysba7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['Authentication']
collection = db['Users']
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)