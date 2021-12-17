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
        "name": "",
        "company": "",
        "location": "",
        "email": "",
        "blog": ""
    }
#if usr.name is not None:
    dct["name"] = usr.name
#if usr.email is not None:
    dct["email"] = usr.email
#if usr.location is not None:
    dct["location"] = usr.location
#if usr.company is not None:
    dct["company"] = usr.company
#if usr is not None:
    dct["blog"] = usr.blog
    return dct
