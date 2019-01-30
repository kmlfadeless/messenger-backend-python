import pymongo


def db():
    f = open("passwords.txt", "r")
    lines = f.readlines()
    credentials = lines[0]
    f.close()
    client = pymongo.MongoClient('mongodb+srv://'+credentials+'@kml-ijrny.mongodb.net/test?retryWrites=true')
    return client.testdb
