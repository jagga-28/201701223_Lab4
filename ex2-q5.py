from pprint import pprint
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure,OperationFailure
connectionString="mongodb+srv://HitarthBharad:iamHitarthBharad@cluster0-3igae.mongodb.net/test?retryWrites=true&w=majority"
client=MongoClient(connectionString)
db=client["201701222"]
mycol=db["Sales_rep"]

try:
    client.admin.command('ismaster')

except ConnectionFailure:
    print('Server not available')

except OperationFailure:
    print('wrong credentials')

else:
    print('connected to database')
    val = db.Sales.aggregate([
                {"$unwind" : {"path" : "$items"}},
                {"$group" : {
                        "_id" : "$items.name",
                        "sales_history" : {"$push" : {"storeLocation" : "$storeLocation","quantity" : {"$multiply" : ["$items.price","$items.quantity"]}}}
                            }
                },
                #{"$out" : "stock_replenish"}
            ])
    for v in val:
        mycol.insert_one(v)

finally:
	client.close()