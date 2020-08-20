# execute this code to erase database
from pymongo import MongoClient
client = MongoClient('mongo', 27017)
client.drop_database('db')
