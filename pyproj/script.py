from github import Github  # for github api
from geopy.geocoders import Nominatim  # Nomanatim is a geocoder for OpenStreetMap data, free api
from timezonefinder import TimezoneFinder  # for finding timezone of a location
from datetime import datetime  # for datetime objects necessary for converting to UTC
from pytz import timezone  # also for converting to UTC
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
    # get naive locations list
    loclist = get_loc_list(f1, f2, g)
    # count locations and remove duplicates
    locdict = {}
    for loc in loclist:
        if loc in locdict:
            locdict[loc] += 1
        else:
            locdict[loc] = 1

    # initialise CSV file
    csvfile = open("locations.csv", "w")
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Location", "Region", "Timezone", "Count"])

    # fill CSV file with data
    geoloc = Nominatim(user_agent="github_locations")  # initialise Nominatim API
    for loc in locdict:
        # get latitude and longitude
        gloc = geoloc.geocode(loc)
        if gloc is not None:
            # get timezones
            reg = TimezoneFinder().timezone_at(lng=gloc.longitude, lat=gloc.latitude)  # get regional timezone
            utc = timezone(reg).localize(datetime.now()).strftime("UTC%z")  # get UTC timezone
            # write to CSV
            csvwriter.writerow([loc, reg, utc, locdict[loc]])
        else:
            del[loc]  # remove location if it cannot be geocoded, as it is not a valid location

    print("\nCSV created, Python script done")


def get_loc_list(followers, following, g):

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
