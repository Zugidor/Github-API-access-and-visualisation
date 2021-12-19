from github import Github
import pymongo

from pprint import pprint
import os
import json


# add logged in user's following and follower users to DB
def main():
    token = os.getenv("GITHUB_TOKEN", "no token")  # get token from environment variable
    g = Github(token)  # create github object
    usr = g.get_user()  # get user object
    # connect to mongo db
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["github"]
    # clear collections, if any, and start empty
    db.followers.drop()
    db.following.drop()
    followers = db["followers"]
    following = db["following"]
    # get user followers and following
    f1 = usr.get_followers()
    f2 = usr.get_following()
    # add followers and following to DB, while avoiding duplicates
    for f in f1:
        dct = makeDict(f.login, g)
        if dct is not None:
            followers.update_one(dct, {"$set": dct}, upsert=True)
    for f in f2:
        dct = makeDict(f.login, g)
        if dct is not None:
            following.update_one(dct, {"$set": dct}, upsert=True)
    dct = makeDict(usr.login, g)
    # print followers, following and user info
    f1 = db.followers.find()
    f2 = db.following.find()
    for f in f1:
        print("follower with loc: ")
        pprint(f)
        print("")
    for f in f2:
        print("following with loc: ")
        pprint(f)
        print("")
    print("Me: ")
    pprint(dct)
    print("\ndone")


def makeDict(username, g):
    # get user object
    usr = g.get_user(username)
    # create dictionary with relevant info
    dct = {
            "login": usr.login,
            "location": usr.location
          }
    # only return dictionary if user has a location
    for k, v in dct.items():
        if k == "location" and v is None:
            return None
    return dct


if __name__ == "__main__":
    main()
