from github import Github
import os
import json
import pymongo
import script2
import clear


def main():
    token = os.getenv("GITHUB_TOKEN", "no token")  # get token from environment variable
    g = Github(token)  # create github object
    usr = g.get_user("nating")  # get user object
    dct = makeDict(usr)  # get details as dictionary
    print("raw dict: " + json.dumps(dct, indent=2))
    # remove null values
    for k, v in dct.items():
        if v is None:
            del dct[k]
    print("clean dict: " + json.dumps(dct, indent=2))
    # connect to mongo
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client.class_db
    # insert into collection
    db.users.insert_one(dct)
    script2.main()
    clear.main()
    script2.main()


def makeDict(usr):
    dct = {
        "login": usr.login,
        "name": usr.name,
        "company": usr.company,
        "location": usr.location,
        "email": usr.email,
        "blog": usr.blog
    }
    return dct


if __name__ == "__main__":
    main()
