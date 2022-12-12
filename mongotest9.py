import pymongo
client = pymongo.MongoClient("mongodb+srv://pranav09:<password>@cluster0.lqxb7ue.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d= {
    'name': 'pranav',
    'email':' p.com',
     'surname': 'vanage'
}
db1 = client['mongotest']
coll = db1['pv1']
coll.insert_one(d)