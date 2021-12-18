# Github API access and visualisation

CSU-33012 Software Engineering project of Github API access and visualisation of data.

Started with Stephen Barret's Python walkthrough lectures.

I aim to visualise data concerned with user locations and see how GitHub has allowed software developers to connect over vast distances. This tool will look at the location of a logged in user and the locations of all of their followers and followees. I hope to visualise the resulting data in a way that shows how physically ditant developers are closely connected on GitHub.

API access scripts: Written in Python 3.8.10 with PyGithub.
Data storage: MongoDB with pymongo.
Visualisation: D3.js.

## Pre-Requisites

- [Python 3.6 or higher](https://www.python.org/downloads/) installed
- Valid GitHub token set to system environment variable `GITHUB_TOKEN` (this is done via control panel if you are on Windows. You may need to restart your computer)
- The following Python packages installed (see installed packages with `pip list`):
  - pip (`python3 get-pip.py`)
  - PyGithub (`pip install PyGithub`)
  - pymongo (`pip install pymongo`)
- [Docker](https://www.docker.com/products/docker-desktop) installed.

## Instructions

start.sh starts the mongodb docker container and the python shell.

Run python scripts in the python shell.

Example:

```bash
./start.sh
import script
script.main()```
