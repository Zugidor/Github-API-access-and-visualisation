import github  # for github api
from geopy.geocoders import Nominatim  # Nomanatim is a geocoder for OpenStreetMap data, free api
from timezonefinder import TimezoneFinder  # for finding timezone of a location
from datetime import datetime  # for datetime objects necessary for converting to UTC
from pytz import timezone  # also for converting to UTC
import os
import csv


def main():

    print("This tool inspects and returns CSV with the timezones "
          "of all the followers and following users of a given GitHub user.")  # print info
    token = os.getenv("GITHUB_TOKEN", "no token")  # get token from environment variable
    g = github.Github(token)  # create main github object from token
    usr = None
    while True:
        usrnm = input("Enter the Github login username of the account you wish to inspect: ")  # get username
        try:
            usr = g.get_user(usrnm)  # create main user object from inputted username
        except github.GithubException:
            print("Invalid username or token")
        if usr is not None:
            break

    print("Collecting location data...")

    # get user followers and following
    f1 = usr.get_followers()
    f2 = usr.get_following()
    # get locations list
    loclist = get_loc_list(f1, f2, g)

    print("Writing regional timezones to CSV...")

    # initialise regional timezones CSV file
    csvfile = open("regions.csv", "w")
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Region", "Count"])

    # get regional and UTC timezones for each location, count occurrences, and write data to CSV
    regdict = {}
    utcdict = {}
    geoloc = Nominatim(user_agent="github_locations")  # initialise Nominatim API
    for loc in loclist:
        # get latitude and longitude
        gloc = geoloc.geocode(loc)
        if gloc is not None:
            reg = TimezoneFinder().timezone_at(lng=gloc.longitude, lat=gloc.latitude)  # get regional timezone
            # build dictionary of regional timezones and their counts
            if reg in regdict:
                regdict[reg] += 1
            else:
                regdict[reg] = 1
    reglist = sorted(regdict.items(), key=lambda x: x[1], reverse=True)  # sort dictionary by count
    for i in reglist:  # i[0] is reg, i[1] is count
        csvwriter.writerow([i[0], i[1]])  # write to CSV
        utc = timezone(i[0]).localize(datetime.now()).strftime("UTC%z")  # get UTC timezone
        # build dictionary of UTC timezones and their counts
        if utc in utcdict:
            utcdict[utc] += 1 * i[1]
        else:
            utcdict[utc] = 1 * i[1]
    utclist = sorted(utcdict.items(), key=lambda x: x[1], reverse=True)  # sort dictionary by count

    print("Writing UTC timezones to CSV...")

    # initialise UTC timezones CSV file
    csvfile = open("utc.csv", "w")
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Timezone", "Count"])
    for i in utclist:  # i[0] is utc, i[1] is count
        csvwriter.writerow([i[0], i[1]])  # write to CSV

    print("CSV files created,\nPython script done!")


def get_loc_list(followers, following, g):

    # get followers locations
    count = 0
    loclist = []
    for f in followers:
        loc = g.get_user(f.login).location
        if loc is not None and loc != "" and not loc.__contains__("wa.me"):
            loclist.append(loc)
        count += 1
        if count == 300:
            print("limit of 300 followers reached!")
            break

    # get following locations
    count = 0
    for f in following:
        loc = g.get_user(f.login).location
        if loc is not None and loc != "" and not loc.__contains__("wa.me"):
            loclist.append(loc)
        count += 1
        if count == 300:
            print("limit of 300 following reached!")
            break

    # get main user location
    loc = g.get_user().location
    if loc is not None:
        loclist.append(loc)

    # remove "/", "&", and "."
    for loc in loclist:
        if loc.__contains__("."):
            newloc = loc.replace(".", "")
            loclist.remove(loc)
            loclist.append(newloc)
        if loc.__contains__("/"):
            newloc = loc[0:loc.find("/")]
            loclist.remove(loc)
            loclist.append(newloc)
        if loc.__contains__("&"):
            newloc = loc[0:loc.find("&")]
            loclist.remove(loc)
            loclist.append(newloc)

    return loclist


if __name__ == "__main__":
    main()
