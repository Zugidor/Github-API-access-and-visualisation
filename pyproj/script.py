from github import Github
import os
import json


def main():
    token = os.getenv("GITHUB_TOKEN", "no token")  # get token from environment variable
    g = Github(token)  # create github object
    usr = g.get_user("Zugidor")
    dctNating = getDetails(usr)
    print(json.dumps(dctNating, indent=2))


def getDetails(usr):
    dct = {
            "login": usr.login,
            "name": usr.name,
            "company": usr.company,
            "location": usr.location,
            "email": usr.email,
            "blog": usr.blog
           }
    return dct
