from github import Github

from pprint import pprint
import os
import json


# add logged in user's following and follower users to DB
def main():
    token = os.getenv("GITHUB_TOKEN", "no token")  # get token from environment variable
    g = Github(token)  # create github object
    usr = g.get_user()  # get user object

    # get user followers and following
    f1 = usr.get_followers()
    f2 = usr.get_following()

    # add followers and following to JSONs and print
    dctlist = []
    for f in f1:
        dct = makeDict(f.login, g)
        if dct is not None:
            dctlist.append(dct)
            print("follower with loc: ")
            pprint(dct)
            print("")
    json.dump(dctlist, open("followers.json", "w"))

    dctlist = []
    for f in f2:
        dct = makeDict(f.login, g)
        if dct is not None:
            dctlist.append(dct)
            print("following with loc: ")
            pprint(dct)
            print("")
    json.dump(dctlist, open("following.json", "w"))

    # add main user info to separate JSON and print
    dct = makeDict(usr.login, g)
    print("Me: ")
    pprint(dct)
    json.dump(dct, open("me.json", "w"))
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
