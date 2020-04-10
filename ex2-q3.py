from pprint import pprint
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure,OperationFailure
client=MongoClient("mongodb+srv://HitarthBharad:iamHitarthBharad@cluster0-3igae.mongodb.net/test?retryWrites=true&w=majority")
db=client["201701222"]
try:
    client.admin.command('ismaster')

except ConnectionFailure:
    print('Server not available')

except OperationFailure:
    print('wrong credentials')

else:
    print('connected to database')
    casa=db.Sales.aggregate([{ "$group": { "_id": "$storeLocation", "total": { "$sum":1 } } }])


finally:
	client.close()

for docs in casa:
    print(docs)