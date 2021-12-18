from github import Github
import os
import json
import pymongo
import script2


# add logged in user to and all followers to DB
def main():
    token = os.getenv("GITHUB_TOKEN", "no token")  # get token from environment variable
    g = Github(token)  # create github object
    usr = g.get_user()  # get user object
    # connect to mongo db
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["github"]
    # clear collections, if any, start empty
    db.followers.drop()
    db.following.drop()
    followers = db["followers"]
    following = db["following"]
    f1 = usr.get_followers()
    f2 = usr.get_following()
    # add followers and followees to DB, while avoiding duplicates
    for f in f1:
        dct = makeDict(f.login, g)
        followers.update_one(dct, {"$set": dct}, upsert=True)
    for f in f2:
        dct = makeDict(f.login, g)
        following.update_one(dct, {"$set": dct}, upsert=True)


def makeDict(username, g):
    usr = g.get_user(username)  # get user object
    dct = {
            "login": usr.login,
            "name": usr.name,
            "location": usr.location
          }
    # remove null values
    for k, v in dct.items():
        if v is None:
            del dct[k]
    return dct


if __name__ == "__main__":
    main()
