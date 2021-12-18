import pprint
import pymongo


def main():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client.class_db
    users = db.users.find()
    for user in users:
        pprint.pprint(user)
    print("\ndone")
