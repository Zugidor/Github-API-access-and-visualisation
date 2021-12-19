from github import Github
import os
import csv


def main():
    print("This tool inspects and returns CSV with the locations of all the followers and following users of a "
          "given GitHub user.")  # print info
    usrnm = input("Enter the Github login username of the account you wish to inspect: ")  # get username
    token = os.getenv("GITHUB_TOKEN", "no token")  # get token from environment variable
    g = Github(token)  # create main github object from token
    usr = g.get_user(usrnm)  # create main user object from inputted username

    # get user followers and following
    f1 = usr.get_followers()
    f2 = usr.get_following()
    # initialise CSV file
    csvfile = open("locations.csv", "w")
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Location", "Count"])
    # get locations list
    loclist = getloclist(f1, f2, g)
    # add locations to CSV
    for loc in set(loclist):
        csvwriter.writerow([loc, loclist.count(loc)])  # TODO: remove dupes and count properly
    print("\nCSV created, Python script done")


def getloclist(followers, following, g):
    # get followers locations
    count = 0
    loclist = []
    for f in followers:
        loc = g.get_user(f.login).location
        if loc is not None:
            loclist.append(loc)
        count += 1
        if count == 300:
            print("limit of 300 followers reached")
            break
    # get following locations
    count = 0
    for f in following:
        loc = g.get_user(f.login).location
        if loc is not None:
            loclist.append(loc)
        count += 1
        if count == 300:
            print("limit of 300 following reached")
            break
    # get main user location
    loc = g.get_user().location
    if loc is not None:
        loclist.append(loc)

    return loclist


if __name__ == "__main__":
    main()
