import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client['library']

cl = db['books']

#d = {'name':'physics','price':230}
'''d= [
    {'name':'Chemistry','price':700},
    {'name':'Biology','price':750}
   ]
cl.insert_many(d)
print("inserted")'''

'''x= cl.find_one()
print(x)'''

#print(client.list_database_names())

'''dblist= client.list_database_names()
if 'library' in dblist:
    print("The database exists")'''

'''x=cl.find()
for i in x:
    print(i)'''

collist= db.list_collection_names())

