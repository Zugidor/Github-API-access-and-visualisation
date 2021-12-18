import pymongo


def main():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client.class_db
    db.users.delete_many({})


if __name__ == "__main__":
    main()
