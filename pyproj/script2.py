import pymongo

import pprint

def main():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["github"]
    f1 = db.followers.find()
    f2 = db.following.find()
    for f in f1:
        print("follower with loc: ")
        pprint.pprint(f)
    for f in f2:
        print("following with loc: ")
        pprint.pprint(f)
    print("\ndone")


if __name__ == "__main__":
    main()
