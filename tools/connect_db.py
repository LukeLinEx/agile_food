from pymongo import MongoClient
from os.path import expanduser

db = "food_wish_list"
path = expanduser("~/.credentials/{db}.txt".format(db=db))
mongo_connect = open(path, 'r')
ip, port, user, pwd = map(lambda x: x.strip(), mongo_connect.readlines())
client = MongoClient(ip, int(port))


def connect_collection(project, element):
    db = client[project]                ### project is the db_name in db
    db.authenticate(user, pwd)
    collection = eval("db." + element)  ### element is the collection in db

    return collection


dishes = connect_collection(db, "dishes")