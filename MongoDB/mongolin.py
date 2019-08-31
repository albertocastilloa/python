import pymongo
import datetime

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.classDB

classroom = db.classroom.find()

db.classroom.insert_one(
{
    'name':'Ahmed',
    'row':3,
    'favorite_python_library':'Matplotlib',
    'hobbies':['Running', 'Stargazing', 'Reading'],
    'date': datetime.datetime.utcnow()
},
)

db.classroom.update_one(
    {'name':'Ahmed'},
    {'$set':
        {'row':5}
    }
)

for i in classroom:
    print(i)