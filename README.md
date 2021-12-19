# Github API access and visualisation

CSU-33012 Software Engineering project of Github API access and visualisation of data.

Started with Professor Stephen Barret's Python walkthrough lectures.

I aim to visualise data concerned with user locations and see how GitHub has allowed software developers to connect over vast distances. This tool will look at the location of a logged in user and the locations of all of their followers and followees. I hope to visualise the resulting data in a way that shows how physically ditant developers are closely connected on GitHub.

This is useful for softare developers to see which time zones to worry about if they're considering working with followers or followees on Github. Likewise, it can be used to see if a developer is in the same time zone as their followers or followees. Planning and working around international time zones is an important step in the software engineering process.

API access scripts: Written in Python 3.8.10 with PyGithub.
Data storage: MongoDB with pymongo. CSV and/or JSON files.
Visualisation: D3.js.

## Pre-Requisites

- [Python 3.6 or higher](https://www.python.org/downloads/) installed
- Valid GitHub token set as an environment variable `GITHUB_TOKEN` (this can be done via [Control Panel or System Settings](https://imgur.com/a/CQjLpfk) if you are on Windows. You may need to restart your computer)
- The following Python packages installed (see installed packages with `pip list`):
  - pip (`python3 get-pip.py`)
  - PyGithub (`pip install PyGithub`)
  - pymongo (`pip install pymongo`)
- [Docker](https://www.docker.com/products/docker-desktop) installed.

## Instructions

start.sh starts the mongodb docker container and runs the python script.
