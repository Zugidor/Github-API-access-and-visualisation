from github import Github

from pprint import pprint
import os
import json


def main():
    print("This tool inspects and returns JSONs with the locations of all the followers and following users of a "
          "given GitHub user.")
    usrnm = input("Enter the Github login username of the account you wish to inspect: ")
    token = os.getenv("GITHUB_TOKEN", "no token")  # get token from environment variable
    g = Github(token)  # create github object
    usr = g.get_user(usrnm)  # get user object

    # get user followers and following
    f1 = usr.get_followers()
    f2 = usr.get_following()

    # add followers and following to JSONs and print
    count = 0
    dctlist = []
    for f in f1:
        dct = makeDict(f.login, g)
        if dct is not None:
            dctlist.append(dct)
            print("follower with loc: ")
            pprint(dct)
            print("")
        count += 1
        if count == 300:
            print("limit of 300 followers reached")
            break
    json.dump(dctlist, open("followers.json", "w"))

    count = 0
    dctlist = []
    for f in f2:
        dct = makeDict(f.login, g)
        if dct is not None:
            dctlist.append(dct)
            print("following with loc: ")
            pprint(dct)
            print("")
        count += 1
        if count == 300:
            print("limit of 300 following reached")
            break
    json.dump(dctlist, open("following.json", "w"))

    # add main user info to separate JSON and print
    dct = makeDict(usr.login, g)
    print("Me: ")
    pprint(dct)
    json.dump(dct, open("me.json", "w"))
    print("\nJSONs created, Python script done")


def makeDict(username, g):
    # get user object
    usr = g.get_user(username)
    if usr.location is None:
        return None
    # create dictionary with relevant info
    dct = {
            "location": usr.location
          }
    # only return dictionary if user has a location
    return dct


if __name__ == "__main__":
    main()
