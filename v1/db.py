import pymongo


def db():
    client = pymongo.MongoClient('mongodb://kml-shard-00-00-ijrny.mongodb.net:27017,kml-shard-00-01-ijrny.mongodb.net:27017,kml-shard-00-02-ijrny.mongodb.net:27017/test?ssl=true&replicaSet=KML-shard-0&authSource=admin&retryWrites=true')
    f = open("passwords.txt", "r")
    lines = f.readlines()
    username = lines[0]
    password = lines[1]
    f.close()
    return client.the_database.authenticate(username, password, source='testdb')
