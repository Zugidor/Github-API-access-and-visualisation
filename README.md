# Github API access and visualisation

CSU-33012 Software Engineering project of Github API access and visualisation of data.

Started with Professor Stephen Barret's Python walkthrough lectures.

## Introduction

I aim to visualise data concerned with user locations and see how GitHub has allowed software developers to connect over vast distances. This tool looks at the location of a logged in user and the locations of all of their followers and followees, and converts them into timezones. I hope to visualise the resulting data in a way that shows how developers may be closely connected on GitHub but how far apart they are geographically, especially in regards to timezones, which affect waking/working hours.

This is useful for softare developers to see which timezones to worry about if they're considering collaborating with followers or followees on Github, as it is likely that future or past collaborators are either followed or followers, or both. Planning and working around international time zones is an important step in the software engineering process, and this tool help provide insight on this, especially in the light of the current era of remote work becoming ever more popular/necessary.

Because this tool is not intended to process a very large amount of data, due to the inherent limitations on the number of API calls GitHub allows (5,000 per hour), I have opted to not use a database. Instead, I have used a CSV file, which is easy for humans and programs to read and write to.

Even though it's public information, no GitHub usernames or locations are stored, only regional and UTC timezones (for example, Europe/Paris UTC+01:00 or Asia/Kolkata UTC+05:30), and these timezones are not linked nor traced to individual GitHub users. As such, anonymity is maintained and there are no privacy concerns.

API access scripts: Written in Python 3.8.10 with PyGithub.
Data storage: CSV file.
Visualisation: Not yet implemented.

## Pre-Requisites

You need:

- [Python 3.6 or higher](https://www.python.org/downloads/) installed
- A valid GitHub token set as an environment variable `GITHUB_TOKEN` (this can be done via [Control Panel or System Settings](https://imgur.com/a/CQjLpfk) if you are on Windows. You may need to restart your computer)
- The following Python packages installed:
  - pip
    - PyGithub
    - geopy
    - timezonefinder
    - datetime
    - pytz

Check your installed packages with `pip list`

If you don't have pip, run getpip.sh or `python3 get-pip.py`

To install the other packages, run getpacks.sh or `pip install -r requirements.txt`

## Instructions

1. Run start.sh to run the python script and start the http server.
2. Navigate to the webpage at <http://localhost:8080/> in your browser to view the visualisation.
