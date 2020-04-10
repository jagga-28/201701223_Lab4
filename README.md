# 201701223_Lab4
NoSQL Lab 4 - MongoDB

from pymongo import MongoClient
client=MongoClient('mongodb+srv://HitarthBharad:iamHitarthBharad@cluster0-3igae.mongodb.net/test?retryWrites=true&w=majority')

db = client['HitarthBharad']
col = db['posts']
