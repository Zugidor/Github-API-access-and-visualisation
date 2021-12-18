import pprint
import pymongo


def main():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["github"]
    users = db.users.find()
    for user in users:
        pprint.pprint(user)
    print("\ndone")


if __name__ == "__main__":
    main()
